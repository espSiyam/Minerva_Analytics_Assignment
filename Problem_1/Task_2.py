import json
from tqdm import tqdm

# Opening first JSON file
f = open('Copy of vehiclePosition01.json')
data = json.load(f)

pointIds = [] # Where we store all the point_id found in two json files

try:
    for i in range(len(data['data'])):
        for j in range(len(data['data'][i]['Responses'])):
            for k in range(len(data['data'][i]['Responses'][j]['lines'])):
                for l in range(len(data['data'][i]['Responses'][j]['lines'][k]["vehiclePositions"])):
                    pointId = data['data'][i]['Responses'][j]['lines'][k]["vehiclePositions"][l]["pointId"]
                    pointIds.append(pointId) # Appending the point id to check with stop_id in stop_time.txt
except:
    pass

# Opening second JSON file
f = open('Copy of vehiclePosition02.json')
data = json.load(f)

try:
    for i in range(len(data['data'])):
        for j in range(len(data['data'][i]['Responses'])):
            for k in range(len(data['data'][i]['Responses'][j]['lines'])):
                for l in range(len(data['data'][i]['Responses'][j]['lines'][k]["vehiclePositions"])):
                    pointId = data['data'][i]['Responses'][j]['lines'][k]["vehiclePositions"][l]["pointId"]
                    pointIds.append(pointId) # Appending from second JSON too
except:
    pass

# Loading the stop_times.txt as csv
import pandas as pd
dataframe = pd.read_csv("stop_times.txt")

not_found = [] # List of items which vehicles id is not found

for i in tqdm(range(len(dataframe))):
    if dataframe['stop_id'].iloc[i] not in pointIds: # if doens't exist in pointIds, then missing in json files
        not_found.append(dataframe['stop_id'].iloc[i])

# First 10 not found vehicle_id
print(not_found[:10])