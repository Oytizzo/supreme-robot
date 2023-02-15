import json
import pandas as pd

with open("./vessel_api_last.json", "r") as vessel_api_first_file:
    vessel_api_first = json.load(vessel_api_first_file)

# print(vessel_api_first)
nodes = vessel_api_first['data']['vessels']['nodes']

new_nodes = [{**item.pop('staticData'), **item.pop('lastPositionUpdate')} for item in nodes]
print(new_nodes)
result_dataframe_of_vessel_api = pd.DataFrame(new_nodes)
print(result_dataframe_of_vessel_api)

result_dataframe_of_vessel_api.to_csv('new_vessel_api_last.csv', index=False)


# Can't do that because for static.imo
# nodes = pd.json_normalize(nodes, max_level=5)
# data = pd.DataFrame(nodes)
# print(data)

# # SAIS
real_time_sat_data = pd.read_csv("./real_time_sat_data_response.csv")
print(real_time_sat_data)

columns = ["mmsi", "imo", "latitude", "longitude", "source", "ts_insert_utc", "eeid"]
real_time_sat_data.to_csv('new_real_time_sat_data.csv', columns=columns, index=False)


def compare(vessel_api_df, real_time_sat_df):

    pass
