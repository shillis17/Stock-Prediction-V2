from ProphetPrediction import ProhetPrediction
from LSTMPrediction import LSTMPrediction
from gather_data import get_data
from upload import upload
from apscheduler.schedulers.background import BackgroundScheduler

# Turn on scheduler to live steam data in
scheduler = BackgroundScheduler()
scheduler.daemonic = False
scheduler.start()

google, microsoft, apple, jnj, amazon = get_data()

stocks = [['GOOGL', google], ['MSFT', microsoft], ['AAPL', apple],
          ['JNJ', jnj], ['AMZN', amazon]]

days = [7, 14, 30]

count = 0


def make_graphs(stocks, days):
    """
    Make graphs for web app

    Calls scripts to train and graph the models and save the graphs locally.

    Attributes:
        stocks: list of lists containing stock dataframes and names
        days: list of ints of prediction windows.

    Returns:
        None
    """
    for i in stocks:
        for n in days:
            ProhetPrediction(i[1], i[0], n)
            LSTMPrediction(i[1], i[0], n)
    return None


def schedule():
    """
    Holds function that will be called on by APScheduler and repeated
    every 24 hours

    Attributes:
        stocks: list of lists containing stock dataframes and names
        days: list of ints of prediction windows.

    Returns:
        None
    """
    global stocks
    global days
    make_graphs(stocks, days)
    upload()
    global count
    count += 1


# Start scheduler and keep script runnung until not needed
scheduler.add_job(schedule, trigger='cron', hour='23', minute='59')
input("Press enter to exit.")
scheduler.shutdown()
