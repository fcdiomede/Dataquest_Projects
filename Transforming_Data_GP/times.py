import read
import pandas as pd
import dateutil
import datetime
import read

data = read.load_data()

def datetimes(timestamp):
    sub_time = dateutil.parser.parse(timestamp)
    return sub_time.hour
data['hour'] = data['submission_time'].apply(datetimes)
print(data['hour'].value_counts().head())