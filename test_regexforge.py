#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for RegexForge
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from regexforge import (
    RegexForge, PatternLibrary, CodeGenerator, RegexAnalyzer,
    MatchResult, RegexAnalysis
)


class TestPatternLibrary(unittest.TestCase):
    """Test PatternLibrary class"""
    
    def test_list_patterns(self):
        """Test listing all patterns"""
        patterns = PatternLibrary.list_patterns()
        self.assertGreater(len(patterns), 0)
    
    def test_list_patterns_by_category(self):
        """Test listing patterns by category"""
        patterns = PatternLibrary.list_patterns("basic")
        for p in patterns:
            self.assertEqual(p["category"], "basic")
    
    def test_get_pattern(self):
        """Test getting a pattern by name"""
        pattern = PatternLibrary.get_pattern("email")
        self.assertIsNotNone(pattern)
        self.assertIn("@", pattern)
    
    def test_get_nonexistent_pattern(self):
        """Test getting a nonexistent pattern"""
        pattern = PatternLibrary.get_pattern("nonexistent")
        self.assertIsNone(pattern)
    
    def test_get_categories(self):
        """Test getting all categories"""
        categories = PatternLibrary.get_categories()
        self.assertIn("basic", categories)
        self.assertIn("network", categories)


class TestCodeGenerator(unittest.TestCase):
    """Test CodeGenerator class"""
    
    def test_generate_python(self):
        """Test Python code generation"""
        code = CodeGenerator.generate("python", r"\d+", "i")
        self.assertIsNotNone(code)
        self.assertIn("import re", code)
        self.assertIn("re.IGNORECASE", code)
    
    def test_generate_javascript(self):
        """Test JavaScript code generation"""
        code = CodeGenerator.generate("javascript", r"\d+", "gi")
        self.assertIsNotNone(code)
        self.assertIn("const pattern", code)
        self.assertIn("/gi", code)
    
    def test_generate_java(self):
        """Test Java code generation"""
        code = CodeGenerator.generate("java", r"\d+", "i")
        self.assertIsNotNone(code)
        self.assertIn("Pattern.compile", code)
    
    def test_generate_go(self):
        """Test Go code generation"""
        code = CodeGenerator.generate("go", r"\d+", "i")
        self.assertIsNotNone(code)
        self.assertIn("regexp.MustCompile", code)
    
    def test_generate_rust(self):
        """Test Rust code generation"""
        code = CodeGenerator.generate("rust", r"\d+", "i")
        self.assertIsNotNone(code)
        self.assertIn("Regex::new", code)
    
    def test_generate_unsupported_language(self):
        """Test unsupported language"""
        code = CodeGenerator.generate("unsupported", r"\d+")
        self.assertIsNone(code)


class TestRegexAnalyzer(unittest.TestCase):
    """Test RegexAnalyzer class"""
    
    def test_analyze_valid_pattern(self):
        """Test analyzing a valid pattern"""
        analysis = RegexAnalyzer.analyze(r"\d+")
        self.assertTrue(analysis.is_valid)
        self.assertIsNone(analysis.error)
    
    def test_analyze_invalid_pattern(self):
        """Test analyzing an invalid pattern"""
        analysis = RegexAnalyzer.analyze(r"[")
        self.assertFalse(analysis.is_valid)
        self.assertIsNotNone(analysis.error)
    
    def test_analyze_groups(self):
        """Test analyzing groups"""
        analysis = RegexAnalyzer.analyze(r"(\w+)@(\w+)\.(?P<domain>\w+)")
        self.assertTrue(analysis.is_valid)
        self.assertEqual(analysis.groups_count, 3)
        self.assertIn("domain", analysis.named_groups)
    
    def test_complexity_score(self):
        """Test complexity score calculation"""
        simple = RegexAnalyzer.analyze(r"\d+")
        complex_pattern = RegexAnalyzer.analyze(r"(?:[a-z]+(?:\d+)?)+")
        
        # Simple patterns should have lower complexity
        self.assertLess(simple.complexity_score, 50)
    
    def test_suggestions(self):
        """Test suggestion generation"""
        analysis = RegexAnalyzer.analyze(r".*.*")
        self.assertTrue(len(analysis.suggestions) > 0)


class TestRegexForge(unittest.TestCase):
    """Test RegexForge main class"""
    
    def setUp(self):
        self.forge = RegexForge()
    
    def test_test_pattern_basic(self):
        """Test basic pattern matching"""
        results, error = self.forge.test_pattern(r"\d+", "Hello 123 World 456")
        self.assertIsNone(error)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].match_text, "123")
        self.assertEqual(results[1].match_text, "456")
    
    def test_test_pattern_with_flags(self):
        """Test pattern matching with flags"""
        results, error = self.forge.test_pattern(r"hello", "HELLO world", "i")
        self.assertIsNone(error)
        self.assertEqual(len(results), 1)
    
    def test_test_pattern_invalid(self):
        """Test invalid pattern"""
        results, error = self.forge.test_pattern(r"[", "test")
        self.assertIsNotNone(error)
        self.assertEqual(len(results), 0)
    
    def test_test_pattern_groups(self):
        """Test pattern with groups"""
        results, error = self.forge.test_pattern(
            r"(\w+)@(\w+)\.(?P<domain>\w+)",
            "test@example.com"
        )
        self.assertIsNone(error)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].groups, ("test", "example", "com"))
        self.assertEqual(results[0].named_groups, {"domain": "com"})
    
    def test_performance_test(self):
        """Test performance test"""
        perf = self.forge.performance_test(r"\d+", "test 123 test", iterations=100)
        self.assertIn("iterations", perf)
        self.assertIn("total_time_ms", perf)
        self.assertIn("avg_time_us", perf)
    
    def test_format_output_json(self):
        """Test JSON output formatting"""
        results, _ = self.forge.test_pattern(r"\d+", "test 123")
        output = self.forge.format_output_json(results, r"\d+", "test 123")
        self.assertIn('"pattern"', output)
        self.assertIn('"matches"', output)
    
    def test_format_output_html(self):
        """Test HTML output formatting"""
        results, _ = self.forge.test_pattern(r"\d+", "test 123")
        output = self.forge.format_output_html(results, r"\d+", "test 123")
        self.assertIn("<!DOCTYPE html>", output)
        self.assertIn("RegexForge", output)


class TestMatchResult(unittest.TestCase):
    """Test MatchResult dataclass"""
    
    def test_to_dict(self):
        """Test MatchResult to_dict method"""
        result = MatchResult(
            match_text="test",
            start=0,
            end=4,
            groups=("a", "b"),
            named_groups={"name": "value"}
        )
        d = result.to_dict()
        self.assertEqual(d["match"], "test")
        self.assertEqual(d["start"], 0)
        self.assertEqual(d["end"], 4)
        self.assertEqual(d["groups"], ["a", "b"])
        self.assertEqual(d["named_groups"], {"name": "value"})


if __name__ == "__main__":
    unittest.main()
