import requests
import csv


def download_data(url: str) -> None or requests:
    """Connects to the selected url and download content"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("Error while connecting:", e)
        return None
    print("Successfully connected to:", url)
    return response.iter_lines()


def url_decorator(url: str):
    """Wraps filter function. Tries to connect to the desired url, then pass data to the filter function"""
    def decorator(func):
        def wrapper() -> list:
            output_data = list()
            # Get data from url
            response = download_data(url)
            if response is not None:
                # Parsing file:
                lines = (line.decode('utf-8') for line in response)
                for row in csv.reader(lines):
                    # Call original filter function
                    data = func(row)
                    if data:
                        output_data.append(data)

            return output_data

        return wrapper

    return decorator


@url_decorator(url="https://urlhaus.abuse.ch/downloads/csv_recent")
def urlhaus_abuse_data(row: list):
    if row and "#" not in row[0]:
        # Adds url, 3rd position in row:
        return row[2]


@url_decorator(url="http://reputation.alienvault.com/reputation.data")
def reputation_alienvault_data(row: list):
    #  1st position in row, string split by "#", desired string in 1st position
    return row[0].split("#")[0]


@url_decorator(url="https://openphish.com/feed.txt")
def openphish_data(row: list):
    return row[0]
