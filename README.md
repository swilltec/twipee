# Twipee

Twipee is a django application developed for extracting daily python tweets on twitter ran by @karlafej and @simecek, 
This application runs a scheduled job periodically to check and store changes in csv file in the database.


## Models

### Tweet

 timestamp = models.DateTimeField(blank=True, null=True)
    tip = models.TextField()
    author = models.CharField(blank=True, null=True, max_length=10

| Field   | Type             | Description           |
|-----------------|------------------|-------------------         |
| id               | Integar          | The tweet unique identifier |
| tip         | String           | Python daily tip body    |
| timestamp  | Datetime           | Timestamp the tweet was posted on twitter |
| author | String | The author of the tip|


### Link
| Field   | Type             | Description           |
|-----------------|------------------|-------------------         |
| id               | Integar          | The link unique identifier |
| url         | URL           |This is an optional field. It is the url to complete published article if the tip was published  |
| tweet  | ForeignKey           | ForeignKey relationship to tweet object|


## Getting Started
1. Clone the repo
   ```sh
   git clone https://github.com/swilltec/twipee/
   ```
2. Navigate to bookmark directory and run
  ```sh
  make start
  ```
NB: 
Veiw [Makefile](Makefile) for more commands

## Architecture
This project is divided into three layers of presentation, persistence, and actions or rules
is a common pattern. Some variations on this approach are so common, they’ve been
given names. Model-view-controller (MVC) is a way of modeling data for persistence,
providing users with a view into that data, and allowing them to control changes to
that data with some set of actions.

## Technologies
 - [Python](https://www.python.org/)
 - [Sqlite](https://www.sqlite.org/index.html)
 - [Github](https://github.com/)
 - [Django](https://docs.djangoproject.com/en/3.2/)
 - [Apscheduler](https://apscheduler.readthedocs.io/en/latest/)


## Constraints
 -  The app runs in only one instance which is set by '--noreload flag'.
    It keeps Django from starting up a second instance which is the default behavior in debug mode. 
    A second instance would mean all scheduled tasks would fire twice.
 -  The app reads data from a local file to stimulate actual data due to the restriction placed on host country on twitter.
    The [fetch_tweet_csv](core/utils/process_csv.py) function can easily be modified to fetch real time data from twitter easily
