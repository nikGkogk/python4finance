from pprint import pprint

import pandas as pd
import numpy as np
import cufflinks as cf
import plotly.offline as plyo
import matplotlib as mplt

# Reads the financial data from a CSV file.
raw = pd.read_csv('../data/fxcm_eur_usd_eod_data.csv', index_col=0, parse_dates=True)

# The resulting DataFrame object consists of multiple columns and more than 1,500 data rows.
pprint(raw.info())

# Selects four columns from the DataFrame object (Open-High-Low-Close, or OHLC).
quotes = raw[['AskOpen', 'AskHigh', 'AskLow', 'AskClose']]
quotes = quotes.iloc[-60:] # Only a few data rows are used for the visualization.

pprint(quotes)

# Create initial QuantFigure
qf = cf.QuantFig(
    quotes, # The DataFrame object is passed to the QuantFig constructor.
    title='EUR/USD Exchange Rate',
    legend='top',
    name='EUR/USD'
)

# Add Bollinger Bands
qf.add_bollinger_bands(
    periods=15, # The number of periods for the Bollinger band.
    boll_std=2  # The number of standard deviations to be used for the band width.
)

plyo.init_notebook_mode(connected=True) # Turns on the notebook plotting mode.
plyo.iplot(qf.iplot(asFigure=True),image='png',filename='qf_02')

qf.add_rsi(
    periods=14,     # Fixes the RSI period.
    showbands=False # Does not show an upper or lower band
)

plyo.plot(
    qf.iplot(asFigure=True),
    filename='qf.html'
)
