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
* Custom date ranges
* Daily / weekly / monthly intervals
* Period-safe filenames (no accidental overwrites)
* Optional combined multi-ticker output
* Proper CLI entrypoint (`etf` command)

---

## 📦 Installation

### 1️⃣ Install `uv` (if not already installed)

```bash
brew install uv
```

or

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### 2️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd yahoo-history-downloader
```

---

### 3️⃣ Enable packaging mode (already configured)

The project uses:

```toml
[tool.uv]
package = true
```

This allows CLI entrypoints to be installed.

---

### 4️⃣ Install dependencies & CLI entrypoint

```bash
uv sync
```

This installs:

* Dependencies
* The `etf` CLI command

---

## 🖥 Usage

### Download a single ETF

```bash
uv run etf A200.AX --start 2019-01-01 --end 2024-01-01
```

Output:

```
A200_AX_1d_20190101_20240101.csv
```

---

### Download multiple ETFs (separate files)

```bash
uv run etf A200.AX VAS.AX IVV.AX --start 2015-01-01
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
uv run etf A200.AX VAS.AX IVV.AX --combined
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
| `--interval` | `1d`, `1wk`, `1mo`                        | 1d         |
| `--combined` | Combine multi-ticker output into one file | False      |

---

## 📁 Output Format

Files are always named using:

```
{TICKER}_{INTERVAL}_{START}_{END}.csv
```

Example:

```
A200_AX_1d_20190101_20240101.csv
```

This ensures:

* No file overwrite conflicts
* Self-describing datasets
* Easy version tracking

---

## 🛠 Project Structure

```
yahoo-history-downloader/
│
├── pyproject.toml
├── uv.lock
├── README.md
└── src/
    └── etf_downloader/
        ├── __init__.py
        └── cli.py
```

---

## 📊 Data Source

Data is retrieved using the `yfinance` library, which handles:

* Yahoo session management
* Crumb tokens
* Rate limiting
* Retry logic

This avoids the need to manually handle Yahoo’s protected endpoints.

---

## 🧠 Future Improvements

Potential extensions:

* Portfolio return & CAGR calculation
* Drawdown analysis
* Sharpe ratio computation
* `--period 5y` shorthand
* Parquet output support
* Scheduled automation
* Portfolio backtesting mode
* `etf version` command

---

## 📄 License

MIT License (or your preferred license)
