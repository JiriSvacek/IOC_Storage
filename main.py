from src.scraping import urlhaus_abuse_data, reputation_alienvault_data, openphish_data
from configparser import SectionProxy
from src.db_model import MyDB
import configparser
import psycopg2


def get_db_credentials() -> SectionProxy:
    """Parse config file and returns DATABASE section with credentials"""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DATABASE']


def connect_to_database() -> MyDB:
    """Establish connection to the database, if connection fails program will stop."""
    cfg = get_db_credentials()
    print("Connecting to the DB")
    try:
        return MyDB(psycopg2.connect(host=cfg['host'], port=int(cfg['port']), dbname=cfg['database'], user=cfg['user'],
                                     password=cfg['password']))
    except psycopg2.OperationalError as e:
        print("Failed to connect to DB")
        print(e)
        exit()


if __name__ == "__main__":
    db = connect_to_database()
    # Get data and write them to the DB
    db.insert_data_to_urls(urlhaus_abuse_data(), "UrlHaus Abuse")
    db.insert_data_to_ip_addresses(reputation_alienvault_data(), "Reputation AlienVault")
    db.insert_data_to_urls(openphish_data(), "OpenPhish")

    db.curs.close()
    print("Done")
