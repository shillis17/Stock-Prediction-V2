from ProphetPrediction import ProhetPrediction
from LSTMPrediction import LSTMPrediction
from gather_data import get_data
import boto3

s3 = boto3.client('s3')

google, microsoft, apple, jnj, amazon = get_data()

stocks = [['GOOGL', google], ['MSFT', microsoft], ['AAPL', apple],
          ['JNJ', jnj], ['AMZN', amazon]]

days = [7,14,30]


def make_graphs(stocks,days):
    """
    Make graphs for web app
    
    Calls scripts to train and graph the models and save the graphs locally
    
    Attributes:
        stocks: list of lists containing stock dataframes and names
        days: list of ints of prediction windows
    """
    for i in stocks:
        for n in days:
            ProhetPrediction(i[1], i[0], n)
            LSTMPrediction(i[1], i[0], n)
    return None

make_graphs(stocks,days)

# Upload LSTM predictions
s3.upload_file('../img/Predictions/AAPL_7_Days_LSTM.png',
               'web-app-storage',
               'AAPL_7_Days_LSTM.png')
s3.upload_file('../img/Predictions/AAPL_14_Days_LSTM.png',
               'web-app-storage',
               'AAPL_14_Days_LSTM.png')
s3.upload_file('../img/Predictions/AAPL_30_Days_LSTM.png',
               'web-app-storage',
               'AAPL_30_Days_LSTM.png')
s3.upload_file('../img/Predictions/AMZN_7_Days_LSTM.png',
               'web-app-storage',
               'AMZN_7_Days_LSTM.png')
s3.upload_file('../img/Predictions/AMZN_14_Days_LSTM.png',
               'web-app-storage',
               'AMZN_14_Days_LSTM.png')
s3.upload_file('../img/Predictions/AMZN_30_Days_LSTM.png',
               'web-app-storage',
               'AMZN_30_Days_LSTM.png')
s3.upload_file('../img/Predictions/GOOGL_7_Days_LSTM.png',
               'web-app-storage',
               'GOOGL_7_Days_LSTM.png')
s3.upload_file('../img/Predictions/GOOGL_14_Days_LSTM.png',
               'web-app-storage',
               'GOOGL_14_Days_LSTM.png')
s3.upload_file('../img/Predictions/GOOGL_30_Days_LSTM.png',
               'web-app-storage',
               'GOOGL_30_Days_LSTM.png')
s3.upload_file('../img/Predictions/JNJ_7_Days_LSTM.png',
               'web-app-storage',
               'JNJ_7_Days_LSTM.png')
s3.upload_file('../img/Predictions/JNJ_14_Days_LSTM.png',
               'web-app-storage',
               'JNJ_14_Days_LSTM.png')
s3.upload_file('../img/Predictions/JNJ_30_Days_LSTM.png',
               'web-app-storage',
               'JNJ_30_Days_LSTM.png')
s3.upload_file('../img/Predictions/MSFT_7_Days_LSTM.png',
               'web-app-storage',
               'MSFT_7_Days_LSTM.png')
s3.upload_file('../img/Predictions/MSFT_14_Days_LSTM.png',
               'web-app-storage',
               'MSFT_14_Days_LSTM.png')
s3.upload_file('../img/Predictions/MSFT_30_Days_LSTM.png',
               'web-app-storage',
               'MSFT_30_Days_LSTM.png')

# Upload Prophet predictions
s3.upload_file('../img/Predictions/AAPL_7_Days_Prophet.png',
               'web-app-storage',
               'AAPL_7_Days_Prophet.png')
s3.upload_file('../img/Predictions/AAPL_14_Days_Prophet.png',
               'web-app-storage',
               'AAPL_14_Days_Prophet.png')
s3.upload_file('../img/Predictions/AAPL_30_Days_Prophet.png',
               'web-app-storage',
               'AAPL_30_Days_Prophet.png')
s3.upload_file('../img/Predictions/AMZN_7_Days_Prophet.png',
               'web-app-storage',
               'AMZN_7_Days_Prophet.png')
s3.upload_file('../img/Predictions/AMZN_14_Days_Prophet.png',
               'web-app-storage',
               'AMZN_14_Days_Prophet.png')
s3.upload_file('../img/Predictions/AMZN_30_Days_Prophet.png',
               'web-app-storage',
               'AMZN_30_Days_Prophet.png')
s3.upload_file('../img/Predictions/GOOGL_7_Days_Prophet.png',
               'web-app-storage',
               'GOOGL_7_Days_Prophet.png')
s3.upload_file('../img/Predictions/GOOGL_14_Days_Prophet.png',
               'web-app-storage',
               'GOOGL_14_Days_Prophet.png')
s3.upload_file('../img/Predictions/GOOGL_30_Days_Prophet.png',
               'web-app-storage',
               'GOOGL_30_Days_Prophet.png')
s3.upload_file('../img/Predictions/JNJ_7_Days_Prophet.png',
               'web-app-storage',
               'JNJ_7_Days_Prophet.png')
s3.upload_file('../img/Predictions/JNJ_14_Days_Prophet.png',
               'web-app-storage',
               'JNJ_14_Days_Prophet.png')
s3.upload_file('../img/Predictions/JNJ_30_Days_Prophet.png',
               'web-app-storage',
               'JNJ_30_Days_Prophet.png')
s3.upload_file('../img/Predictions/MSFT_7_Days_Prophet.png',
               'web-app-storage',
               'MSFT_7_Days_Prophet.png')
s3.upload_file('../img/Predictions/MSFT_14_Days_Prophet.png',
               'web-app-storage',
               'MSFT_14_Days_Prophet.png')
s3.upload_file('../img/Predictions/MSFT_30_Days_Prophet.png',
               'web-app-storage',
               'MSFT_30_Days_Prophet.png')
