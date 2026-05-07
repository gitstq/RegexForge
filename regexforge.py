#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RegexForge - Lightweight Regular Expression Testing, Debugging & Visualization CLI Tool
A powerful regex toolkit with pattern library, code generation, and performance analysis.

Author: gitstq
License: MIT
Version: 1.0.0
"""

import re
import sys
import json
import time
import argparse
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass
from enum import Enum
import html


class OutputFormat(Enum):
    """Output format options"""
    TEXT = "text"
    JSON = "json"
    HTML = "html"


@dataclass
class MatchResult:
    """Represents a regex match result"""
    match_text: str
    start: int
    end: int
    groups: Tuple[str, ...]
    named_groups: Dict[str, str]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "match": self.match_text,
            "start": self.start,
            "end": self.end,
            "groups": list(self.groups),
            "named_groups": self.named_groups
        }


@dataclass
class RegexAnalysis:
    """Regex pattern analysis result"""
    pattern: str
    flags: str
    is_valid: bool
    error: Optional[str]
    groups_count: int
    named_groups: List[str]
    complexity_score: int
    suggestions: List[str]


class PatternLibrary:
    """Built-in regex pattern library with 30+ common patterns"""
    
    PATTERNS = {
        # Basic patterns
        "email": {
            "pattern": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "description": "Email address",
            "category": "basic"
        },
        "url": {
            "pattern": r"https?://[^\s<>\"']+|www\.[^\s<>\"']+",
            "description": "URL (HTTP/HTTPS)",
            "category": "basic"
        },
        "ipv4": {
            "pattern": r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",
            "description": "IPv4 address",
            "category": "network"
        },
        "ipv6": {
            "pattern": r"(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}",
            "description": "IPv6 address",
            "category": "network"
        },
        "mac_address": {
            "pattern": r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})",
            "description": "MAC address",
            "category": "network"
        },
        "phone_us": {
            "pattern": r"\+?1?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
            "description": "US phone number",
            "category": "phone"
        },
        "phone_cn": {
            "pattern": r"(?:\+?86)?1[3-9]\d{9}",
            "description": "Chinese mobile phone number",
            "category": "phone"
        },
        "date_iso": {
            "pattern": r"\d{4}-\d{2}-\d{2}",
            "description": "ISO date (YYYY-MM-DD)",
            "category": "datetime"
        },
        "date_us": {
            "pattern": r"\b(0?[1-9]|1[0-2])[-/](0?[1-9]|[12]\d|3[01])[-/]\d{4}\b",
            "description": "US date (MM/DD/YYYY)",
            "category": "datetime"
        },
        "time_24h": {
            "pattern": r"([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?",
            "description": "24-hour time format",
            "category": "datetime"
        },
        "credit_card": {
            "pattern": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
            "description": "Credit card number",
            "category": "finance"
        },
        "ssn_us": {
            "pattern": r"\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b",
            "description": "US Social Security Number",
            "category": "identity"
        },
        "hex_color": {
            "pattern": r"#(?:[0-9a-fA-F]{3}){1,2}\b",
            "description": "Hex color code",
            "category": "design"
        },
        "rgb_color": {
            "pattern": r"rgb\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)",
            "description": "RGB color",
            "category": "design"
        },
        "username": {
            "pattern": r"^[a-zA-Z][a-zA-Z0-9_]{2,15}$",
            "description": "Username (3-16 chars, starts with letter)",
            "category": "validation"
        },
        "password_strong": {
            "pattern": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
            "description": "Strong password (8+ chars, mixed case, digit, special)",
            "category": "validation"
        },
        "slug": {
            "pattern": r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
            "description": "URL slug",
            "category": "web"
        },
        "domain": {
            "pattern": r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}",
            "description": "Domain name",
            "category": "web"
        },
        "html_tag": {
            "pattern": r"<([a-zA-Z][a-zA-Z0-9]*)[^>]*>.*?</\1>|<[a-zA-Z][a-zA-Z0-9]*[^>]*/>",
            "description": "HTML tag",
            "category": "web"
        },
        "json_string": {
            "pattern": r'"(?:[^"\\]|\\.)*"',
            "description": "JSON string",
            "category": "data"
        },
        "number_int": {
            "pattern": r"-?\d+",
            "description": "Integer number",
            "category": "data"
        },
        "number_float": {
            "pattern": r"-?\d+\.\d+",
            "description": "Floating point number",
            "category": "data"
        },
        "uuid": {
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            "description": "UUID",
            "category": "identity"
        },
        "base64": {
            "pattern": r"(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?",
            "description": "Base64 encoded string",
            "category": "encoding"
        },
        "markdown_header": {
            "pattern": r"^#{1,6}\s+.+$",
            "description": "Markdown header",
            "category": "markup"
        },
        "markdown_link": {
            "pattern": r"\[([^\]]+)\]\(([^)]+)\)",
            "description": "Markdown link",
            "category": "markup"
        },
        "youtube_id": {
            "pattern": r"(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^\"&?\/\s]{11})",
            "description": "YouTube video ID",
            "category": "media"
        },
        "twitter_handle": {
            "pattern": r"@[a-zA-Z0-9_]{1,15}",
            "description": "Twitter handle",
            "category": "social"
        },
        "hashtag": {
            "pattern": r"#[a-zA-Z0-9_]+",
            "description": "Hashtag",
            "category": "social"
        },
        "whitespace": {
            "pattern": r"\s+",
            "description": "Whitespace characters",
            "category": "utility"
        },
        "chinese": {
            "pattern": r"[\u4e00-\u9fff]+",
            "description": "Chinese characters",
            "category": "i18n"
        },
        "emoji": {
            "pattern": r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002702-\U000027B0]",
            "description": "Emoji characters",
            "category": "i18n"
        }
    }
    
    @classmethod
    def list_patterns(cls, category: Optional[str] = None) -> List[Dict[str, str]]:
        """List all patterns or filter by category"""
        patterns = []
        for name, info in cls.PATTERNS.items():
            if category is None or info["category"] == category:
                patterns.append({
                    "name": name,
                    "pattern": info["pattern"],
                    "description": info["description"],
                    "category": info["category"]
                })
        return patterns
    
    @classmethod
    def get_categories(cls) -> List[str]:
        """Get all pattern categories"""
        return list(set(info["category"] for info in cls.PATTERNS.values()))
    
    @classmethod
    def get_pattern(cls, name: str) -> Optional[str]:
        """Get a pattern by name"""
        if name in cls.PATTERNS:
            return cls.PATTERNS[name]["pattern"]
        return None


class CodeGenerator:
    """Generate regex code for multiple programming languages"""
    
    @staticmethod
    def generate_python(pattern: str, flags: str = "") -> str:
        """Generate Python regex code"""
        flag_code = ""
        if "i" in flags:
            flag_code += "re.IGNORECASE | "
        if "m" in flags:
            flag_code += "re.MULTILINE | "
        if "s" in flags:
            flag_code += "re.DOTALL | "
        if "x" in flags:
            flag_code += "re.VERBOSE | "
        flag_code = flag_code.rstrip(" | ") if flag_code else "0"
        
        return f'''import re

pattern = r"{pattern}"
flags = {flag_code}
regex = re.compile(pattern, flags)

# Find all matches
matches = regex.findall(text)

# Find with positions
for match in regex.finditer(text):
    print(f"Match: {{match.group()}} at {{match.start()}}-{{match.end()}}")
'''
    
    @staticmethod
    def generate_javascript(pattern: str, flags: str = "") -> str:
        """Generate JavaScript regex code"""
        js_flags = flags.replace("s", "")
        return f'''// JavaScript Regex
const pattern = /{pattern}/{js_flags};

// Test match
const isMatch = pattern.test(text);

// Find all matches
const matches = text.match(pattern);

// Find with positions
const matchesWithPos = [...text.matchAll(pattern)];
matchesWithPos.forEach(match => {{
    console.log(`Match: ${{match[0]}} at ${{match.index}}`);
}});
'''
    
    @staticmethod
    def generate_java(pattern: str, flags: str = "") -> str:
        """Generate Java regex code"""
        java_flags = []
        if "i" in flags:
            java_flags.append("Pattern.CASE_INSENSITIVE")
        if "m" in flags:
            java_flags.append("Pattern.MULTILINE")
        if "s" in flags:
            java_flags.append("Pattern.DOTALL")
        
        flags_code = " | ".join(java_flags) if java_flags else "0"
        
        return f'''import java.util.regex.*;

String patternStr = "{pattern}";
Pattern pattern = Pattern.compile(patternStr, {flags_code});
Matcher matcher = pattern.matcher(text);

while (matcher.find()) {{
    System.out.println("Match: " + matcher.group() + " at " + matcher.start() + "-" + matcher.end());
}}
'''
    
    @staticmethod
    def generate_go(pattern: str, flags: str = "") -> str:
        """Generate Go regex code"""
        go_flags = ""
        if "i" in flags:
            go_flags += "(?i)"
        if "m" in flags:
            go_flags += "(?m)"
        if "s" in flags:
            go_flags += "(?s)"
        
        full_pattern = go_flags + pattern
        
        return f'''package main

import (
    "fmt"
    "regexp"
)

func main() {{
    pattern := regexp.MustCompile(`{full_pattern}`)
    
    matches := pattern.FindAllString(text, -1)
    for _, match := range matches {{
        fmt.Println("Match:", match)
    }}
    
    // Find with positions
    locs := pattern.FindAllStringIndex(text, -1)
    for i, loc := range locs {{
        fmt.Printf("Match %d: %s at %d-%d\\n", i, text[loc[0]:loc[1]], loc[0], loc[1])
    }}
}}
'''
    
    @staticmethod
    def generate_rust(pattern: str, flags: str = "") -> str:
        """Generate Rust regex code"""
        rust_flags = ""
        if "i" in flags:
            rust_flags += "(?i)"
        if "m" in flags:
            rust_flags += "(?m)"
        if "s" in flags:
            rust_flags += "(?s)"
        
        full_pattern = rust_flags + pattern
        
        return f'''use regex::Regex;

fn main() {{
    let pattern = Regex::new(r"{full_pattern}").unwrap();
    
    for cap in pattern.captures_iter(text) {{
        println!("Match: {{:?}}", &cap[0]);
    }}
}}
'''
    
    @staticmethod
    def generate_php(pattern: str, flags: str = "") -> str:
        """Generate PHP regex code"""
        php_flags = flags.replace("s", "")
        
        return f'''<?php
$pattern = '/{pattern}/{php_flags}';

preg_match_all($pattern, $text, $matches, PREG_SET_ORDER | PREG_OFFSET_CAPTURE);

foreach ($matches as $match) {{
    echo "Match: " . $match[0][0] . " at " . $match[0][1] . "\\n";
}}
?>
'''
    
    @staticmethod
    def generate_ruby(pattern: str, flags: str = "") -> str:
        """Generate Ruby regex code"""
        ruby_flags = ""
        if "i" in flags:
            ruby_flags += "i"
        if "m" in flags:
            ruby_flags += "m"
        if "s" in flags:
            ruby_flags += "m"  # Ruby uses m for DOTALL
        
        return '''# Ruby Regex
pattern = /''' + pattern + '''/''' + ruby_flags + '''

text.scan(pattern) do |match|
  puts "Match: #{match}"
end

# With positions
text.gsub(pattern) do |match|
  puts "Match: #{match} at #{$~.begin(0)}-#{$~.end(0)}"
  match
end
'''
    
    @staticmethod
    def generate_csharp(pattern: str, flags: str = "") -> str:
        """Generate C# regex code"""
        csharp_flags = []
        if "i" in flags:
            csharp_flags.append("RegexOptions.IgnoreCase")
        if "m" in flags:
            csharp_flags.append("RegexOptions.Multiline")
        if "s" in flags:
            csharp_flags.append("RegexOptions.Singleline")
        
        flags_code = " | ".join(csharp_flags) if csharp_flags else "RegexOptions.None"
        
        return f'''using System.Text.RegularExpressions;

string pattern = @"{pattern}";
Regex regex = new Regex(pattern, {flags_code});

MatchCollection matches = regex.Matches(text);
foreach (Match match in matches) {{
    Console.WriteLine($"Match: {{match.Value}} at {{match.Index}}-{{match.Index + match.Length}}");
}}
'''
    
    @staticmethod
    def generate_perl(pattern: str, flags: str = "") -> str:
        """Generate Perl regex code"""
        perl_flags = ""
        if "i" in flags:
            perl_flags += "i"
        if "m" in flags:
            perl_flags += "m"
        if "s" in flags:
            perl_flags += "s"
        
        return f'''# Perl Regex
my $pattern = qr/{pattern}/{perl_flags};

while ($text =~ /$pattern/g) {{
    print "Match: $& at " . pos($text) - length($&) . "-" . pos($text) . "\\n";
}}
'''
    
    @staticmethod
    def generate_swift(pattern: str, flags: str = "") -> str:
        """Generate Swift regex code"""
        swift_flags = []
        if "i" in flags:
            swift_flags.append(".caseInsensitive")
        if "m" in flags:
            swift_flags.append(".anchorsMatchLines")
        
        flags_code = ", options: [" + ", ".join(swift_flags) + "]" if swift_flags else ""
        
        return f'''import Foundation

let pattern = #"{pattern}"#
let regex = try! NSRegularExpression(pattern: pattern{flags_code})

let matches = regex.matches(in: text, range: NSRange(text.startIndex..., in: text))
for match in matches {{
    if let range = Range(match.range, in: text) {{
        print("Match: \\(text[range])")
    }}
}}
'''
    
    @staticmethod
    def generate_kotlin(pattern: str, flags: str = "") -> str:
        """Generate Kotlin regex code"""
        kotlin_flags = ""
        if "i" in flags:
            kotlin_flags += "RegexOption.IGNORE_CASE"
        if "m" in flags:
            kotlin_flags += "RegexOption.MULTILINE"
        
        options_code = f", setOf({kotlin_flags})" if kotlin_flags else ""
        
        return f'''val pattern = Regex("""{pattern}"""{options_code})

pattern.findAll(text).forEach {{ match ->
    println("Match: ${{match.value}} at ${{match.range}}")
}}
'''
    
    @staticmethod
    def generate_typescript(pattern: str, flags: str = "") -> str:
        """Generate TypeScript regex code"""
        ts_flags = flags.replace("s", "")
        return f'''// TypeScript Regex
const pattern: RegExp = /{pattern}/{ts_flags};

// Test match
const isMatch: boolean = pattern.test(text);

// Find all matches
const matches: RegExpMatchArray | null = text.match(pattern);

// Find with positions
const matchesWithPos: IterableIterator<RegExpMatchArray> = text.matchAll(pattern);
for (const match of matchesWithPos) {{
    console.log(`Match: ${{match[0]}} at ${{match.index}}`);
}}
'''
    
    @staticmethod
    def generate_scala(pattern: str, flags: str = "") -> str:
        """Generate Scala regex code"""
        scala_flags = ""
        if "i" in flags:
            scala_flags += "(?i)"
        if "m" in flags:
            scala_flags += "(?m)"
        if "s" in flags:
            scala_flags += "(?s)"
        
        full_pattern = scala_flags + pattern
        
        return f'''import scala.util.matching.Regex

val pattern: Regex = s"$full_pattern".r

pattern.findAllIn(text).matchData.foreach {{ m =>
    println(s"Match: ${{m.matched}} at ${{m.start}}-${{m.end}}")
}}
'''
    
    LANGUAGES = {
        "python": generate_python,
        "javascript": generate_javascript,
        "js": generate_javascript,
        "java": generate_java,
        "go": generate_go,
        "rust": generate_rust,
        "php": generate_php,
        "ruby": generate_ruby,
        "csharp": generate_csharp,
        "c#": generate_csharp,
        "perl": generate_perl,
        "swift": generate_swift,
        "kotlin": generate_kotlin,
        "typescript": generate_typescript,
        "ts": generate_typescript,
        "scala": generate_scala
    }
    
    @classmethod
    def generate(cls, language: str, pattern: str, flags: str = "") -> Optional[str]:
        """Generate code for specified language"""
        lang_lower = language.lower()
        if lang_lower in cls.LANGUAGES:
            return cls.LANGUAGES[lang_lower].__func__(pattern, flags)
        return None


