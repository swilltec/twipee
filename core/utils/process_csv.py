import csv
import re
from pathlib import Path
from datetime import datetime
import pytz

from core.models import Tweet, Link


def fetch_tweet_csv() -> csv:
    """
    fetch and return csv file


    Returns
    -------
    csv
        converted csv object

    """
    csv_file_path = Path(__file__).resolve(
    ).parent.parent.parent / 'data/python_daily_tips.csv'
    if not Path(csv_file_path).is_file():
        raise FileNotFoundError('No csv was found at this path')
    return csv_file_path


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
    native_time = datetime.strptime(date, "%m/%d/%Y %H:%M:%S")
    return pytz.utc.localize(native_time)


def extract_links_from_tweet(tip: str) -> tuple[list, str]:
    """Extract links from tweet tips

    Parameters
    ----------
    tip : str
        tip to modify

    Returns
    -------
    links, new_tip: tuple
        return a tuple of links and clean tips
    """
    regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    links = re.findall(regex, tip)
    new_tweet = re.sub(regex, '', tip)
    return links, new_tip


def create_tweets(tweet: dict, timestamp: datetime) -> None:
    """Create new tweets and links

    Parameters
    ----------
    timestamp : datetime
        timestamp of tweet
    
    tweet: dict
        dictionary containing tweet body

    Returns
    -------
        None
    """

    links, new_tip = extract_links_from_tweet(
        tweet.get('Python Tip:'))
    new_tweet = Tweet()
    new_tweet.author = tweet.get('Your name or Twitter id:')
    new_tweet.timestamp = timestamp
    new_tweet.tip = new_tip
    new_tweet.save()
    for link in links:
        Link.objects.create(url=link, tweet=new_tweet)


def load_tweets() -> None:
    """Read tweets information from a CSV file."""
    last_entry_date = Tweet.objects.first()
    timestamp = last_entry_date.timestamp if last_entry_date else None
    file = fetch_tweet_csv()

    with open(file, 'r') as infile:
        reader = csv.DictReader(infile)

        for elem in reader:
            converted_timestamp = convert_timestamp_str_to_datetime(
                elem.get('Timestamp'))

            if timestamp:
                if timestamp < converted_timestamp:
                    create_tweets(elem, converted_timestamp)
            else:
                create_tweets(elem, converted_timestamp)
