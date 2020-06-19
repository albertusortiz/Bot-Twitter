import tweepy

from keys import keys

import time


SCREEN_NAME = keys['screen_name']
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def users(i):
    for follower in tweepy.Cursor(api.followers).items():
        try:
            # follower.follow()
            # print ("acabo de seguir a ")
            print (follower.screen_name)
            i = i + 1
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

        # time.sleep(50)
    return i

user = api.me()
print(user.name)
print(SCREEN_NAME)
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)

### Seguir a quien me sigue
i = users(0)
print(i)


