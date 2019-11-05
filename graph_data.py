import os
import tweepy

# read file name
path_negative = r'/Users/cui/Downloads/MultiModalDataset/negative/'
path_positive = r'/Users/cui/Downloads/MultiModalDataset/positive/'

name_negative = os.listdir(path_negative)
name_positive = os.listdir(path_positive)


name_negative_dict={}
name_positive_dict={}

# join str
web = 'https://twitter.com/'
consumer_key = 'y0KKe5hy17OGc9fmOtdK24aHN'
consumer_secret = 'K3vpk3vnYFXFuDKGilEvKdOCDsQXay5pim707GMnTUs3VNZRLO'
access_token = '1170009404004954112-WHULqPxRTTw9PYIz027mrQVIxgIlHG'
access_secret = 'xTZhDpkGfzI8SO7b05jfMtbwHMw5OSmJk4In8VxsGcehH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

for name in name_negative:
    try:
        users = api.friends(name, count=200)
        with open(name + '.txt') as file:
            file.write(users)
            file.close()
    except:
        print(name)
    else:
        for user in users:
            user = user.screen_name
            if user not in name_negative_dict.keys():
                name_negative_dict[user] = 1
            else:
                name_negative_dict[user] += 1

for name in name_positive:
    try:
        users = api.friends(name, count=200)
        with open('/dataset/' + name + '.txt') as file:
            file.write(users)
            file.close()
    except:
        print(name)
    else:
        for user in users:
            user = user.screen_name
            if user not in name_positive_dict.keys():
                name_positive_dict[user] = 1
            else:
                name_positive_dict[user] += 1

with open('negative_dict.txt') as file:
    for i in name_negative_dict:
        file.write(i)
        file.write(' ')
        file.write(name_negative_dict[i])
        file.write('\n')
    file.close()


with open('positive_dict.txt') as file:
    for i in name_negative_dict:
        file.write(i)
        file.write(' ')
        file.write(name_positive_dict[i])
        file.write('\n')
    file.close()





