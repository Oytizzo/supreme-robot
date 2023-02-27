import os
import json
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
api_service_name = "youtube"
api_version = "v3"
api_key = os.environ.get("youtube_api_key_for_scraping")
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)


def get_50_channel_list(max_result: int, order: str, query: str, search_type: str):
    request = youtube.search().list(
        part="snippet",
        maxResults=max_result,
        order=order,
        q=query,
        type=search_type
    )
    response = request.execute()
    # print(response)
    print(len(response['items']))

    channel_names_ids_urls = []
    for item in response['items']:
        channel_name_id_url = f"{item['snippet']['title']} => {item['id']['channelId']} => https://youtube.com/channel/{item['id']['channelId']}"
        channel_names_ids_urls.append(channel_name_id_url)
        print(channel_name_id_url)

    # print(channel_names_ids_urls)
    return channel_names_ids_urls


def get_last_50_uploads_in_channel(channel_id: str, part="contentDetails"):
    response_channel = youtube.channels().list(id=channel_id, part=part).execute()
    response_uploads = youtube.playlistItems().list(playlistId=response_channel['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
                                                    part='snippet',
                                                    maxResults=50).execute()
    return response_uploads


def main():
    channels = get_50_channel_list(max_result=50, order="viewCount", query="hello", search_type="channel")
    uploads = get_last_50_uploads_in_channel(channels[0].split(" => ")[1])
    with open("upload_playlist.json", "w") as f:
        json.dump(uploads, f, indent=4)

    print("End")


if __name__ == "__main__":
    main()
