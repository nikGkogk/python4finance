import numpy as np
import pandas as pd
from pylab import plt

TRADING_DAYS_COUNT = 256

data = pd.read_csv('../data/tr_eikon_eod_data.csv', index_col=0, parse_dates=True)
data = pd.DataFrame(data['.SPX'])
data.dropna(inplace=True)
data.info()

# log returns
data['returns'] = np.log(data / data.shift(1))
# rolling annualized volatility
data['volatility'] = data['returns'].rolling(TRADING_DAYS_COUNT).std() * np.sqrt(TRADING_DAYS_COUNT)

# plot
data[['.SPX', 'volatility']].plot(subplots=True, figsize=(10, 6))
plt.show()
