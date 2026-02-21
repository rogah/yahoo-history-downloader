# Yahoo ETF History Downloader

A lightweight CLI tool for downloading historical ETF and stock price data using `yfinance`.

Built with:

* Python 3.12
* uv (fast Python package manager)
* typer (CLI framework)
* yfinance (Yahoo Finance wrapper)

---

## 🚀 Features

* Download one or multiple tickers
* Supports custom date ranges
* Supports daily / weekly / monthly intervals
* Automatic period-safe filenames
* Optional combined multi-ticker output
* Clean CLI interface

---

## 📦 Installation

### 1. Install `uv` (if not already installed)

```bash
brew install uv
```

or

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### 2. Clone the repository

```bash
git clone <your-repo-url>
cd yahoo-history-downloader
```

---

### 3. Install dependencies

```bash
uv sync
```

---

## 🖥 Usage

### Download a single ETF

```bash
uv run python src/main.py A200.AX --start 2019-01-01 --end 2024-01-01
```

Example output:

```
A200_AX_1d_20190101_20240101.csv
```

---

### Download multiple ETFs (separate files)

```bash
uv run python src/main.py A200.AX VAS.AX IVV.AX --start 2015-01-01
```

Outputs:

```
A200_AX_1d_20150101_20260221.csv
VAS_AX_1d_20150101_20260221.csv
IVV_AX_1d_20150101_20260221.csv
```

---

### Download multiple ETFs into one combined file

```bash
uv run python src/main.py A200.AX VAS.AX IVV.AX --combined
```

Output:

```
combined_1d_20000101_20260221.csv
```

---

## ⚙ CLI Options

| Option       | Description                               | Default    |
| ------------ | ----------------------------------------- | ---------- |
| `--start`    | Start date (YYYY-MM-DD)                   | 2000-01-01 |
| `--end`      | End date (YYYY-MM-DD)                     | Today      |
| `--interval` | Data interval (`1d`, `1wk`, `1mo`)        | 1d         |
| `--combined` | Combine multi-ticker output into one file | False      |

---

## 📁 Output Format

* CSV format
* Includes: Open, High, Low, Close, Adj Close, Volume
* Filenames include:

  * Ticker
  * Interval
  * Start date
  * End date

Example:

```
A200_AX_1d_20190101_20240101.csv
```

This prevents file overwrites and makes datasets self-describing.

---

## 📊 Data Source

Data is retrieved via the `yfinance` library, which wraps Yahoo Finance’s historical data endpoints.

This tool is intended for personal research and educational use.

---

## 🛠 Project Structure

```
yahoo-history-downloader/
│
├── pyproject.toml
├── uv.lock
├── README.md
└── src/
    └── main.py
```

---

## 🧠 Why `yfinance`?

Yahoo’s raw download endpoints require cookies and crumb tokens.
`yfinance` handles:

* Session management
* Crumb retrieval
* Retries
* Rate limiting

This keeps the CLI simple and reliable.

---

## 📌 Future Improvements

Potential extensions:

* Portfolio return & CAGR calculation
* Drawdown analysis
* Sharpe ratio computation
* Period shorthand (`--period 5y`)
* Parquet output support
* Scheduled automation
* Portfolio backtesting mode

---

## 📄 License

MIT License (or your preferred license)
