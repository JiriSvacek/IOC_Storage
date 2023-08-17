from src.scraping import urlhaus_abuse_data, reputation_alienvault_data, openphish_data
from src.db_model import MyDB
import configparser


def get_db_credentials() -> tuple:
    config = configparser.ConfigParser()
    config.read('config.ini')
    database = config['DATABASE']
    return database['host'], int(database["port"]), database['database'], database['user'], database['password']


if __name__ == "__main__":
    db = MyDB(*get_db_credentials())

    db.insert_data_to_urls(urlhaus_abuse_data(), "UrlHaus Abuse")
    db.insert_data_to_ip_addresses(reputation_alienvault_data(), "Reputation AlienVault")
    db.insert_data_to_urls(openphish_data(), "OpenPhish")

    db.curs.close()
    print("Done")
