from download import download
from flask import Flask, render_template, request
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def get_page():
    """
    Revieves data graphs
    
    Calls download to revieve the graphs form the S3bucket
    """
    download()


scheduler.add_job(get_page, 'cron', hour='1')


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
    if stock.lower() == 'apple':
        if days == 7:
            return render_template('apple7.html')
        elif days == 14:
            return render_template('apple14.html')
        else:
            return render_template('apple30.html')
    elif stock == 'amazon':
        if days == 7:
            return render_template('amazon7.html')
        elif days == 14:
            return render_template('amazon7.html')
        else:
            return render_template('amazon7.html')
    elif stock == 'google':
        if days == 7:
            return render_template('google7.html')
        elif days == 14:
            return render_template('google14.html')
        else:
            return render_template('google30.html')
    elif stock == 'jnj':
        if days == 7:
            return render_template('jnj7.html')
        elif days == 14:
            return render_template('jnj14.html')
        else:
            return render_template('jnj30.html')
    else:
        if days == 7:
            return render_template('microsoft7.html')
        elif days == 14:
            return render_template('microsoft14.html')
        else:
            return render_template('microsoft30.html')
    
    return render_template('graph.html')


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