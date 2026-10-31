import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Fetch Tesla stock data for the last 3 months
ticker = yf.Ticker("TSLA")
df = ticker.history(period="3mo")

if df.empty:
    raise SystemExit("No data returned for TSLA")

start_price = float(df["Close"].iloc[0])
end_price = float(df["Close"].iloc[-1])
pct_change = ((end_price - start_price) / start_price) * 100
high = float(df["High"].max())
low = float(df["Low"].min())

fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={"height_ratios": [3, 1]})
fig.suptitle(
    f"Tesla (TSLA) - Last 3 Months  |  {pct_change:+.1f}%  (${start_price:.2f} to ${end_price:.2f})",
    fontsize=14,
    fontweight="bold",
)

# Price chart
axes[0].plot(df.index, df["Close"], color="#cc0000", linewidth=2, label="Close")
axes[0].fill_between(df.index, df["Close"], alpha=0.15, color="#cc0000")
axes[0].axhline(start_price, color="gray", linestyle="--", linewidth=1, alpha=0.7, label=f"Start ${start_price:.2f}")
axes[0].set_ylabel("Price (USD)")
axes[0].legend(loc="upper left")
axes[0].grid(True, alpha=0.3)
axes[0].set_title(f"High ${high:.2f}  |  Low ${low:.2f}")

# Volume chart
axes[1].bar(df.index, df["Volume"], color="#666666", width=0.8, alpha=0.7)
axes[1].set_ylabel("Volume")
axes[1].set_xlabel("Date")
axes[1].grid(True, alpha=0.3)
axes[1].xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
axes[1].xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
fig.autofmt_xdate()

plt.tight_layout()
plt.show()
