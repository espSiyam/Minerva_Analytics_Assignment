import os
import json
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from datetime import datetime

# Opening first JSON file
f = open('Copy of vehiclePosition01.json')
data = json.load(f)

## Segregating First json file
for i in tqdm(range(len(data['data']))): # Iterating through all the data of json file
    time = int(data['data'][i]['time']) / 1000 # Converting miliseconds to seconds
    date = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d') # Converting date from seconds
    
    if not os.path.exists(date): # Make directory by the name of the date to export csv for each days
        path = os.path.join("./", date)
        os.mkdir(path)
        
    for j in range(len(data['data'][i]["Responses"])): # Itererting to all responses (Ultimate goal is to find line_id)
        
        try: # There are few missing values. Ignoring them
            for k in range(len(data['data'][i]["Responses"][j])):
                lines = data['data'][i]["Responses"][j]['lines'][k]  # Iterating through all the lines
                dataframe = pd.DataFrame(lines) # Convert line response dict to dataframe
                csv_join = lines["lineId"] + ".csv" # # To save the csv file name by line_id
                file_name = os.path.join(date, str(csv_join))
                dataframe.to_csv(file_name, index=False) # Saving the dataframe
                
        except:
            pass

# Opening Second JSON file
f = open('Copy of vehiclePosition02.json')
data = json.load(f)

for i in tqdm(range(len(data['data']))):
    time = int(data['data'][i]['time']) / 1000
    date = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d')
    if not os.path.exists(date):
        path = os.path.join("./", date)
        os.mkdir(path)
    for j in range(len(data['data'][i]["Responses"])):
        try:
            for k in range(len(data['data'][i]["Responses"][j])):
                lines = data['data'][i]["Responses"][j]['lines'][k]
                dataframe = pd.DataFrame(lines)
                line_id = lines["lineId"]
                csv_join = line_id + ".csv"
                file_name = os.path.join(date, str(csv_join))
                dataframe.to_csv(file_name, index=False)
        except:
            pass