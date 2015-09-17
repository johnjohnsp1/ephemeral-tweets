# ephemeral-tweets
DESTROY YOUR TWEETS (if you're into that sorta thing)

This script will delete your latest tweet at random time interval.

It will run in the background...until you kill it.

Install python-twitter API wrapper:
pip install python-twitter

Change the "handle" variable to your username.

Change the "count=" value in the statuses variable to delete up to 200 at a time, but be careful of API rate-limiting.

usage: python ephemeral-tweets.py &


