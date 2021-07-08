from apscheduler.schedulers.background import BackgroundScheduler
from .process_csv import load_tweets 


def start_job():
    """ Function to schedule tweet loading
    
    The scheduler can take the following interval(minutes, seconds)
    adjust the int to alter the interval between jobs"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        load_tweets, 'interval', minutes=5)
    scheduler.start()

