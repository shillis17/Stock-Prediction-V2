# Downloads images to S3 for web app to use
import boto3

s3 = boto3.client('s3')


def download():
    """
    Downloads images from S3 bucket and saves them fore web app

    Uses boto3 to upload images from model predictions to S3 for web app
    use
    """
    helper = [
            ['APPL', 7], ['APPL', 14], ['APPL', 30],
            ['AMZN', 7], ['AMZN', 14], ['AMZN', 30],
            ['GOOG', 7], ['GOOG', 14], ['GOOG', 30],
            ['JNJ', 7], ['JNJ', 14], ['JNJ', 30],
            ['MSFT', 7], ['MSFT', 14], ['MSFT', 30]]
            
    for i in helper:
        s3.download_file('web-app-storage',
                         i[0] + '_' + str(i[1]) + '.png',
                         'static/images/' + i[0] + '_' + str(i[1]) + '.png')
    s3.download_file('web-app-storage',
                     'AAPL_historical.png',
                     'static/images/AAPL_historical.png')
    s3.download_file('web-app-storage',
                     'AMZN_historical.png',
                     'static/images/AMZN_historical.png')
    s3.download_file('web-app-storage',
                     'GOOGL_historical.png',
                     'static/images/GOOGL_historical.png')
    s3.download_file('web-app-storage',
                     'JNJ_historical.png',
                     'static/images/JNJ_historical.png')
    s3.download_file('web-app-storage',
                     'MSFT_historical.png',
                     'static/images/MSFT_historical.png')

