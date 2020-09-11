import tweepy
api_key = "rhKW70BWSSRxrt6tuve4B5Su2"

api_secret = "IJwtatttmGoChgDb2c0gRkOZuqOw1t0So11vSFo0BgtHWvzBy3"

access_token = "1304250356436742144-RZaWTSDqz6PVneK5iQ0bYsw2JEGdV3"

access_token_secret = "gbiYGAIrN3KPn84LvRr7OC5Xnvh0fjssmi1M3zXMz5SiO"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

FILE_NAME = "last_seen.txt"


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, "w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return


tweets = api.mentions_timeline(
    read_last_seen(FILE_NAME), tweet_mode='extended')


for tweet in tweets:
    print(str(tweet.id) + ' - ' + tweet.text)
    # if '#awesomebots' in tweet.text.lower():
    #     print(tweet.text)
