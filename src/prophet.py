from fbprophet import Prophet
import pandas as pd
from suppress import suppress_stdout_stderr
from gather_data import get_data
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
plt.style.use('fivethirtyeight')

google,microsoft,apple,jnj,amazon = get_data()
stocks = [['GOOGL',google],['MSFT',microsoft],['AAPL',apple],['JNJ',jnj],['AMZN',amazon]]

def prophet (dataframe,name):
    data = pd.DataFrame(index = dataframe.index.tz_localize(tz=None))
    data['y']=dataframe.close.values
    data['ds']=dataframe.index.tz_localize(tz=None)

    train = data [:2265]
    test = data [-252:]

    with suppress_stdout_stderr():
        model = Prophet(
                daily_seasonality=False,
                weekly_seasonality=False,
                yearly_seasonality=True,
                changepoint_prior_scale=.05
                )
        model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
        model.fit(train)
        future = pd.DataFrame()
        future['ds'] = google.index.tz_localize(tz=None).values
        forecast = model.predict(future)
        forecast.set_index('ds',inplace=True)
    
    fig, ax = plt.subplots()
    plt.autoscale()
    plt.tight_layout(pad=3)
    plt.plot(train.y)
    plt.plot(test.y)
    plt.plot(forecast.yhat[-252:])
    plt.legend(['History','Actual','Predicted'])
    plt.xlabel('Date')
    plt.ylabel('Value (US$)')
    plt.title(name + ' Prophet Prediction')
    plt.savefig('../img/Prophet/'+name+'Prophet.png')

for i in stocks:
    prophet(i[1],i[0])
