def test_difference_in_SAIS_and_vessel(self):
    # SAIS
    all_real_time_sat_data = pd.read_csv(OUTPUTFILES_DIR / "response_real_time_sat_data.csv")
    columns = ["mmsi", "imo", "latitude", "longitude", "source", "ts_insert_utc", "eeid"]
    filtered_real_time_sat_data = all_real_time_sat_data[columns]
    print(filtered_real_time_sat_data)
    filtered_real_time_sat_data.to_csv(OUTPUTFILES_DIR / "filtered_real_time_sat_data.csv", index=False)
    print("Total Records found:" + str(len(filtered_real_time_sat_data)))

    # Vessels
    with open(OUTPUTFILES_DIR / "response_vessel_api_last.json", "r") as json_fp:
        result = json.load(json_fp)
    nodes_of_vessel_api_df = pd.json_normalize(result['data']['vessels']['nodes'])
    print("Total Records found:" + str(len(nodes_of_vessel_api_df)))
    print("\n\tFor each columns: \n" + str(nodes_of_vessel_api_df.count()))

    # renaming column
    nodes_of_vessel_api_df = nodes_of_vessel_api_df.rename(columns={
        'staticData.mmsi': 'mmsi',
        'staticData.imo': 'graphql_imo',
        'lastPositionUpdate.collectionType': 'graphql_collectionType',
        'lastPositionUpdate.timestamp': 'graphql_timestamp',
        'lastPositionUpdate.latitude': 'graphql_latitude',
        'lastPositionUpdate.longitude': 'graphql_longitude'})

    print("Total Records found:" + str(len(nodes_of_vessel_api_df)))
    print("\n\tFor each columns: \n" + str(nodes_of_vessel_api_df.count()))
    total_record = result["data"]["vessels"]["totalCount"]["value"]
    print("\nTotal Records found from data.vessels.totalCount.value: " + str(total_record))

    unique_values = nodes_of_vessel_api_df.nunique()
    print("\n \t Unique values of each column: \n" + str(unique_values))

    # Merge data
    print("=" * 50)
    print(filtered_real_time_sat_data)
    print("=" * 50)
    print(nodes_of_vessel_api_df)
    print("=" * 50)
    # merge_result = pd.merge(filtered_real_time_sat_data, nodes_of_vessel_api_df)
    merge_result = nodes_of_vessel_api_df.merge(filtered_real_time_sat_data, how='outer', on='mmsi')
    print(merge_result)
    merge_result['latitude_difference'] = merge_result['graphql_latitude'] - merge_result['latitude']
    merge_result['longitude_difference'] = merge_result['graphql_longitude'] - merge_result['longitude']
    merge_result['ts_insert_utc'] = pd.to_datetime(merge_result['ts_insert_utc'], format='%Y%m%d%H%M%S', utc=True)
    merge_result['graphql_timestamp'] = pd.to_datetime(merge_result['graphql_timestamp'], format='%Y-%m-%dT%H:%M:%S')
    merge_result['time_difference'] = merge_result['ts_insert_utc'] - merge_result['graphql_timestamp']

    merge_result = merge_result[['mmsi', 'imo', 'graphql_imo',
                                 'ts_insert_utc', 'graphql_timestamp', 'time_difference',
                                 'graphql_latitude', 'latitude', 'latitude_difference',
                                 'graphql_longitude', 'longitude', 'longitude_difference']]
    # merge_result.to_csv(OUTPUTFILES_DIR / "merged_csv.csv")
    # merge_result.to_csv(OUTPUTFILES_DIR / "time_merged_csv.csv")
    merge_result.to_csv(OUTPUTFILES_DIR / "new_merged_csv.csv")
    print(merge_result)
