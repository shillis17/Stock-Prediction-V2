# Downloads images to S3 for web app to use
import boto3

s3 = boto3.client('s3')


def download():
    """
    Downloads images from S3 bucket and saves them fore web app

    Uses boto3 to upload images from model predictions to S3 for web app
    use
    """
    s3.download_file('web-app-storage',
                     'AAPL_7_Days_LSTM.png',
                     'static/images/LSTM/AAPL_7_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'AAPL_14_Days_LSTM.png',
                     'static/images/LSTM/AAPL_14_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'AAPL_30_Days_LSTM.png',
                     'static/images/LSTM/AAPL_30_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'AMZN_7_Days_LSTM.png',
                     'static/images/LSTM/AMZN_7_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'AMZN_14_Days_LSTM.png',
                     'static/images/LSTM/AMZN_14_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'AMZN_30_Days_LSTM.png',
                     'static/images/LSTM/AMZN_30_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'GOOGL_7_Days_LSTM.png',
                     'static/images/LSTM/GOOGL_7_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'GOOGL_14_Days_LSTM.png',
                     'static/images/LSTM/GOOGL_14_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'GOOGL_30_Days_LSTM.png',
                     'static/images/LSTM/GOOGL_30_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'JNJ_7_Days_LSTM.png',
                     'static/images/LSTM/JNJ_7_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'JNJ_14_Days_LSTM.png',
                     'static/images/LSTM/JNJ_14_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'JNJ_30_Days_LSTM.png',
                     'static/images/LSTM/JNJ_3pp 0_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'MSFT_7_Days_LSTM.png',
                     'static/images/LSTM/MSFT_7_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'MSFT_14_Days_LSTM.png',
                     'static/images/LSTM/MSFT_14_Days_LSTM.png')
    s3.download_file('web-app-storage',
                     'MSFT_30_Days_LSTM.png',
                     'static/images/LSTM/MSFT_30_Days_LSTM.png')

    s3.download_file('web-app-storage',
                     'AAPL_7_Days_Prophet.png',
                     'static/images/Prophet/AAPL_7_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'AAPL_14_Days_Prophet.png',
                     'static/images/Prophet/AAPL_14_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'AAPL_30_Days_Prophet.png',
                     'static/images/Prophet/AAPL_30_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'AMZN_7_Days_Prophet.png',
                     'static/images/Prophet/AMZN_7_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'AMZN_14_Days_Prophet.png',
                     'static/images/Prophet/AMZN_14_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'AMZN_30_Days_Prophet.png',
                     'static/images/Prophet/AMZN_30_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'GOOGL_7_Days_Prophet.png',
                     'static/images/Prophet/GOOGL_7_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'GOOGL_14_Days_Prophet.png',
                     'static/images/Prophet/GOOGL_14_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'GOOGL_30_Days_Prophet.png',
                     'static/images/Prophet/GOOGL_30_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'JNJ_7_Days_Prophet.png',
                     'static/images/Prophet/JNJ_7_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'JNJ_14_Days_Prophet.png',
                     'static/images/Prophet/JNJ_14_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'JNJ_30_Days_Prophet.png',
                     'static/images/Prophet/JNJ_30_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'MSFT_7_Days_Prophet.png',
                     'static/images/Prophet/MSFT_7_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'MSFT_14_Days_Prophet.png',
                     'static/images/Prophet/MSFT_14_Days_Prophet.png')
    s3.download_file('web-app-storage',
                     'MSFT_30_Days_Prophet.png',
                     'static/images/Prophet/MSFT_30_Days_Prophet.png')
