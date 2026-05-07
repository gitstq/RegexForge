<p align="center">
  <a href="README.md">简体中文</a> | 
  <a href="README_EN.md">English</a> | 
  <a href="README_TW.md">繁體中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Zero%20Dependencies-✓-brightgreen.svg" alt="Zero Dependencies">
</p>

<h1 align="center">🔍 RegexForge</h1>

<p align="center">
  <strong>Lightweight Regular Expression Testing, Debugging & Visualization CLI Tool</strong>
</p>

<p align="center">
  Zero Dependencies | 30+ Built-in Patterns | 12+ Language Code Generation | Performance Analysis
</p>

---

## 🎉 Introduction

**RegexForge** is a powerful command-line tool for regular expressions, designed specifically for developers. It provides complete regex testing, debugging, analysis, and code generation capabilities to help developers quickly write and optimize regular expressions.

### ✨ Core Value

- 🚀 **Zero Dependencies**: Pure Python standard library implementation, no third-party packages required
- 📚 **Built-in Pattern Library**: 30+ common regex patterns covering email, URL, IP, date, and more
- 💻 **Multi-language Code Generation**: Supports Python, JavaScript, Java, Go, Rust, and 12+ programming languages
- 📊 **Performance Analysis**: Real-time regex performance testing to optimize matching efficiency
- 🎨 **Colorful Output**: Terminal color highlighting for match results
- 📤 **Multi-format Export**: Supports JSON and HTML output formats

### 🌟 Unique Features

| Feature | RegexForge | Other Tools |
|---------|------------|-------------|
| Dependencies | ✅ Zero | ❌ Multiple packages |
| Code Generation | ✅ 12+ languages | ⚠️ Usually 3-5 |
| Built-in Patterns | ✅ 30+ patterns | ⚠️ None or few |
| Performance Test | ✅ Built-in | ❌ Requires extra tools |
| Complexity Analysis | ✅ Smart scoring | ❌ None |

---

## ✨ Core Features

### 🔍 Regex Testing
- Real-time matching test with all standard regex flags (i/m/s/x/a)
- Display match positions, groups, and named groups
- Color-highlighted match results

### 📚 Built-in Pattern Library
- **Basic Patterns**: Email, URL, Domain
- **Network Patterns**: IPv4, IPv6, MAC Address
- **DateTime**: ISO Date, US Date, 24-hour Time
- **Validation**: Username, Password Strength, UUID
- **Finance**: Credit Card, SSN
- **Internationalization**: Chinese Characters, Emoji

### 💻 Code Generation
Generate complete code for the following languages:

| Language | Support |
|----------|---------|
| Python | ✅ |
| JavaScript/TypeScript | ✅ |
| Java/Kotlin | ✅ |
| Go | ✅ |
| Rust | ✅ |
| PHP | ✅ |
| Ruby | ✅ |
| C# | ✅ |
| Perl | ✅ |
| Swift | ✅ |
| Scala | ✅ |

### 📊 Pattern Analysis
- Complexity score (0-100)
- Smart optimization suggestions
- Group statistics

### ⚡ Performance Testing
- Configurable iterations
- Total time, average time statistics
- Matches per second

---

## 🚀 Quick Start

### Requirements
- Python 3.7 or higher
- No external dependencies required

### Installation

**Option 1: Direct Run**
```bash
# Clone repository
git clone https://github.com/gitstq/RegexForge.git
cd RegexForge

# Run directly
python regexforge.py -p "\d+" -t "Hello 123 World"
```

**Option 2: pip Install**
```bash
# Install from source
pip install .

# Or use pip install -e . for development mode
```

### Basic Usage

```bash
# Test regex pattern
regexforge -p "\d+" -t "Hello 123 World 456"

# Use built-in pattern library
regexforge -p "email" -t "test@example.com" --library

# List all built-in patterns
regexforge --list-patterns

# Generate Python code
regexforge -p "\d+" --generate python

# Analyze pattern complexity
regexforge -p "(\w+)@(\w+)\.(\w+)" --analyze

# Performance test
regexforge -p "\d+" -t "test 123" --performance

# JSON format output
regexforge -p "\d+" -t "test 123" -o json

# Output to file
regexforge -p "\d+" -t "test 123" -o html --output-file result.html
```

---

## 📖 Detailed Usage Guide

### Command Line Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `-p, --pattern` | Regex pattern | `-p "\d+"` |
| `-t, --text` | Text to match | `-t "Hello 123"` |
| `-f, --flags` | Regex flags | `-f "im"` |
| `-o, --output` | Output format | `-o json` |
| `--library` | Use built-in pattern | `--library` |
| `--list-patterns` | List all patterns | `--list-patterns` |
| `--generate` | Generate code | `--generate python` |
| `--analyze` | Analyze pattern | `--analyze` |
| `--performance` | Performance test | `--performance` |

### Regex Flags

| Flag | Description |
|------|-------------|
| `i` | Case insensitive |
| `m` | Multiline mode |
| `s` | Dot matches newline |
| `x` | Verbose mode |
| `a` | ASCII mode |

### Usage Examples

**1. Test Email Matching**
```bash
regexforge -p "email" -t "Contact: test@example.com, sales@company.org" --library
```

**2. Extract URLs**
```bash
regexforge -p "url" -t "Visit https://example.com or www.test.org" --library
```

**3. Generate JavaScript Code**
```bash
regexforge -p "(\w+)@(\w+)\.(\w+)" --generate javascript
```

**4. Analyze Complex Pattern**
```bash
regexforge -p "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$" --analyze
```

**5. Performance Test**
```bash
regexforge -p "\d+" -t "test 123 456 789" --performance --iterations 10000
```

---

## 💡 Design Philosophy & Roadmap

### Design Principles

RegexForge is designed with the following principles:

1. **Zero Dependencies First**: All features implemented using Python standard library
2. **Developer Friendly**: Clear CLI interface with colorful output
3. **Feature Complete**: Covering the full workflow of regex development
4. **Extensibility**: Modular design for easy addition of new patterns and languages

### Technology Stack

- **Language**: Python 3.7+ (wide compatibility)
- **CLI Framework**: argparse (standard library)
- **Regex Engine**: re module (standard library)
- **Output Formats**: JSON/HTML (standard library)

### Future Roadmap

- [ ] Add more built-in patterns (bank card, license plate, etc.)
- [ ] Support regex visualization
- [ ] Add interactive REPL mode
- [ ] Support batch file processing
- [ ] Add regex debugger
- [ ] Support custom pattern libraries

---

## 📦 Packaging & Deployment

### Build Distribution

```bash
# Build distribution packages
python -m build

# Upload to PyPI
twine upload dist/*
```

### Local Installation

```bash
# Install from source
pip install .

# Development mode installation
pip install -e .
```

### Compatible Environments

- ✅ Linux (Ubuntu, CentOS, Debian, etc.)
- ✅ macOS (10.14+)
- ✅ Windows (10/11)
- ✅ Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12

---

## 🤝 Contributing

We welcome all forms of contributions!

### How to Contribute

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add some feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

### Code Standards

- Follow PEP 8 coding conventions
- Add unit tests for new features
- Update relevant documentation

### Issue Reporting

If you find a bug or have a feature suggestion, please submit it on the [Issues](https://github.com/gitstq/RegexForge/issues) page.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```
MIT License

Copyright (c) 2026 gitstq

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a>
</p>
