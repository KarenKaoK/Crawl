# Crawl

`Crawl` is a crawler practice project. The main goal of this repository is to design a reusable crawling framework, with [`crawler/base_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/base_crawler.py) as the base layer and source-specific crawler implementations built on top of it.

Instead of treating each crawler as a standalone script, this project is organized around a common crawler structure:

- `base_crawler.py` defines shared crawler behavior
- source-specific crawler files implement parsing logic for different websites
- `main.py` acts as a simple entry point for running the current crawler flow

At the moment, the most concrete implementation in this repository is the ETtoday crawler in [`crawler/ettoday_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/ettoday_crawler.py).

## Project Goal

This project is intended as a practice repo for:

- designing a crawler framework
- separating common crawler utilities from site-specific logic
- experimenting with article list crawling and content extraction
- building a structure that can be extended to multiple news sources

## Framework Design

The crawler design is centered around inheritance:

- [`crawler/base_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/base_crawler.py): base crawler class with shared methods such as HTTP requests and HTML parsing
- [`crawler/ettoday_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/ettoday_crawler.py): example crawler implementation for a specific source
- [`crawler/crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/crawler.py): an experimental crawler module

The intended pattern is:

1. Create a common base crawler
2. Add a crawler class for each content source
3. Reuse shared request/parsing utilities from the base class
4. Customize only the selectors and extraction logic for each site

## Current Example Flow

The current runnable path uses ETtoday as the example source.

It currently performs:

- crawl a news listing page
- extract `title`, `category`, `date`, and `link`
- visit each article page and collect article content
- save the result as a CSV file

## Project Structure

```text
Crawl/
├── main.py
├── config.yaml
├── logger.py
├── writer.py
├── crawler/
│   ├── __init__.py
│   ├── base_crawler.py
│   ├── crawler.py
│   └── ettoday_crawler.py
├── utils/
│   ├── init_utils.py
│   └── utils.py
└── output/
```

## Requirements

- Python 3.8+

Packages used or referenced by the current code:

- `requests`
- `pandas`
- `beautifulsoup4`
- `lxml`
- `PyYAML`
- `tqdm`
- `undetected-chromedriver`

Install with:

```bash
pip install requests pandas beautifulsoup4 lxml pyyaml tqdm undetected-chromedriver
```

Or:

```bash
pip3 install requests pandas beautifulsoup4 lxml pyyaml tqdm undetected-chromedriver
```

## Usage

The current entry point is [`main.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/main.py).

Run:

```bash
python3 main.py
```

The current script:

1. loads configuration from [`config.yaml`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/config.yaml)
2. creates a timestamped output directory
3. runs the ETtoday crawler flow
4. exports results to CSV

## Output

By default, the crawler writes results under:

```text
output/<YYYYMMDD_HHMMSS>/
```

Typical output files:

```text
output/20230803_202041/output.csv
output/20230803_202041/log.log
```

The generated CSV currently includes:

- `title`
- `category`
- `date`
- `link`
- `content`

## Configuration

Configuration is stored in [`config.yaml`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/config.yaml).

Current keys include:

- `output_dir`
- `log_dir`
- `article_dir`
- `article_crawl_raw`
- `article_processed`
- `summary`
- `crawler`

Although the config already lists multiple crawler sources, the current implementation is still partially wired and mainly demonstrates the ETtoday crawler flow.

## Main Modules

- [`main.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/main.py): entry point for the current crawler run
- [`crawler/base_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/base_crawler.py): shared crawler base class
- [`crawler/ettoday_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/ettoday_crawler.py): source-specific crawler example
- [`utils/init_utils.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/utils/init_utils.py): config loading, output directory setup, logger initialization
- [`utils/utils.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/utils/utils.py): utility helpers
- [`logger.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/logger.py): logging setup

## Current Limitations

- the framework direction is clearer than the current implementation completeness
- the ETtoday source URL is still hard-coded in [`main.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/main.py)
- multiple source definitions exist in `config.yaml`, but are not fully integrated into a unified runner yet
- [`writer.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/writer.py) is still a stub
- the `content` field is not yet normalized into clean plain text

---

# 中文版說明

