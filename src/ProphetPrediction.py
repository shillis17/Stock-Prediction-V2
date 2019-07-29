import numpy as np
from fbprophet import Prophet
import pandas as pd
from suppress import suppress_stdout_stderr
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pandas.tseries import converter
converter.register()

rcParams.update({'figure.autolayout': True})
plt.style.use('fivethirtyeight')


class ProhetPrediction():
    """
    Fit and save graph for prophet model based on stock data.

    Takes stock data from get_data and uses fbprophet to train and predict data
    for a given ammount of time.

    Attributes:
        data    (Padnas DataFame): Dataframe of stock data from get_data()
        name    (String): name of the stock used for save file and graph title
    """

    def __init__(self, data, name, days):
        self.data = data
        self.name = name
        self.days = days
        self._label_data()
        self._fit_and_predict()
#        self._plot()

    def _label_data(self):
        """
        Takes self.data and labels columns expected from model.
        """
        data = pd.DataFrame(index=self.data.index.tz_localize(tz=None))
        data['y'] = self.data.close.values
        data['ds'] = self.data.index.tz_localize(tz=None)

        self.labels = data

    def _fit_and_predict(self):
        """
        creates the prophet model and casts predictions based on the self.train
        and self.test data. Saves results to a Pandas DataFrame.
        """
        with suppress_stdout_stderr():
            model = Prophet(
                    daily_seasonality=True,
                    weekly_seasonality=True,
                    yearly_seasonality=False,
                    changepoint_prior_scale=.05
                    )
            model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
            model.fit(self.labels)
            future = model.make_future_dataframe(periods=self.days)
            self.forecast = model.predict(future)

    def _plot(self):
        prediction = self.forecast[-self.days:]
        index = np.arange(1, self.days+1)
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.plot(index, prediction.yhat.values, 'k')
        plt.autoscale()
        plt.tight_layout(pad=3)
        plt.xlabel('Days Out (From Today)')
        plt.ylabel('Value (US$)')
        plt.title(self.name + ' Prophet Prediction')
        plt.savefig('../img/Predictions/' + self.name+'_' +
                    str(self.days) + '_Days_Prophet.png')
