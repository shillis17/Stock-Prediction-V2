# Uploads images to S3 for web app to pull
import boto3

s3 = boto3.client('s3')


def upload():
    """
    uploads images to S3 bucket for web app

    Uses boto3 to upload images from model predictions to S3 for web app
    use
    """
    s3.upload_file('../img/S3/AAPL_historical.png',
                   'web-app-storage',
                   'AAPL_historical.png')
    s3.upload_file('../img/S3/AMZN_historical.png',
                   'web-app-storage',
                   'AMZN_historical.png')
    s3.upload_file('../img/S3/GOOGL_historical.png',
                   'web-app-storage',
                   'GOOGL_historical.png')
    s3.upload_file('../img/S3/JNJ_historical.png',
                   'web-app-storage',
                   'JNJ_historical.png')
    s3.upload_file('../img/S3/MSFT_historical.png',
                   'web-app-storage',
                   'MSFT_historical.png')
    
    helper = [
            ['APPL', 7], ['APPL', 14], ['APPL', 30],
            ['AMZN', 7], ['AMZN', 14], ['AMZN', 30],
            ['GOOG', 7], ['GOOG', 14], ['GOOG', 30],
            ['JNJ', 7], ['JNJ', 14], ['JNJ', 30],
            ['MSFT', 7], ['MSFT', 14], ['MSFT', 30]
            ]
    for i in helper:
        s3.upload_file('../img/S3/' + i[0] + '_' + str(i[1]) + '.png',
                       'web-app-storage',
                       i[0] + '_' + str(i[1]) + '.png')
    