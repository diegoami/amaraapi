from amaraapi.amara_video import *
from amaraapi.amara_tools import *

from argparse import *
import argparse
from samples.amara_env import amara_headers

if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument('--videoId')


    args = parser.parse_args()
    amara = AmaraTools(amara_headers)
    amaraVideo = amara.retrieve_video(args.videoId)
    if (amaraVideo):
        subtitles = amaraVideo.get_best_subtitles()
        print(subtitles)