# New to Twitter?

Mass-follow users by running this script.

You can either:

   * pass a list of users to follow (defaults to to_follow.txt), one user per
   line
   * follow everyone a certain account follows

```.bash
usage: follow_users.py [-h] [-t FILE] [-s FILE] [-c Twitter Account]

Twitter follower

optional arguments:
  -h, --help            show this help message and exit
  -t FILE, --to-follow FILE
                        list of accounts to follow
  -s FILE, --settings-file FILE
                        settings file
  -c Twitter Account, --copy-following Twitter Account
                        copy all users the supplied account follows
```

# Obtaining the token

See [getting started with tweepy](http://www.compjour.org/tutorials/getting-started-with-tweepy/)

# Installation

```.bash
pip install -U -r requirements.txt
```

# Running the script

```.bash
./follow_users.py
```
