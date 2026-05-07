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
  <strong>轻量级正则表达式测试、调试与可视化CLI工具</strong>
</p>

<p align="center">
  零外部依赖 | 30+内置模式 | 12+语言代码生成 | 性能分析
</p>

---

## 🎉 项目介绍

**RegexForge** 是一款功能强大的正则表达式命令行工具，专为开发者设计。它提供了完整的正则表达式测试、调试、分析和代码生成功能，帮助开发者快速编写和优化正则表达式。

### ✨ 核心价值

- 🚀 **零依赖**：纯Python标准库实现，无需安装任何第三方包
- 📚 **内置模式库**：30+常用正则模式，覆盖邮箱、URL、IP、日期等常见场景
- 💻 **多语言代码生成**：支持Python、JavaScript、Java、Go、Rust等12+编程语言
- 📊 **性能分析**：实时测试正则表达式性能，优化匹配效率
- 🎨 **彩色输出**：终端彩色高亮显示匹配结果
- 📤 **多格式导出**：支持JSON、HTML格式输出

### 🌟 自研差异化亮点

| 特性 | RegexForge | 其他工具 |
|------|------------|----------|
| 外部依赖 | ✅ 零依赖 | ❌ 需要安装多个包 |
| 代码生成 | ✅ 12+语言 | ⚠️ 通常仅3-5种 |
| 内置模式 | ✅ 30+模式 | ⚠️ 通常无或很少 |
| 性能测试 | ✅ 内置 | ❌ 需要额外工具 |
| 复杂度分析 | ✅ 智能评分 | ❌ 无 |

---

## ✨ 核心特性

### 🔍 正则表达式测试
- 实时匹配测试，支持所有标准正则标志（i/m/s/x/a）
- 显示匹配位置、分组和命名分组
- 彩色高亮显示匹配结果

### 📚 内置模式库
- **基础模式**：邮箱、URL、域名
- **网络模式**：IPv4、IPv6、MAC地址
- **日期时间**：ISO日期、US日期、24小时时间
- **身份验证**：用户名、密码强度、UUID
- **金融模式**：信用卡号、SSN
- **国际化**：中文字符、Emoji

### 💻 代码生成
支持生成以下语言的完整代码：

| 语言 | 支持状态 |
|------|----------|
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

### 📊 模式分析
- 复杂度评分（0-100）
- 智能优化建议
- 分组统计

### ⚡ 性能测试
- 可配置迭代次数
- 总耗时、平均耗时统计
- 每秒匹配次数

---

## 🚀 快速开始

### 环境要求
- Python 3.7 或更高版本
- 无需安装任何外部依赖

### 安装方式

**方式一：直接运行**
```bash
# 克隆仓库
git clone https://github.com/gitstq/RegexForge.git
cd RegexForge

# 直接运行
python regexforge.py -p "\d+" -t "Hello 123 World"
```

**方式二：pip安装**
```bash
# 从源码安装
pip install .

# 或使用 pip install -e . 进行开发模式安装
```

### 基本用法

```bash
# 测试正则表达式
regexforge -p "\d+" -t "Hello 123 World 456"

# 使用内置模式库
regexforge -p "email" -t "test@example.com" --library

# 列出所有内置模式
regexforge --list-patterns

# 生成Python代码
regexforge -p "\d+" --generate python

# 分析模式复杂度
regexforge -p "(\w+)@(\w+)\.(\w+)" --analyze

# 性能测试
regexforge -p "\d+" -t "test 123" --performance

# JSON格式输出
regexforge -p "\d+" -t "test 123" -o json

# 输出到文件
regexforge -p "\d+" -t "test 123" -o html --output-file result.html
```

---

## 📖 详细使用指南

### 命令行参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `-p, --pattern` | 正则表达式模式 | `-p "\d+"` |
| `-t, --text` | 待匹配文本 | `-t "Hello 123"` |
| `-f, --flags` | 正则标志 | `-f "im"` |
| `-o, --output` | 输出格式 | `-o json` |
| `--library` | 使用内置模式 | `--library` |
| `--list-patterns` | 列出所有模式 | `--list-patterns` |
| `--generate` | 生成代码 | `--generate python` |
| `--analyze` | 分析模式 | `--analyze` |
| `--performance` | 性能测试 | `--performance` |

### 正则标志

| 标志 | 说明 |
|------|------|
| `i` | 忽略大小写 |
| `m` | 多行模式 |
| `s` | 点号匹配换行 |
| `x` | 详细模式 |
| `a` | ASCII模式 |

### 使用示例

**1. 测试邮箱匹配**
```bash
regexforge -p "email" -t "Contact: test@example.com, sales@company.org" --library
```

**2. 提取URL**
```bash
regexforge -p "url" -t "Visit https://example.com or www.test.org" --library
```

**3. 生成JavaScript代码**
```bash
regexforge -p "(\w+)@(\w+)\.(\w+)" --generate javascript
```

**4. 分析复杂模式**
```bash
regexforge -p "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$" --analyze
```

**5. 性能测试**
```bash
regexforge -p "\d+" -t "test 123 456 789" --performance --iterations 10000
```

---

## 💡 设计思路与迭代规划

### 设计理念

RegexForge 的设计遵循以下原则：

1. **零依赖优先**：使用Python标准库实现所有功能，确保安装简单、兼容性好
2. **开发者友好**：提供清晰的命令行界面和彩色输出
3. **功能完整**：覆盖正则表达式开发的全流程需求
4. **可扩展性**：模块化设计，便于添加新模式和语言支持

### 技术选型

- **语言**：Python 3.7+（广泛兼容）
- **CLI框架**：argparse（标准库）
- **正则引擎**：re模块（标准库）
- **输出格式**：JSON/HTML（标准库）

### 后续迭代计划

- [ ] 添加更多内置模式（银行卡号、车牌号等）
- [ ] 支持正则表达式可视化
- [ ] 添加交互式REPL模式
- [ ] 支持批量文件处理
- [ ] 添加正则表达式调试器
- [ ] 支持自定义模式库

---

## 📦 打包与部署指南

### 打包发布

```bash
# 构建分发包
python -m build

# 上传到PyPI
twine upload dist/*
```

### 本地安装

```bash
# 从源码安装
pip install .

# 开发模式安装
pip install -e .
```

### 兼容环境

- ✅ Linux (Ubuntu, CentOS, Debian等)
- ✅ macOS (10.14+)
- ✅ Windows (10/11)
- ✅ Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: 添加某个功能'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 代码规范

- 遵循 PEP 8 编码规范
- 为新功能添加单元测试
- 更新相关文档

### 问题反馈

如果您发现Bug或有功能建议，请在 [Issues](https://github.com/gitstq/RegexForge/issues) 页面提交。

---

## 📄 开源协议说明

本项目采用 [MIT License](LICENSE) 开源协议。

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
