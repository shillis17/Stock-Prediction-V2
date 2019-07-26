from fbprophet import Prophet
import pandas as pd
from suppress import suppress_stdout_stderr
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pandas.tseries import converter
converter.register()

rcParams.update({'figure.autolayout': True})
plt.style.use('fivethirtyeight')


class ProhetClass():
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
        self._split_data()
        self._fit_and_predict()
        self._plot()

    def _split_data(self):
        """
        Takes self.data and splits into training and testing data for model.
        """
        data = pd.DataFrame(index=self.data.index.tz_localize(tz=None))
        data['y'] = self.data.close.values
        data['ds'] = self.data.index.tz_localize(tz=None)

        self.train = data[:len(self.data)-self.days]
        self.test = data[-self.days:]

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
            model.fit(self.train)
            future = pd.DataFrame()
            future['ds'] = self.data.index.tz_localize(tz=None).values
            self.forecast = model.predict(future)
            self.forecast.set_index('ds', inplace=True)

    def _plot(self):
        hist = self.data.close[:1+len(self.data)-self.days]
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.autoscale()
        plt.tight_layout(pad=3)
        plt.plot(hist.index[-self.days:], hist[-self.days:])
        plt.plot(self.forecast.index[-self.days:],
                 self.forecast.yhat[-self.days:])
        plt.plot(self.test.index, self.test.y)
        ax.legend(['History', 'Predictions', 'actual'])
        plt.xlabel('Date')
        plt.ylabel('Value (US$)')
        plt.title(self.name + ' Prophet Prediction')
        plt.xticks(rotation=90)
        plt.savefig('../img/Prophet/' + self.name+'_' +
                    str(self.days) + '_Days_Prophet.png')
