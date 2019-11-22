import pandas as pd
import datetime
import os
import argparse

def process_events_of_file(input, output):
    df = pd.read_csv(input)
    event_ts_format = '%Y-%m-%d %H:%M:%S'
    sorted_df = df.sort_values('timestamp')
    result_rows = []

    for i in range(len(sorted_df)):
        current  = sorted_df.iloc[i]
        current_event = current['EventName']
        # If current element is read event and we have more elements after it
        if current_event == 'EventRead' and i < len(sorted_df)-1:
            next = sorted_df.iloc[i+1]
            init_ts  = datetime.datetime.strptime(current['timestamp'], event_ts_format)
            end_ts = datetime.datetime.strptime(next['timestamp'], event_ts_format)
            ts_delta = (end_ts - init_ts).total_seconds()
            page_num = current['CustomField_PageNum']
            pub_id = current['CustomField_PublicationId']
            result_rows.append([pub_id, page_num, ts_delta])

    result = pd.DataFrame(result_rows, columns = ['CustomField_PublicationId', 'CustomField_PageNum', 'ReadTime_sec'])
    result.to_csv(output, index = False)

## Execute with something like : python challenge2/solution.py -i ~/Documents/code-exercice_1/challenge2/Events.csv -o ~/Documents/code-exercice_1/challenge2/result.csv

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help= 'Input file path', required= True)
    parser.add_argument('-o', '--output', help= 'Output file path', required= True)
    args = parser.parse_args()

    process_events_of_file(args.input, args.output)