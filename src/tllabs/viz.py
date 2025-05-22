"""Visualization utilities for DIFF1 returns using ASCII charts."""

import argparse
import csv
from typing import List


def read_returns(file_path: str, column: str) -> List[float]:
    """Read hourly returns for a given column from a CSV file."""
    returns = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            value = row.get(column)
            if value:
                try:
                    returns.append(float(value))
                except ValueError:
                    continue
    return returns


def returns_to_prices(returns: List[float], base: float = 100.0) -> List[float]:
    """Convert returns to a price series using cumulative product."""
    prices = [base]
    for r in returns:
        prices.append(prices[-1] * (1 + r))
    return prices


def compute_rsi(prices: List[float], period: int = 14) -> List[float]:
    """Compute Relative Strength Index (RSI) for a price series."""
    if period <= 0:
        raise ValueError("period must be positive")
    gains = []
    losses = []
    rsi = []
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        gains.append(max(diff, 0))
        losses.append(-min(diff, 0))
        if i >= period:
            avg_gain = sum(gains[-period:]) / period
            avg_loss = sum(losses[-period:]) / period
            if avg_loss == 0:
                rsi.append(100.0)
            else:
                rs = avg_gain / avg_loss
                rsi.append(100 - (100 / (1 + rs)))
    return rsi


def ascii_line(values: List[float], width: int = 80, height: int = 20) -> str:
    """Return a simple ASCII line chart for the given values."""
    if not values:
        return ""
    min_v = min(values)
    max_v = max(values)
    if max_v == min_v:
        max_v += 1
    step = max(1, len(values) // width)
    scaled = values[::step]
    while len(scaled) > width:
        scaled = scaled[::2]
    rows = [[" " for _ in range(len(scaled))] for _ in range(height)]
    for x, val in enumerate(scaled):
        y = int((val - min_v) / (max_v - min_v) * (height - 1))
        rows[height - 1 - y][x] = "*"
    chart_lines = ["".join(row) for row in rows]
    return "\n".join(chart_lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="DIFF1 ASCII visualization")
    parser.add_argument("--file", default="DIFF1", help="Path to DIFF1 CSV file")
    parser.add_argument(
        "--column",
        default="diff_return_trend_team",
        help="Column name with returns to visualize",
    )
    parser.add_argument(
        "--period", type=int, default=14, help="RSI period in hours"
    )
    args = parser.parse_args(argv)

    returns = read_returns(args.file, args.column)
    if not returns:
        print(f"No returns found for column {args.column}")
        return
    prices = returns_to_prices(returns)
    rsi_values = compute_rsi(prices, period=args.period)

    print("Close price chart:")
    print(ascii_line(prices[-len(rsi_values) - 1 :]))
    print("\nRSI chart:")
    print(ascii_line(rsi_values))


if __name__ == "__main__":
    main()
