import tweepy

# Accessning the account from twitter api

api_key = "xxxxx"
api_key_secret = "xxxxxx"
access_token = "xxxxx"
access_token_secret = "xxxxx"

# Authenticating Api

a = tweepy.OAuthHandler(api_key, api_key_secret)
a.set_access_token(access_token, access_token_secret)

api = tweepy.API(a, wait_on_rate_limit=True)

# using the api for follwing

api.create_friendship('Enter the username to follow')

# using the api for twitting

api.update_status("Write your tweet here")

# Editin the bio of twitter

api.update_profile(description="Write your bio here")
