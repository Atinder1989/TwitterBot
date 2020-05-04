import tweepy
import time

CONSUMER_KEY = "pO3Tadti5UnMdIlGEMuJQISWc"
CONSUMER_SECRET = "OHctD556uIPIJ5AqLv5rFDU4iFRDnEkGzzuYNwCH7X25jxTiWm"
ACCESS_KEY = "1255730943676932096-jsGXdsJPOWdnfG53CgAVvYwZGFctuZ"
ACCESS_SECRET = "irARXEelxyKCLFf4UCqFhYiePatkTrFJdNjy24qfQWTSj"

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.txt"

def retrieve_last_seen_id(file_name):
    f_read = open(file_name,"r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id,file_name):
    f_write = open(file_name,"w")
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print("Replying and re-tweeting")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(last_seen_id,tweet_mode="extended")
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id,FILE_NAME)

        if "#helloworld" in mention.full_text.lower():
            print("found Helloworld")
            api.update_status("@" + mention.user.screen_name + "#HelloWorld back to your and it is just a test",mention.id)


while True:
    reply_to_tweets()
    time.sleep(15)
