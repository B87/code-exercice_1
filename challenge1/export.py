import argparse
import requests
import datetime
import pandas as pd
from pandas.io.json import json_normalize
import json


def generate_urls_for_a_day(date):
    base_url = 'https://api.localytic.cm/v1/exports/analytics/logs/{}/{}/{}/{}'
    result = []
    for i in range(0, 24):
        result.append(base_url.format(date.year, date.month, date.day, str(i).zfill(2)))
    return result

# Can't use this function beacause I don't have access to the real api
def request_files(urls):
    result = []
    for url in urls:
        result.append(requests.get(url, allow_redirects=True).json())
    return result

# Using this mock response for test purposes insead
def request_files_mock(urls):
    return [
        '{"menu": {"id": "file","value": "File","popup": {"menuitem": [{"value": "New", "onclick": "CreateNewDoc()"},{"value": "Open", "onclick": "OpenDoc()"},{"value": "Close", "onclick": "CloseDoc()"}]}}}',
        '{"menu": {"id": "file","value": "File","popup": {"menuitem": [{"value": "New", "onclick": "CreateNewDoc()"},{"value": "Open", "onclick": "OpenDoc()"},{"value": "Close", "onclick": "CloseDoc()"}]}}}',
        '{"menu": {"id": "file","value": "File","popup": {"menuitem": [{"value": "New", "onclick": "CreateNewDoc()"},{"value": "Open", "onclick": "OpenDoc()"},{"value": "Close", "onclick": "CloseDoc()"}]}}}'
    ]

def merge_into_df(files):
    dataframes = []
    for file in files: 
        dataframes.append(json_normalize(json.loads(file)))
    return pd.concat(dataframes, ignore_index=True)


## Execute with something like : python challenge1/export.py -d 2019-12-12 -o ~/Documents/code-exercice_1/challenge1/result.csv
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date', help= 'Date to extract', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), required= True)
    parser.add_argument('-o', '--output', help= 'Result file path', required= True)
    
    args = parser.parse_args()
    urls = generate_urls_for_a_day(args.date)
    content = request_files_mock(urls)
    df = merge_into_df(content)
    df.to_csv(args.output, index = False)

    