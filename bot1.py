#!/usr/bin/python

import praw
import time
from bs4 import BeautifulSoup
import requests

def get_imageURL(url, div_class):
    #url = url of the website with comic
    #div_class = div class within the url HTML that contains the comic image
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('div', {'class': div_class})
    image_url = [i.find('img')['src'] for i in links]
    image_url += '.jpg'
    new_url = ''.join(map(str, image_url))
    return new_url

def run_bot():
    #log into Reddit
    reddit = praw.Reddit(client_id='enter client id',
            client_secret='enter client secret',
            password='enter password',
            user_agent ='enter user agent',
            username='enter username'
            )
    print("Logging in...")
    #if login was successful, it will display the user name
    print(reddit.user.me())
    #establish subreddit, title, url
    subreddit = 'FBoFW'
    author = "Lynn Johnston"
    name = "for better or for worse"
    title = "Daily FBoFW Comic " + time.strftime("%d/%m/%Y")
    print "Subreddit set to '%s'" % subreddit
    print "Title set to '%s'" % title
    image_url = get_imageURL("http://www.gocomics.com/forbetterorforworse/", "item-comic-container")
    print "URL set to '%s'" % image_url
    #make submission to Reddit
    try:
        reddit.subreddit(subreddit).submit(title, url=image_url)
    except: #display error message if submission was not successful 
        print "Error/Exception"
                        
while True:
    run_bot()
    #only post once a day
    time.sleep(86400)