# New to Twitter?

Mass-follow users by running this script.

You can either:

   * pass a list of users to follow (defaults to to_follow.txt), one user per
   line. Lines starting with `# ` will be ignored
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

See [getting started with tweepy](http://www.compjour.org/tutorials/getting-started-with-tweepy/). Then edit the `settings.json` file:

```.json
{
	"consumer_token": "SAMPLE_TOKEN",
	"consumer_secret": "SAMPLE_SECRET",
	"access_token": "SAMPLE_ACCESS_TOKEN",
	"access_token_secret": "SAMPLE_ACCESS_SECRET"
}
```

# Installation

```.bash
pip install -U -r requirements.txt
```

This will install tweepy module.

# Running the script

```.bash
./follow_users.py
```

or


```.bash
./follow_users.py -c "YOUR FRIEND'S TWITTER"
```

# Other notes

You can find people from LW who are on twitter in this
[thread](http://lesswrong.com/lw/d92/less_wrong_on_twitter/). I saved them in
`LW_accounts.txt`. Execute with

```.bash
./follow_users.py -t LW_accounts.txt
```
