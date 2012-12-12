import urllib
import json
import re

def parser(data):
    tweets = []
    collection = json.loads(data)
    for item in collection:
            tweets.append((dateparse(item['created_at']),item['text']))
    return tweets
   
def dateparse(date):
    match = re.search(r'[\w\s\:]+',str(date))
    return match.group()


def main():
    name = 'pramode_ce'
    count = 10
    url = 'http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s&include_rts=true&exclude_replies=true&count=%d' %(name,count)
    
    request = urllib.urlopen(url)
    tweets = parser(request.read())
    
    for tweet in tweets:
        print tweet[0]+tweet[1]+'\n'
    
main()
