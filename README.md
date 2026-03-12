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



