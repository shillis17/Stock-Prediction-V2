from tiingo import TiingoClient
import os
import datetime

def get_data():
    now = datetime.datetime.now()
    end = str(now.year) + '-' + str(now.month) + '-' + str(now.day-1)
    start = str(now.year - 10) + '-' + str(now.month) + '-' + str(now.day-1)

    config = {'api_key':os.environ.get('TIINGO_API_KEY'),'session':True}
    client = TiingoClient(config)

    google = client.get_dataframe("GOOGL",
                              startDate=start,
                              endDate=end,
                              frequency='daily')
    google.to_csv('../data/google.csv')

    microsoft = client.get_dataframe("MSFT",
                              startDate=start,
                              endDate=end,
                              frequency='daily')
    microsoft.to_csv('../data/microsoft.csv')

    apple = client.get_dataframe("AAPL",
                              startDate=start,
                              endDate=end,
                              frequency='daily')
    apple.to_csv('../data/apple.csv')

    jnj = client.get_dataframe("JNJ",
                              startDate=start,
                              endDate=end,
                              frequency='daily')
    jnj.to_csv('../data/jnj.csv')

    amazon = client.get_dataframe("AMZN",
                              startDate=start,
                              endDate=end,
                              frequency='daily')
    amazon.to_csv('../data/amazon.csv')
    
    return google,microsoft,apple,jnj,amazon