`Crawl` 是一個爬蟲練習專案。這個 repository 的主要目標不是只完成單一網站的爬取，而是練習設計一套可重複使用的爬蟲框架，並以 [`crawler/base_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/base_crawler.py) 作為基底，再依不同來源建立各自的 crawler。

這個專案的核心方向是：

- 用 `base_crawler.py` 定義共用的爬蟲能力
- 依不同網站或資料來源建立對應的 crawler 檔案
- 讓共用邏輯與網站專屬解析邏輯分開

目前這個 repo 裡最完整的範例，是 [`crawler/ettoday_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/ettoday_crawler.py) 的 ETtoday 爬蟲實作。

## 專案目標

這個專案主要是用來練習：

- 設計爬蟲框架
- 將共用工具與網站專屬邏輯拆分
- 練習文章列表與文章內容的爬取流程
- 建立可擴充到多個來源的結構

## 框架設計

目前的設計主軸是以繼承方式組織 crawler：

- [`crawler/base_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/base_crawler.py)：放共用的 request、HTML parsing 等方法
- [`crawler/ettoday_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/ettoday_crawler.py)：針對特定來源的 crawler 實作範例
- [`crawler/crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/crawler.py)：較早期或實驗中的 crawler 模組

預期的開發方式是：

1. 先建立共用的 base crawler
2. 針對不同來源建立自己的 crawler class
3. 重用 base class 的共用能力
4. 只在子類別中處理各網站不同的 selector 與資料擷取邏輯

## 目前的範例流程

目前實際可執行的流程是以 ETtoday 作為示範來源。

現在已經能做到：

- 爬取新聞列表頁
- 擷取 `title`、`category`、`date`、`link`
- 進入文章頁抓取內容
- 將結果輸出成 CSV

## 專案結構

```text
Crawl/
├── main.py
├── config.yaml
├── logger.py
├── writer.py
├── crawler/
│   ├── __init__.py
│   ├── base_crawler.py
│   ├── crawler.py
│   └── ettoday_crawler.py
├── utils/
│   ├── init_utils.py
│   └── utils.py
└── output/
```

## 環境需求

- Python 3.8 以上

目前程式碼中有使用或引用到的套件：

- `requests`
- `pandas`
- `beautifulsoup4`
- `lxml`
- `PyYAML`
- `tqdm`
- `undetected-chromedriver`

安裝方式：

```bash
pip install requests pandas beautifulsoup4 lxml pyyaml tqdm undetected-chromedriver
```

或：

```bash
pip3 install requests pandas beautifulsoup4 lxml pyyaml tqdm undetected-chromedriver
```

## 使用方式

目前的入口是 [`main.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/main.py)。

執行：

```bash
python3 main.py
```

目前程式會：

1. 從 [`config.yaml`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/config.yaml) 載入設定
2. 建立時間戳記輸出資料夾
3. 執行 ETtoday 的 crawler 流程
4. 將結果輸出成 CSV

## 輸出結果

預設輸出在：

```text
output/<YYYYMMDD_HHMMSS>/
```

常見產物如下：

```text
output/20230803_202041/output.csv
output/20230803_202041/log.log
```

目前 CSV 欄位包含：

- `title`
- `category`
- `date`
- `link`
- `content`

## 設定檔

設定放在 [`config.yaml`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/config.yaml)。

目前包含的 key 有：

- `output_dir`
- `log_dir`
- `article_dir`
- `article_crawl_raw`
- `article_processed`
- `summary`
- `crawler`

雖然 `config.yaml` 已經列出多個來源，但目前實作還是以 ETtoday 範例為主。

## 主要模組

- [`main.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/main.py)：目前的執行入口
- [`crawler/base_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/base_crawler.py)：共用的 crawler base class
- [`crawler/ettoday_crawler.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/crawler/ettoday_crawler.py)：來源專屬 crawler 範例
- [`utils/init_utils.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/utils/init_utils.py)：設定讀取、輸出資料夾建立、logger 初始化
- [`utils/utils.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/utils/utils.py)：輔助工具函式
- [`logger.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/logger.py)：日誌設定

## 目前限制

- 目前比較明確的是框架方向，整體實作仍在逐步補齊
- ETtoday 的來源網址仍寫在 [`main.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/main.py) 中
- `config.yaml` 雖然有多個來源設定，但還沒有完全整合進統一 runner
- [`writer.py`](/Users/ren/Desktop/karen/git_karen/Crawl-and-Gen/writer.py) 仍是 stub
- 部分模組仍帶有實驗性質或尚未完成
- `content` 欄位目前還沒有整理成乾淨的純文字格式

