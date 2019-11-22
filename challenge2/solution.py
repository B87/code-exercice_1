import pandas as pd
import datetime
import os


df = pd.read_csv(os.path.dirname(__file__) + '/Events.csv')
event_ts_format = '%Y-%m-%d %H:%M:%S'
sorted_df = df.sort_values('timestamp')
result_rows = []

for i in range(len(sorted_df)):
    current  = sorted_df.iloc[i]
    current_event = current['EventName']

    if current_event == 'EventRead' and i < len(sorted_df)-1:
        next = sorted_df.iloc[i+1]
        init_ts  = datetime.datetime.strptime(current['timestamp'], event_ts_format)
        end_ts = datetime.datetime.strptime(next['timestamp'], event_ts_format)
        ts_delta = (end_ts - init_ts).total_seconds()
        page_num = current['CustomField_PageNum']
        pub_id = current['CustomField_PublicationId']
        result_rows.append([pub_id, page_num, ts_delta])

result = pd.DataFrame(result_rows, columns = ['CustomField_PublicationId', 'CustomField_PageNum', 'ReadTime_sec'])

result.to_csv(os.path.dirname(__file__) + '/result.csv', index = False)