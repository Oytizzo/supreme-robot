import os
import json
import urllib.request
import string
import random

channels_to_extract = 100
API_KEY = os.environ.get("youtube_api_key_for_scraping")  # your api key

while True:

    # random_name = ''.join(random.choice(string.ascii_uppercase) for _ in
    #                       range(random.randint(3, 10)))  # for random name of channel to search
    random_name = "hello"
    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=channel&q={}".format(
        API_KEY, channels_to_extract, random_name)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))
    results_id = {}
    if results['pageInfo']["totalResults"] >= channels_to_extract:  # may return 0 result because is a random name
        break  # when find a result break

for result in results['items']:
    results_id[result['id']['channelId']] = [result["snippet"]["title"],
                                             'https://www.youtube.com/channel/' + result['id'][
                                                 'channelId']]  # get id and link of channel for all result

with open("all_info_channels.json", "w") as f:  # write all info result in a file json
    json.dump(results, f, indent=4)

with open("only_id_channels.json", "w") as f:  # write only id of channels result in a file json
    json.dump(results_id, f, indent=4)

for channelId in results_id.keys():
    print('Link --> https://www.youtube.com/channel/' + channelId)  # link at youtube channel for all result

print(result)