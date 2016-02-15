#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import tweepy
import json
import argparse
import argcomplete
import os

if __name__ == "__main__":

    to_follow_f = "to_follow.txt"

    parser = argparse.ArgumentParser(description='Twitter follower')
    parser.add_argument("-t", "--to-follow",
                        help="list of accounts to follow",
                        metavar="FILE",
                        type=argparse.FileType('r'),
                        default=open(to_follow_f)
                                if os.path.exists(to_follow_f) else None)

    parser.add_argument("-s", "--settings-file",
                        help="settings file",
                        metavar="FILE",
                        type=argparse.FileType('r'),
                        default=open("settings.json", "r"))

    parser.add_argument("-c", "--copy-following",
                        help="copy all users the supplied account follows",
                        metavar="Twitter Account",
                        type=str)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    s = json.load(args.settings_file)

    auth = tweepy.OAuthHandler(s['consumer_token'], s['consumer_secret'])
    auth.secure = True
    auth.set_access_token(s['access_token'], s['access_token_secret'])

    api = tweepy.API(auth)

    if(args.copy_following):
        acccount = args.copy_following
        for friend in tweepy.Cursor(api.friends, screen_name=acccount).items():
            try:
                friend.follow()
            except tweepy.TweepError, e:
                print(e)
                continue

    elif(args.to_follow):
        for line in args.to_follow:
            if line[0:2] == '# ':
                continue
            try:
                api.create_friendship(screen_name=line)
            except tweepy.TweepError, e:
                print("Couldn't follow %s" % line)
                print(e)
                continue
    else:
        print("Please pass in the file of users to follow or a user whose"
              " followers to copy")
