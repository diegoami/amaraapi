from amaraapi.amara import *
from argparse import *
import argparse
from samples.amara_env import amara_headers

if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument('--videoId')
    parser.add_argument('--language')

    args = parser.parse_args()
    amara = Amara(amara_headers)
    amaraId = amara.get_amara_id("http://www.youtube.com/watch?v="+args.videoId, args.language)
    subtitles = amara.get_subtitles(amaraId , args.language)
    print(subtitles)