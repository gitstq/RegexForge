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
  <strong>輕量級正則表達式測試、除錯與視覺化CLI工具</strong>
</p>

<p align="center">
  零外部依賴 | 30+內建模式 | 12+語言程式碼生成 | 效能分析
</p>

---

## 🎉 專案介紹

**RegexForge** 是一款功能強大的正則表達式命令列工具，專為開發者設計。它提供了完整的正則表達式測試、除錯、分析和程式碼生成功能，幫助開發者快速編寫和優化正則表達式。

### ✨ 核心價值

- 🚀 **零依賴**：純Python標準庫實現，無需安裝任何第三方套件
- 📚 **內建模式庫**：30+常用正則模式，涵蓋郵箱、URL、IP、日期等常見場景
- 💻 **多語言程式碼生成**：支援Python、JavaScript、Java、Go、Rust等12+程式語言
- 📊 **效能分析**：即時測試正則表達式效能，優化匹配效率
- 🎨 **彩色輸出**：終端彩色高亮顯示匹配結果
- 📤 **多格式匯出**：支援JSON、HTML格式輸出

### 🌟 自研差異化亮點

| 特性 | RegexForge | 其他工具 |
|------|------------|----------|
| 外部依賴 | ✅ 零依賴 | ❌ 需要安裝多個套件 |
| 程式碼生成 | ✅ 12+語言 | ⚠️ 通常僅3-5種 |
| 內建模式 | ✅ 30+模式 | ⚠️ 通常無或很少 |
| 效能測試 | ✅ 內建 | ❌ 需要額外工具 |
| 複雜度分析 | ✅ 智慧評分 | ❌ 無 |

---

## ✨ 核心特性

### 🔍 正則表達式測試
- 即時匹配測試，支援所有標準正則標誌（i/m/s/x/a）
- 顯示匹配位置、分組和命名分組
- 彩色高亮顯示匹配結果

### 📚 內建模式庫
- **基礎模式**：郵箱、URL、域名
- **網路模式**：IPv4、IPv6、MAC地址
- **日期時間**：ISO日期、US日期、24小時時間
- **身份驗證**：使用者名稱、密碼強度、UUID
- **金融模式**：信用卡號、SSN
- **國際化**：中文字元、Emoji

### 💻 程式碼生成
支援生成以下語言的完整程式碼：

| 語言 | 支援狀態 |
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
- 複雜度評分（0-100）
- 智慧優化建議
- 分組統計

### ⚡ 效能測試
- 可配置迭代次數
- 總耗時、平均耗時統計
- 每秒匹配次數

---

## 🚀 快速開始

### 環境要求
- Python 3.7 或更高版本
- 無需安裝任何外部依賴

### 安裝方式

**方式一：直接執行**
```bash
# 複製儲存庫
git clone https://github.com/gitstq/RegexForge.git
cd RegexForge

# 直接執行
python regexforge.py -p "\d+" -t "Hello 123 World"
```

**方式二：pip安裝**
```bash
# 從原始碼安裝
pip install .

# 或使用 pip install -e . 進行開發模式安裝
```

### 基本用法

```bash
# 測試正則表達式
regexforge -p "\d+" -t "Hello 123 World 456"

# 使用內建模式庫
regexforge -p "email" -t "test@example.com" --library

# 列出所有內建模式
regexforge --list-patterns

# 生成Python程式碼
regexforge -p "\d+" --generate python

# 分析模式複雜度
regexforge -p "(\w+)@(\w+)\.(\w+)" --analyze

# 效能測試
regexforge -p "\d+" -t "test 123" --performance

# JSON格式輸出
regexforge -p "\d+" -t "test 123" -o json

# 輸出到檔案
regexforge -p "\d+" -t "test 123" -o html --output-file result.html
```

---

## 📖 詳細使用指南

### 命令列參數

| 參數 | 說明 | 範例 |
|------|------|------|
| `-p, --pattern` | 正則表達式模式 | `-p "\d+"` |
| `-t, --text` | 待匹配文字 | `-t "Hello 123"` |
| `-f, --flags` | 正則標誌 | `-f "im"` |
| `-o, --output` | 輸出格式 | `-o json` |
| `--library` | 使用內建模式 | `--library` |
| `--list-patterns` | 列出所有模式 | `--list-patterns` |
| `--generate` | 生成程式碼 | `--generate python` |
| `--analyze` | 分析模式 | `--analyze` |
| `--performance` | 效能測試 | `--performance` |

### 正則標誌

| 標誌 | 說明 |
|------|------|
| `i` | 忽略大小寫 |
| `m` | 多行模式 |
| `s` | 點號匹配換行 |
| `x` | 詳細模式 |
| `a` | ASCII模式 |

### 使用範例

**1. 測試郵箱匹配**
```bash
regexforge -p "email" -t "Contact: test@example.com, sales@company.org" --library
```

**2. 提取URL**
```bash
regexforge -p "url" -t "Visit https://example.com or www.test.org" --library
```

**3. 生成JavaScript程式碼**
```bash
regexforge -p "(\w+)@(\w+)\.(\w+)" --generate javascript
```

**4. 分析複雜模式**
```bash
regexforge -p "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$" --analyze
```

**5. 效能測試**
```bash
regexforge -p "\d+" -t "test 123 456 789" --performance --iterations 10000
```

---

## 💡 設計思路與迭代規劃

### 設計理念

RegexForge 的設計遵循以下原則：

1. **零依賴優先**：使用Python標準庫實現所有功能，確保安裝簡單、相容性好
2. **開發者友善**：提供清晰的命令列介面和彩色輸出
3. **功能完整**：涵蓋正則表達式開發的全流程需求
4. **可擴展性**：模組化設計，便於添加新模式和語言支援

### 技術選型

- **語言**：Python 3.7+（廣泛相容）
- **CLI框架**：argparse（標準庫）
- **正則引擎**：re模組（標準庫）
- **輸出格式**：JSON/HTML（標準庫）

### 後續迭代計劃

- [ ] 添加更多內建模式（銀行卡號、車牌號等）
- [ ] 支援正則表達式視覺化
- [ ] 添加互動式REPL模式
- [ ] 支援批次檔案處理
- [ ] 添加正則表達式除錯器
- [ ] 支援自訂模式庫

---

## 📦 打包與部署指南

### 打包發布

```bash
# 建構分發包
python -m build

# 上傳到PyPI
twine upload dist/*
```

### 本地安裝

```bash
# 從原始碼安裝
pip install .

# 開發模式安裝
pip install -e .
```

### 相容環境

- ✅ Linux (Ubuntu, CentOS, Debian等)
- ✅ macOS (10.14+)
- ✅ Windows (10/11)
- ✅ Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12

---

## 🤝 貢獻指南

我們歡迎所有形式的貢獻！

### 如何貢獻

1. Fork 本儲存庫
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'feat: 添加某個功能'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 建立 Pull Request

### 程式碼規範

- 遵循 PEP 8 編碼規範
- 為新功能添加單元測試
- 更新相關文件

### 問題回饋

如果您發現Bug或有功能建議，請在 [Issues](https://github.com/gitstq/RegexForge/issues) 頁面提交。

---

## 📄 開源協議說明

本專案採用 [MIT License](LICENSE) 開源協議。

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
