from gather_data import get_data
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
plt.style.use('fivethirtyeight')
# Get data from get_data
google, microsoft, apple, jnj, amazon = get_data()


def plot(stock, name):
    """
    Makes plots for visual EDA to see historical data easier than in DataFrame

    Parameters:
        stock (PandasDataFrame): Dataframe of stock data from get_data()
        name  (string): name of the stock used for save file and graph title

    Returns:
        None
    """
    fig, ax = plt.subplots()
    plt.autoscale()
    plt.tight_layout(pad=3)
    plt.plot(stock.close)
    plt.xlabel('Date')
    plt.ylabel('Value (US$)')
    plt.title(name+' Stock History')
    plt.savefig('../img/EDA/'+name+'History.png')


stocks = [['GOOGL', google], ['MSFT', microsoft], ['AAPL', apple],
          ['JNJ', jnj], ['AMZN', amazon]]

for i in stocks:
    print(i[1].head(10))