class RegexAnalyzer:
    """Analyze regex patterns for complexity and provide suggestions"""
    
    @staticmethod
    def analyze(pattern: str, flags: str = "") -> RegexAnalysis:
        """Analyze a regex pattern"""
        is_valid = True
        error = None
        groups_count = 0
        named_groups = []
        suggestions = []
        complexity_score = 0
        
        # Try to compile the pattern
        try:
            re_flags = 0
            if "i" in flags:
                re_flags |= re.IGNORECASE
            if "m" in flags:
                re_flags |= re.MULTILINE
            if "s" in flags:
                re_flags |= re.DOTALL
            if "x" in flags:
                re_flags |= re.VERBOSE
            
            compiled = re.compile(pattern, re_flags)
            groups_count = compiled.groups
            named_groups = list(compiled.groupindex.keys())
            
        except re.error as e:
            is_valid = False
            error = str(e)
            return RegexAnalysis(
                pattern=pattern,
                flags=flags,
                is_valid=is_valid,
                error=error,
                groups_count=groups_count,
                named_groups=named_groups,
                complexity_score=0,
                suggestions=["Fix syntax error before analysis"]
            )
        
        # Calculate complexity score
        complexity_score = RegexAnalyzer._calculate_complexity(pattern)
        
        # Generate suggestions
        suggestions = RegexAnalyzer._generate_suggestions(pattern, complexity_score)
        
        return RegexAnalysis(
            pattern=pattern,
            flags=flags,
            is_valid=is_valid,
            error=error,
            groups_count=groups_count,
            named_groups=named_groups,
            complexity_score=complexity_score,
            suggestions=suggestions
        )
    
    @staticmethod
    def _calculate_complexity(pattern: str) -> int:
        """Calculate complexity score (0-100)"""
        score = 0
        
        # Length factor
        score += min(len(pattern) // 2, 20)
        
        # Quantifiers
        score += pattern.count("*") * 2
        score += pattern.count("+") * 2
        score += pattern.count("?") * 2
        score += pattern.count("{") * 3
        
        # Groups
        score += pattern.count("(") * 3
        score += pattern.count("(?:") * 2
        score += pattern.count("(?=") * 4
        score += pattern.count("(?!") * 4
        score += pattern.count("(?<=") * 4
        score += pattern.count("(?<!") * 4
        
        # Character classes
        score += pattern.count("[") * 2
        
        # Alternation
        score += pattern.count("|") * 3
        
        # Escape sequences
        score += pattern.count("\\") * 1
        
        # Backreferences
        score += len(re.findall(r'\\[1-9]', pattern)) * 5
        
        return min(score, 100)
    
    @staticmethod
    def _generate_suggestions(pattern: str, complexity: int) -> List[str]:
        """Generate optimization suggestions"""
        suggestions = []
        
        if complexity > 70:
            suggestions.append("⚠️ High complexity! Consider breaking into simpler patterns")
        
        if ".*.*" in pattern or ".+.+" in pattern:
            suggestions.append("💡 Multiple greedy quantifiers may cause backtracking issues")
        
        if re.search(r'\[[^\]]*\.\.[^\]]*\]', pattern):
            suggestions.append("💡 Character range detected - ensure proper escaping")
        
        if pattern.count("(") > 5:
            suggestions.append("💡 Many groups - consider using non-capturing groups (?:) if not needed")
        
        if re.search(r'\^\.\*\$', pattern):
            suggestions.append("💡 Pattern matches everything - verify this is intended")
        
        if re.search(r'\(\.\*\)', pattern):
            suggestions.append("💡 Greedy .* inside group may cause performance issues")
        
        if re.search(r'\\d\+', pattern) and not re.search(r'\\d\{', pattern):
            suggestions.append("💡 Consider using {n} quantifier for exact digit counts")
        
        if not suggestions:
            suggestions.append("✅ Pattern looks good!")
        
        return suggestions


class RegexForge:
    """Main RegexForge class"""
    
    def __init__(self):
        self.colors = {
            "reset": "\033[0m",
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
            "bold": "\033[1m",
            "underline": "\033[4m"
        }
    
    def colorize(self, text: str, color: str) -> str:
        """Apply color to text"""
        if sys.stdout.isatty():
            return f"{self.colors.get(color, '')}{text}{self.colors['reset']}"
        return text
    
    def parse_flags(self, flag_str: str) -> int:
        """Parse flag string to re flags"""
        flags = 0
        if "i" in flag_str:
            flags |= re.IGNORECASE
        if "m" in flag_str:
            flags |= re.MULTILINE
        if "s" in flag_str:
            flags |= re.DOTALL
        if "x" in flag_str:
            flags |= re.VERBOSE
        if "a" in flag_str:
            flags |= re.ASCII
        return flags
    
    def test_pattern(self, pattern: str, text: str, flags: str = "") -> Tuple[List[MatchResult], Optional[str]]:
        """Test a regex pattern against text"""
        try:
            re_flags = self.parse_flags(flags)
            compiled = re.compile(pattern, re_flags)
            
            results = []
            for match in compiled.finditer(text):
                named_groups = {k: v for k, v in match.groupdict().items() if v is not None}
                results.append(MatchResult(
                    match_text=match.group(0),
                    start=match.start(),
                    end=match.end(),
                    groups=match.groups(),
                    named_groups=named_groups
                ))
            
            return results, None
        except re.error as e:
            return [], str(e)
    
    def performance_test(self, pattern: str, text: str, flags: str = "", iterations: int = 1000) -> Dict[str, Any]:
        """Run performance test on pattern"""
        try:
            re_flags = self.parse_flags(flags)
            compiled = re.compile(pattern, re_flags)
            
            # Warm up
            for _ in range(10):
                compiled.findall(text)
            
            # Measure
            start_time = time.perf_counter()
            for _ in range(iterations):
                compiled.findall(text)
            end_time = time.perf_counter()
            
            total_time = end_time - start_time
            avg_time = total_time / iterations
            
            return {
                "iterations": iterations,
                "total_time_ms": round(total_time * 1000, 3),
                "avg_time_us": round(avg_time * 1000000, 3),
                "matches_per_sec": round(iterations / total_time) if total_time > 0 else 0
            }
        except re.error as e:
            return {"error": str(e)}
    
    def format_output_text(self, results: List[MatchResult], pattern: str, text: str) -> str:
        """Format results as colored text"""
        output = []
        output.append(self.colorize("\n" + "=" * 60, "cyan"))
        output.append(self.colorize("  RegexForge - Match Results", "bold"))
        output.append(self.colorize("=" * 60, "cyan"))
        output.append(f"\n{self.colorize('Pattern:', 'yellow')} {pattern}")
        output.append(f"{self.colorize('Text length:', 'yellow')} {len(text)} chars")
        output.append(f"{self.colorize('Matches found:', 'yellow')} {len(results)}")
        
        if results:
            output.append(self.colorize("\n" + "-" * 60, "cyan"))
            output.append(self.colorize("  Match Details", "bold"))
            output.append(self.colorize("-" * 60, "cyan"))
            
            for i, result in enumerate(results, 1):
                output.append(f"\n{self.colorize(f'[{i}]', 'green')} {self.colorize(result.match_text, 'magenta')}")
                output.append(f"    {self.colorize('Position:', 'yellow')} {result.start}-{result.end}")
                
                if result.groups:
                    output.append(f"    {self.colorize('Groups:', 'yellow')} {list(result.groups)}")
                
                if result.named_groups:
                    output.append(f"    {self.colorize('Named Groups:', 'yellow')}")
                    for name, value in result.named_groups.items():
                        output.append(f"      {name}: {value}")
        
        # Highlighted text
        if results:
            output.append(self.colorize("\n" + "-" * 60, "cyan"))
            output.append(self.colorize("  Highlighted Text", "bold"))
            output.append(self.colorize("-" * 60, "cyan") + "\n")
            
            highlighted = text
            offset = 0
            for result in results:
                start = result.start + offset
                end = result.end + offset
                highlighted = highlighted[:start] + self.colorize(highlighted[start:end], "green") + highlighted[end:]
                offset += len(self.colors["green"]) + len(self.colors["reset"])
            
            output.append(highlighted)
        
        return "\n".join(output)
    
    def format_output_json(self, results: List[MatchResult], pattern: str, text: str, analysis: Optional[RegexAnalysis] = None, performance: Optional[Dict] = None) -> str:
        """Format results as JSON"""
        output = {
            "pattern": pattern,
            "text_length": len(text),
            "match_count": len(results),
            "matches": [r.to_dict() for r in results]
        }
        
        if analysis:
            output["analysis"] = {
                "is_valid": analysis.is_valid,
                "error": analysis.error,
                "groups_count": analysis.groups_count,
                "named_groups": analysis.named_groups,
                "complexity_score": analysis.complexity_score,
                "suggestions": analysis.suggestions
            }
        
        if performance:
            output["performance"] = performance
        
        return json.dumps(output, indent=2, ensure_ascii=False)
    
    def format_output_html(self, results: List[MatchResult], pattern: str, text: str) -> str:
        """Format results as HTML"""
        html_output = [
            '<!DOCTYPE html>',
            '<html lang="en">',
            '<head>',
            '    <meta charset="UTF-8">',
            '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
            '    <title>RegexForge Results</title>',
            '    <style>',
            '        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 40px; background: #1a1a2e; color: #eee; }',
            '        .container { max-width: 1200px; margin: 0 auto; }',
            '        h1 { color: #00d4ff; }',
            '        h2 { color: #ff6b6b; border-bottom: 2px solid #ff6b6b; padding-bottom: 10px; }',
            '        .pattern { background: #16213e; padding: 15px; border-radius: 8px; font-family: monospace; margin: 20px 0; }',
            '        .match { background: #0f3460; margin: 10px 0; padding: 15px; border-radius: 8px; border-left: 4px solid #00d4ff; }',
            '        .match-number { color: #00d4ff; font-weight: bold; }',
            '        .match-text { color: #ff6b6b; font-family: monospace; background: #1a1a2e; padding: 5px 10px; border-radius: 4px; }',
            '        .position { color: #ffd93d; }',
            '        .groups { color: #6bcb77; }',
            '        .highlighted { background: #0f3460; padding: 20px; border-radius: 8px; font-family: monospace; white-space: pre-wrap; line-height: 1.8; }',
            '        .highlight { background: #00d4ff; color: #1a1a2e; padding: 2px 4px; border-radius: 3px; }',
            '    </style>',
            '</head>',
            '<body>',
            '    <div class="container">',
            f'        <h1>🔍 RegexForge Results</h1>',
            f'        <div class="pattern"><strong>Pattern:</strong> {html.escape(pattern)}</div>',
            f'        <p><strong>Text length:</strong> {len(text)} characters</p>',
            f'        <p><strong>Matches found:</strong> {len(results)}</p>',
        ]
        
        if results:
            html_output.append('        <h2>Match Details</h2>')
            for i, result in enumerate(results, 1):
                html_output.append(f'        <div class="match">')
                html_output.append(f'            <span class="match-number">[{i}]</span> ')
                html_output.append(f'            <span class="match-text">{html.escape(result.match_text)}</span><br>')
                html_output.append(f'            <span class="position">Position: {result.start}-{result.end}</span>')
                if result.groups:
                    html_output.append(f'<br><span class="groups">Groups: {html.escape(str(list(result.groups)))}</span>')
                html_output.append('        </div>')
            
            # Highlighted text
            html_output.append('        <h2>Highlighted Text</h2>')
            highlighted = html.escape(text)
            for result in reversed(results):
                match_escaped = html.escape(result.match_text)
                highlighted = highlighted[:result.start] + f'<span class="highlight">{match_escaped}</span>' + highlighted[result.end:]
            html_output.append(f'        <div class="highlighted">{highlighted}</div>')
        
        html_output.extend([
            '    </div>',
            '</body>',
            '</html>'
        ])
        
        return '\n'.join(html_output)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="RegexForge - Lightweight Regular Expression Testing, Debugging & Visualization CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -p "\d+" -t "Hello 123 World 456"
  %(prog)s -p "email" -t "test@example.com" --library
  %(prog)s -p "\w+" -t "Hello World" -f json
  %(prog)s --list-patterns
  %(prog)s -p "\d+" --generate python
  %(prog)s -p "(\w+)@(\w+)" -t "test@example.com" --analyze
        """
    )
    
    parser.add_argument("-p", "--pattern", help="Regex pattern to test")
    parser.add_argument("-t", "--text", help="Text to match against")
    parser.add_argument("-f", "--flags", default="", help="Regex flags: i (case-insensitive), m (multiline), s (dotall), x (verbose)")
    parser.add_argument("-o", "--output", choices=["text", "json", "html"], default="text", help="Output format")
    parser.add_argument("--output-file", help="Write output to file")
    parser.add_argument("--library", action="store_true", help="Use pattern from library (pattern name instead of regex)")
    parser.add_argument("--list-patterns", action="store_true", help="List all patterns in library")
    parser.add_argument("--category", help="Filter patterns by category")
    parser.add_argument("--generate", metavar="LANG", help="Generate code for specified language")
    parser.add_argument("--analyze", action="store_true", help="Analyze pattern complexity")
    parser.add_argument("--performance", action="store_true", help="Run performance test")
    parser.add_argument("--iterations", type=int, default=1000, help="Performance test iterations")
    parser.add_argument("-v", "--version", action="version", version="RegexForge v1.0.0")
    
    args = parser.parse_args()
    
    forge = RegexForge()
    
    # List patterns
    if args.list_patterns:
        patterns = PatternLibrary.list_patterns(args.category)
        if not patterns:
            print(forge.colorize("No patterns found.", "red"))
            return
        
        print(forge.colorize("\n📚 Pattern Library", "bold"))
        print(forge.colorize("=" * 60, "cyan"))
        
        categories = {}
        for p in patterns:
            if p["category"] not in categories:
                categories[p["category"]] = []
            categories[p["category"]].append(p)
        
        for cat, pats in sorted(categories.items()):
            print(f"\n{forge.colorize(f'[{cat}]', 'yellow')}")
            for p in pats:
                print(f"  {forge.colorize(p['name'], 'green')}: {p['description']}")
                print(f"    {forge.colorize(p['pattern'], 'cyan')}")
        
        return
    
    # Validate required arguments
    if not args.pattern:
        parser.error("Pattern is required (-p/--pattern)")
    
    # Get pattern from library if specified
    pattern = args.pattern
    if args.library:
        lib_pattern = PatternLibrary.get_pattern(args.pattern)
        if lib_pattern:
            pattern = lib_pattern
            print(forge.colorize(f"\n📖 Using library pattern: {args.pattern}", "cyan"))
        else:
            print(forge.colorize(f"Pattern '{args.pattern}' not found in library.", "red"))
            return
    
    # Generate code
    if args.generate:
        code = CodeGenerator.generate(args.generate, pattern, args.flags)
        if code:
            print(forge.colorize(f"\n💻 Generated code for {args.generate}:", "bold"))
            print(forge.colorize("=" * 60, "cyan"))
            print(code)
        else:
            print(forge.colorize(f"Language '{args.generate}' not supported.", "red"))
            print(forge.colorize(f"Supported languages: {', '.join(sorted(CodeGenerator.LANGUAGES.keys()))}", "yellow"))
        return
    
    # Analyze pattern
    if args.analyze:
        analysis = RegexAnalyzer.analyze(pattern, args.flags)
        print(forge.colorize("\n📊 Pattern Analysis", "bold"))
        print(forge.colorize("=" * 60, "cyan"))
        print(f"{forge.colorize('Pattern:', 'yellow')} {pattern}")
        print(f"{forge.colorize('Valid:', 'yellow')} {forge.colorize('Yes', 'green') if analysis.is_valid else forge.colorize('No', 'red')}")
        
        if not analysis.is_valid:
            print(f"{forge.colorize('Error:', 'red')} {analysis.error}")
        else:
            print(f"{forge.colorize('Groups:', 'yellow')} {analysis.groups_count}")
            print(f"{forge.colorize('Named Groups:', 'yellow')} {analysis.named_groups if analysis.named_groups else 'None'}")
            print(f"{forge.colorize('Complexity Score:', 'yellow')} {analysis.complexity_score}/100")
            
            # Complexity bar
            bar_length = 20
            filled = int(analysis.complexity_score / 100 * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)
            color = "green" if analysis.complexity_score < 40 else ("yellow" if analysis.complexity_score < 70 else "red")
            print(f"  [{forge.colorize(bar, color)}]")
            
            print(f"\n{forge.colorize('Suggestions:', 'yellow')}")
            for suggestion in analysis.suggestions:
                print(f"  {suggestion}")
        
        if not args.text:
            return
    
    # Test pattern
    if args.text:
        results, error = forge.test_pattern(pattern, args.text, args.flags)
        
        if error:
            print(forge.colorize(f"\n❌ Regex Error: {error}", "red"))
            return
        
        # Performance test
        performance = None
        if args.performance:
            performance = forge.performance_test(pattern, args.text, args.flags, args.iterations)
        
        # Analysis for JSON output
        analysis = None
        if args.output == "json":
            analysis = RegexAnalyzer.analyze(pattern, args.flags)
        
        # Format output
        if args.output == "json":
            output = forge.format_output_json(results, pattern, args.text, analysis, performance)
        elif args.output == "html":
            output = forge.format_output_html(results, pattern, args.text)
        else:
            output = forge.format_output_text(results, pattern, args.text)
            if performance:
                output += f"\n\n{forge.colorize('⚡ Performance Test', 'bold')}"
                output += f"\n{forge.colorize('=' * 60, 'cyan')}"
                output += f"\n{forge.colorize('Iterations:', 'yellow')} {performance['iterations']}"
                output += f"\n{forge.colorize('Total time:', 'yellow')} {performance['total_time_ms']} ms"
                output += f"\n{forge.colorize('Avg time:', 'yellow')} {performance['avg_time_us']} µs"
                output += f"\n{forge.colorize('Matches/sec:', 'yellow')} {performance['matches_per_sec']}"
        
        # Write to file or print
        if args.output_file:
            with open(args.output_file, "w", encoding="utf-8") as f:
                f.write(output)
            print(forge.colorize(f"\n✅ Output written to {args.output_file}", "green"))
        else:
            print(output)
    else:
        print(forge.colorize("\n💡 Tip: Use -t/--text to test the pattern against text", "cyan"))


if __name__ == "__main__":
    main()
