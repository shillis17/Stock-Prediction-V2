from build_plots import build_plots
from upload import upload
from apscheduler.schedulers.background import BackgroundScheduler

# Turn on scheduler to live steam data in
scheduler = BackgroundScheduler()
scheduler.daemonic = False
scheduler.start()


def make_graphs():
    """
    Make graphs for web app

    Calls scripts to train and graph the models and save the graphs locally.

    Attributes:
        stocks: list of lists containing stock dataframes and names
        days: list of ints of prediction windows.

    Returns:
        None
    """
    build_plots()
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
    make_graphs()
    upload()

schedule()
# Start scheduler and keep script runnung until not needed
scheduler.add_job(schedule, trigger='cron', hour='23')
input("Press enter to exit.")
scheduler.shutdown()
