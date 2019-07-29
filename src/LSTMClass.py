import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from keras import backend as K
import matplotlib.pyplot as plt
from matplotlib import rcParams
from pandas.tseries import converter
converter.register()

rcParams.update({'figure.autolayout': True})
plt.style.use('fivethirtyeight')


def root_mean_squared_error(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))


class LSTMClass():
    """
    Fit and save graph for prophet model based on stock data.

    Takes stock data from get_data and uses Keras to train and predict data
    using an LSTM model for a given ammount of time.

    Attributes:
        data    (Padnas DataFame): Dataframe of stock data from get_data()
        name    (String): name of the stock used for save file and graph title
    """

    def __init__(self, data, name, days):
        self.data = data
        self.name = name
        self.days = days
        self._split_format_data()
        self._fit_and_predict()
#        self._plot()

    def _split_format_data(self):
        """
        Takes self.data and scales and splits into training and testing data
        for model as well as formatting into the propper shape to be input into
        an lstm model.
        """
        self.train = self.data[:len(self.data)-self.days]
        self.feed = self.train.copy()
        self.test = self.data[-self.days-1:]
        self.actuals = self.test.close
        train = self.train.close.values.reshape(-1, 1)

        self.scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = self.scaler.fit_transform(train)
        X_train = []
        y_train = []
        for i in range((self.days*5), len(train)-self.days):
            X_train.append(scaled_data[i-(self.days*5):i, 0])
            y_train.append(scaled_data[i, 0])
        X_train, y_train = np.array(X_train), np.array(y_train)
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        self.X_train = X_train
        self.y_train = y_train

    def _fit_and_predict(self):
        """
        creates the prophet model and casts predictions based on the self.train
        and self.test data. Saves results to a Pandas DataFrame.
        """
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True,
                       input_shape=(self.X_train.shape[1], 1)))
        model.add(LSTM(units=50))
        model.add(Dense(1))

        model.compile(loss=root_mean_squared_error, optimizer='adam')
        model.fit(self.X_train, self.y_train, epochs=1, batch_size=252)

        predictions = self.feed.close[-(self.days*5):]
        for i in range(self.days):
            x = np.array(predictions[-(self.days*5):]).reshape(-1, 1)
            scaled_x = self.scaler.fit_transform(x)
            scaled_x = scaled_x.reshape(1, -1, 1)
            pred = model.predict(scaled_x)
            pred = self.scaler.inverse_transform(pred)
            predictions = predictions.append(pd.Series(pred[0][0]),
                                             ignore_index=True)
        self.predictions = predictions

    def _plot(self):
        """
        Plots the results of the prediction on the actuals provided by
        get_data().
        """
        hist = self.train.close[-self.days:]
        pred = self.predictions[-self.days-1:]
        true = self.test
        actual = true.close
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.autoscale()
        plt.tight_layout(pad=3)
        ax.plot(hist)
        ax.plot(actual.index, pred)
        ax.plot(actual)
        ax.legend(['History', 'Predictions', 'actual'])
        plt.xlabel('Date')
        plt.ylabel('Value (US$)')
        plt.title(self.name + ' LSTM Prediction')
        plt.xticks(rotation=90)
        plt.savefig('../img/LSTM/' + self.name +
                    '_'+str(self.days) + '_Days_LSTM.png')
