import praw
import datetime


USER_AGENT = "FBoFWBot 1.0 by Tiffany /u/Annabellasimone"

def setup_connection_reddit(subreddit):
    r = praw.Reddit(user_agent = USER_AGENT)
    r.login()
    print("Logging in...")
    subreddit = r.get_subreddit("testingground4bots")
    print("Grabbing subreddit...")
    return subreddit

	
def run_bot():
	
    base_url = "http://fborfw.com/strip_fix/"
    author = "Lynn Johnston"
    name = "for better or for worse"
    title = "Daily FBoFW Comic " + date.today()
    try:
	    reddit_post = api.submit(subreddit, comic.post_title, url=base_url)
	
	
	
while True:
    run_bot()
    time.sleep(86400)