import typer
import yfinance as yf
from datetime import datetime

def main(
    ticker: str,
    start: str = "2000-01-01",
    end: str = datetime.today().strftime("%Y-%m-%d"),
    interval: str = "1d",
    output: str | None = None,
):
    """
    Download historical ETF data using yfinance.
    """

    typer.echo(f"Downloading {ticker} from {start} to {end} ({interval})...")

    df = yf.download(
        ticker,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=False,
        progress=False,
    )

    if df.empty:
        typer.echo("No data returned.")
        raise typer.Exit(1)

    output_file = output or f"{ticker.replace('.', '_')}_{interval}.csv"
    df.to_csv(output_file)

    typer.echo(f"Saved to {output_file}")

if __name__ == "__main__":
    typer.run(main)