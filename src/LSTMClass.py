
import pandas as pd
from suppress import suppress_stdout_stderr
from gather_data import get_data
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.preprocessing import MinMaxScaler

rcParams.update({'figure.autolayout': True})
plt.style.use('fivethirtyeight')
# Get data from get_data
google, microsoft, apple, jnj, amazon = get_data()
stocks = [['GOOGL', google], ['MSFT', microsoft], ['AAPL', apple],
          ['JNJ', jnj], ['AMZN', amazon]]


class LSTM():
    """
    Fit and save graph for prophet model based on stock data.

    Takes stock data from get_data and uses Keras to train and predict data
    using an LSTM model for a given ammount of time.

    Attributes:
        data    (Padnas DataFame): Dataframe of stock data from get_data()
        name    (String): name of the stock used for save file and graph title
    """

    def __init__(self, data, name):
        self.data = data
        self.name = name

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