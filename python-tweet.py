import tweepy

consumer_key = 'dRzzqvP2ronqIe3lSiOHg3hLC'
consumer_secret = '3Qw3dffDyUHPRirNgBzmNMjTIAmuoXTf3Y5y6mpvNixPHu9h6C'
access_token = '1163471772722847748-7IiOpJNJMCg9EQiKTX2eD4ihdMpmLc'
access_token_secret = 'xelpYWILujObf4Ec5zTN2FS80ANxpQgqe1DBzrbWLVJRy'

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = OAuth()
api = tweepy.API(oauth)

tweet = raw_input('Tweet: ')
check = raw_input('Are you sure you want to tweet "' + tweet + '"(y/N)')
if check == 'y':
    api.update_status(tweet)
    print('a tweet has been posted')
