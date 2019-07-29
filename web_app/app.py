from download import download
from flask import Flask, render_template, request
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

download()


def get_page():
    """
    Revieves data graphs

    Calls download to revieve the graphs form the S3bucket
    """
    download()


scheduler.add_job(get_page, 'cron', hour='5')


@app.route('/')
def home():
    """
    Call functions and model to assess the data recieved and make predidction,
    renders home.html and counts ammount of each risk recieved.
    """
    return render_template('home.html')


@app.route('/graph', methods=['POST'])
def get_data():
    stock = request.form['Stocks']
    days = int(request.form['Days'])
    if stock == 'Apple':
        if days == 7:
            hist = "/static/images/AAPL_historical.png"
            pred = "/static/images/APPL_7.png"
        elif days == 14:
            hist = "/static/images/AAPL_historical.png"
            pred = "/static/images/APPL_14.png"
        else:
            hist = "/static/images/AAPL_historical.png"
            pred = "/static/images/APPL_30.png"
    elif stock == 'Amazon':
        if days == 7:
            hist = "/static/images/AMZN_historical.png"
            pred = "/static/images/AMZN_7.png"
        elif days == 14:
            hist = "/static/images/AMZN_historical.png"
            pred = "/static/images/AMZN_14.png"
        else:
            hist = "/static/images/AMZN_historical.png"
            pred = "/static/images/AMZN_30.png"
    elif stock == 'Google':
        if days == 7:
            hist = "/static/images/GOOGL_historical.png"
            pred = "/static/images/GOOG_7.png"
        elif days == 14:
            hist = "/static/images/GOOGL_historical.png"
            pred = "/static/images/GOOG_14.png"
        else:
            hist = "/static/images/GOOGL_historical.png"
            pred = "/static/images/GOOG_30.png"
    elif stock == 'JNJ':
        if days == 7:
            hist = "/static/images/JNJ_historical.png"
            pred = "/static/images/JNJ_7.png"
        elif days == 14:
            hist = "/static/images/JNJ_historical.png"
            pred = "/static/images/JNJ_14.png"
        else:
            hist = "/static/images/JNJ_historical.png"
            pred = "/static/images/JNJ_30.png"
    else:
        if days == 7:
            hist = "/static/images/MSFT_historical.png"
            pred = "/static/images/MSFT_7.png"
        elif days == 14:
            hist = "/static/images/MSFT_historical.png"
            pred = "/static/images/MSFT_14.png"
        else:
            hist = "/static/images/MSFT_historical.png"
            pred = "/static/images/MSFT_30.png"

    return render_template('graph.html', stock=stock, days=days,
                           hist=hist, pred=pred)


@app.route('/prophet')
def prophet():
    return render_template('prophet.html')


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
