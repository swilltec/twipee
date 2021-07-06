import csv
import re
from datetime import datetime



date = '12/28/2017 7:38:50'


def convert_timestamp_str_to_datetime(date: str) -> datetime:
    """
    Convert timestamp in string to datetime format

    Parameters
    ----------
    date : str
        timestamp to be converted.

    Returns
    -------
    datetime
        converted datetime object

    """
    return datetime.strptime(date, "%m/%d/%Y %H:%M:%S")


def find_all_urls(text: str) -> list:
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', 
                                  elem["Python Tip:"])
    



def load_tweets(data_path: str, last_entry_date: datetime = None) -> None:
    """Read tweets information from a CSV file.

    Params:
        data_path: A path to a CSV file containing tweets data
        last_entry_date: Date of last saved entry
    """

    with open(data_path, 'r') as infile:
        reader = csv.DictReader(infile)
        
        for elem in reader:
            if last_entry_date > convert_timestamp_str_to_datetime(
                    elem.get('Timestamp')
                    ):
                urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', 
                                  elem["Python Tip:"])
                test=re.sub('http[s]?://\S+', '', elem["Python Tip:"])

                params = {
                    'timestamp': elem["Timestamp"],
                    'tip': elem["Python Tip:"],
                    'name': elem["Your name or Twitter id:"],
                    'Your email': elem["Your email:"]
                }
                print(test)

            
            
    

load_tweets('../../data/python_daily_tips.csv', convert_timestamp_str_to_datetime(
    date))