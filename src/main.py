import typer
import yfinance as yf
from datetime import datetime
import pandas as pd

def sanitize_date(date_str: str) -> str:
    return date_str.replace("-", "")

def main(
    tickers: list[str],
    start: str = "2000-01-01",
    end: str = datetime.today().strftime("%Y-%m-%d"),
    interval: str = "1d",
    combined: bool = False,
):
    """
    Download historical data for one or more ETFs using yfinance.
    Output filenames always include period range to avoid conflicts.
    """

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

    start_clean = sanitize_date(start)
    end_clean = sanitize_date(end)

    # Single ticker case
    if len(tickers) == 1:
        ticker = tickers[0]
        filename = f"{ticker.replace('.', '_')}_{interval}_{start_clean}_{end_clean}.csv"
        df.to_csv(filename)
        typer.echo(f"Saved {filename}")
        return

    # Multiple tickers
    if combined:
        filename = f"combined_{interval}_{start_clean}_{end_clean}.csv"
        df.to_csv(filename)
        typer.echo(f"Saved {filename}")
    else:
        for ticker in tickers:
            ticker_df = df[ticker].dropna(how="all")
            filename = f"{ticker.replace('.', '_')}_{interval}_{start_clean}_{end_clean}.csv"
            ticker_df.to_csv(filename)
            typer.echo(f"Saved {filename}")

if __name__ == "__main__":
    typer.run(main)