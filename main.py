import asyncio, time, csv, os, configparser

from twikit import Client, TooManyRequests
from datetime import datetime
from random import randint

async def login(client, USERNAME, EMAIL, PASSWORD):
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )
    client.save_cookies('cookies.json')

async def get_tweet(client, QUERY, tweet_type, maximum):
    tweet_count = 0
    tweet = None
    
    while tweet_count < maximum:
        try :
            if tweet is None :
                tweet = await client.search_tweet(QUERY, tweet_type)
            else :
                wait_time = randint(5, 10)
                time.sleep(wait_time)
                tweet = await tweet.next()
                
        except TooManyRequests as e :
            wait_time = datetime.fromtimestamp(e.wait_time) - datetime.now()
            time.sleep(wait_time)
            continue
        
        if not tweet:
            break
        
        for t in tweet:
            tweet_count += 1
            tweet_data = [t.id, t.user.name, t.text, t.created_at_datetime, t.reply_count, t.favorite_count,
                          t.view_count, t.quote_count, t.retweet_count, t.reply_to, t.quote, t.retweeted_tweet, t.replies, t.related_tweets, t.hashtags]
            
            with open('tweets.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(tweet_data)
            

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('Config.ini')

    USERNAME = config['Configuration']['username']
    EMAIL = config['Configuration']['email']
    PASSWORD = config['Configuration']['password']
    QUERY = config['Configuration']['query']
    TYPE = config['Configuration']['type_of_tweets']
    LIMIT = int(config['Configuration']['limit'])
    
    client = Client('en-US')
    
    if os.path.exists('cookies.json'):
        client.load_cookies('cookies.json')
    else :
        asyncio.run(login(client, USERNAME, EMAIL, PASSWORD))
    
    if os.path.exists('tweets.csv'):
        asyncio.run(get_tweet(client, QUERY, TYPE, LIMIT))
    else :
        with open('tweets.csv', 'w', newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'username', 'text', 'created_at_datetime', 'reply_count', 'favorite_count',
                          'view_count', 'quote_count', 'retweet_count', 'in_reply_to', 'quote', 'retweeted_tweet', 'replies', 'related_tweets', 'hashtags'])
            
        asyncio.run(get_tweet(client, QUERY, TYPE, LIMIT))