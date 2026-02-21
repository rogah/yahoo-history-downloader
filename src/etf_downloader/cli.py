import typer
import yfinance as yf
from datetime import datetime
from pathlib import Path

app = typer.Typer(help="Download historical ETF/stock data from Yahoo Finance.")

@app.callback()
def _main():
    """ETF history downloader."""
    pass

def sanitize_date(date_str: str) -> str:
    return date_str.replace("-", "")

def build_filename(ticker: str, interval: str, start: str, end: str) -> str:
    return f"{ticker.replace('.', '_')}_{interval}_{sanitize_date(start)}_{sanitize_date(end)}.csv"

@app.command()
def download(
    tickers: list[str] = typer.Argument(..., help="Ticker symbol(s), e.g. A200.AX IVV.AX"),
    start: str = typer.Option("2000-01-01", "--start", "-s", help="Start date (YYYY-MM-DD)"),
    end: str | None = typer.Option(None, "--end", "-e", help="End date (YYYY-MM-DD)"),
    interval: str = typer.Option("1d", "--interval", "-i", help="Interval: 1d, 1wk, 1mo"),
    combined: bool = typer.Option(False, "--combined", "-c", help="Combine multi-ticker output into one file"),
    output: str | None = typer.Option(None, "--output", "-o", help="Output file or directory"),
):
    end = end or datetime.today().strftime("%Y-%m-%d")
    typer.echo(f"Downloading {', '.join(tickers)} from {start} to {end} ({interval})...")

    df = yf.download(
        tickers,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=False,
        group_by="ticker",
        progress=False,
    )

    if df.empty:
        typer.echo("No data returned.")
        raise typer.Exit(1)

    out = Path(output).expanduser() if output else Path.cwd()
    if output:
        (out if out.suffix == "" else out.parent).mkdir(parents=True, exist_ok=True)

    if len(tickers) == 1:
        ticker = tickers[0]
        final = out if (output and out.suffix) else out / build_filename(ticker, interval, start, end)
        df.to_csv(final)
        typer.echo(f"Saved {final}")
        return

    if combined:
        final = out if (output and out.suffix) else out / build_filename("combined", interval, start, end)
        df.to_csv(final)
        typer.echo(f"Saved {final}")
        return

    if output and out.suffix:
        raise typer.Exit("Error: --output must be a directory when saving multiple separate files.")

    for ticker in tickers:
        ticker_df = df[ticker].dropna(how="all")
        final = out / build_filename(ticker, interval, start, end)
        ticker_df.to_csv(final)
        typer.echo(f"Saved {final}")