from pprint import pprint

import numpy as np
import pandas as pd
from sklearn.svm import SVC
from pylab import plt

# --- SET UP DATA ---
# read the data
data = pd.read_csv('../data/tr_eikon_eod_data.csv', index_col=0, parse_dates=True)
# take historical end-of-day stock price
data = pd.DataFrame(data['AAPL.O'])
# calculate log returns
data['Returns'] = np.log(data / data.shift())
data.dropna(inplace=True)

# create a lag dataset
lags = 6
cols = []
for lag in range(1, lags + 1):
    col = 'lag_{}'.format(lag)
    data[col] = np.sign(data['Returns'].shift(lag))
    cols.append(col)
data.dropna(inplace=True)
# --- END SET UP DATA ---

sample = data[:2000].copy(deep=False)
outOfSample = data[2000:].copy(deep=False)

# fit the model
model = SVC(gamma='auto')
model.fit(sample[cols], np.sign(sample['Returns']))
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape='ovr',
    degree=3, gamma='auto', kernel='rbf',max_iter=-1, probability=False, random_state=None,
    shrinking=True, tol=0.001, verbose=False)

# sample predictions
sample['Prediction'] = model.predict(sample[cols])
sample['Strategy'] = sample['Prediction'] * sample['Returns']
# show sample prediction strategy
sample[['Returns', 'Strategy']].cumsum().apply(np.exp).plot(figsize=(10, 6))
plt.title('Sample Predictions')

# out of sample prediction
outOfSample['Prediction'] = model.predict(outOfSample[cols])
outOfSample['Strategy'] = outOfSample['Prediction'] * outOfSample['Returns']
outOfSample[['Returns', 'Strategy']].cumsum().apply(np.exp).plot(figsize=(10, 6))
plt.title('Out Of Sample Predictions')

# show plots
plt.show()

# -- Conclusion --
# Out of sample results leads us with an underperformed strategy
# Thus, our prediction model will need some work :P :P
