import os
import sys
from pymediainfo import MediaInfo


def get_alternate_len(media_info):
    myJson = media_info.to_data()
    myArray = myJson['tracks']
    for track in myArray:
        if track['track_type'] == 'General' or track['track_type'] == 'Video':
            if 'duration' in track:
                return int(track['duration'] / 1000)
    return 0


def get_track_len(file_path):
    global number_of_video_files
    media_info = MediaInfo.parse(file_path)
    for track in media_info.tracks:
        if track.track_type == "Video":
            number_of_video_files += 1
            if type(track.duration) == int:
                len_in_sec = int(track.duration / 1000)
            elif type(track.duration) == str:
                len_in_sec = int(float(track.duration) / 1000)
            else:
                len_in_sec = get_alternate_len(media_info)
                if len_in_sec == 0:
                    print("File path = " + file_path + ", problem in type of track.duration")
            return len_in_sec

    return 0


number_of_video_files = 0
if __name__ == "__main__":
    dir_path = sys.argv[1]
    total_len_in_secs = 0.0
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            total_len_in_secs += get_track_len(os.path.join(root, name))

    hours = int(total_len_in_secs / 3600)
    remainder = total_len_in_secs - (hours * 3600)
    minutes = int(remainder / 60)
    seconds = remainder - (minutes * 60)

    print("Directory: " + dir_path)
    print("Total number of video files is " + str(number_of_video_files))
    print("Length: %d:%02d:%02d" % (hours, minutes, seconds))
