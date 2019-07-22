from fbprophet import Prophet
import pandas as pd
from suppress import suppress_stdout_stderr
from gather_data import get_data
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
plt.style.use('fivethirtyeight')
# Get data from get_data
google, microsoft, apple, jnj, amazon = get_data()
stocks = [['GOOGL', google], ['MSFT', microsoft], ['AAPL', apple],
          ['JNJ', jnj], ['AMZN', amazon]]


class ProhetClass():
    """
    Fit and save graph for prophet model based on stock data.

    Takes stock data from get_data and uses fbprophet to train and predict data
    for a given ammount of time.

    Attributes:
        data    (Padnas DataFame): Dataframe of stock data from get_data()
        name    (String): name of the stock used for save file and graph title
    """

    def __init__(self, data, name):
        self.data = data
        self.name = name
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

        self.train = data[:2265]
        self.test = data[-252:]

    def _fit_and_predict(self):
        """
        creates the prophet model and casts predictions based on the self.train
        and self.test data. Saves results to a Pandas DataFrame.
        """
        with suppress_stdout_stderr():
            model = Prophet(
                    daily_seasonality=False,
                    weekly_seasonality=False,
                    yearly_seasonality=True,
                    changepoint_prior_scale=.05
                    )
            model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
            model.fit(self.train)
            future = pd.DataFrame()
            future['ds'] = google.index.tz_localize(tz=None).values
            self.forecast = model.predict(future)
            self.forecast.set_index('ds', inplace=True)

    def _plot(self):
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.autoscale()
        plt.tight_layout(pad=3)
        plt.plot(self.train.y)
        plt.plot(self.test.y)
        plt.plot(self.forecast.yhat[-252:])
        plt.legend(['History', 'Actual', 'Predicted'])
        plt.xlabel('Date')
        plt.ylabel('Value (US$)')
        plt.title(self.name + ' Prophet Prediction')
        plt.savefig('../img/Prophet/'+self.name+'Prophet.png')


for i in stocks:
    ProhetClass(i[1], i[0])
