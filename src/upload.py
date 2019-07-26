# Uploads images to S3 for web app to pull
import boto3

s3 = boto3.client('s3')


def upload():
    """
    uploads images to S3 bucket for web app

    Uses boto3 to upload images from model predictions to S3 for web app
    use
    """
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
