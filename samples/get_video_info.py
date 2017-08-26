from amaraapi import Amara

import argparse
from samples.amara_env import amara_headers

if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument('--videoId')

    args = parser.parse_args()
    amara = Amara(amara_headers)
    amara_video = amara.retrieve_video(args.videoId)
    if (amara_video ):
        video_info = amara_video .get_video_info()
        print(video_info )
        languages = amara_video .get_languages()
        print(languages)