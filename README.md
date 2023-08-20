# IOC storage
Project is focused on downloading urls and ip addresses from three sources: https://urlhaus.abuse.ch/downloads/csv_recent/, http://reputation.alienvault.com/reputation.data, https://openphish.com/feed.txt. After downloading data are pushed to the created Postgresql database tables.

**For run:**
* Install requirements.txt or activate virtual enviroment (venv)
* Update database credentials in config.ini
* run main.py.
