from gather_data import get_data
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
plt.style.use('fivethirtyeight')

google,microsoft,apple,jnj,amazon = get_data()

def plot(stock,name):
    fig, ax = plt.subplots()
    plt.autoscale()
    plt.tight_layout(pad=3)
    plt.plot(stock.close)
    plt.xlabel('Date')
    plt.ylabel('Value (US$)')
    plt.title(name+' Stock History')
    plt.savefig('../img/EDA/'+name+'History.png')

stocks = [['GOOGL',google],['MSFT',microsoft],['AAPL',apple],['JNJ',jnj],['AMZN',amazon]]

for i in stocks:
    print(i[1].head(10))

for i in stocks:
    plot(i[1],i[0])