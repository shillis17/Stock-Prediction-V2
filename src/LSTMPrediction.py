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

class LSTMPrediction():
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
        self._format_data()
        self._fit_and_predict()
        self._plot()
        
    def _format_data(self):
        """
        Takes self.data and scales and splits into training and testing data 
        for model as well as formatting into the propper shape to be input into
        an lstm model.
        """
        data = self.data.copy()

        self.scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = self.scaler.fit_transform(data)
        X = [] 
        y = []
        for i in range((self.days*5),len(data)-self.days):
            X.append(scaled_data[i-(self.days*5):i,0])
            y.append(scaled_data[i,0])
        X, y = np.array(X), np.array(y)
        X = np.reshape(X, (X.shape[0],X.shape[1],1))
        self.X = X
        self.y = y

    def _fit_and_predict(self):
        """
        creates the prophet model and casts predictions based on the self.train
        and self.test data. Saves results to a Pandas DataFrame.
        """
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True,
               input_shape=(self.X.shape[1],1)))
        model.add(LSTM(units=50))
        model.add(Dense(1))

        model.compile(loss=root_mean_squared_error, optimizer='adam')
        model.fit(self.X, self.y, epochs=5, batch_size=32)

        predictions = self.data.close[-(self.days*5):]
        for i in range (self.days):
            x = np.array(predictions[-(self.days*5):]).reshape(-1,1)
            scaled_x = self.scaler.fit_transform(x)
            scaled_x = scaled_x.reshape(1,-1,1)
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
        prediction = self.predictions[-self.days:].values
        index = np.arange(1,self.days+1)
        fig,ax = plt.subplots(figsize=(12, 8))
        plt.plot(index,prediction,'k')
        plt.autoscale()
        plt.tight_layout(pad=3)
        plt.xlabel('Days Out (From Today)')
        plt.ylabel('Value (US$)')
        plt.title(self.name + ' LSTM Prediction')
        plt.xticks(rotation=90)
        plt.savefig('../img/Predictions/'+self.name+'_'+str(self.days)+'_Days_LSTM.png')