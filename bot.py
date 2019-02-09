from instagram_private_api import Client, ClientCompatPatch
from random import randint
from time import sleep
import requests

user_name = 'insta-user'
password = 'insta-pass'
my_user_id = "123456"

blacklist = []

print "getting media id"
media_url = 'https://www.instagram.com/p/ags90jgs90a/'
req = requests.get('https://api.instagram.com/oembed/?url={}'.format(media_url))
media_id_sorteio = req.json()['media_id']

print "media id:", media_id_sorteio

print "getting client"
api = Client(user_name, password)
rank_token = Client.generate_uuid()

print "client ok"

possibles = []

print "getting following users"
following_usernames = ['user1', 'user2']

print "followers ok"

erro = False
while(len(blacklist) < len(following_usernames)):
    try:
        for follower in following_usernames:
            if follower not in blacklist:
                if not erro:
                    delay = randint(0, 5)+randint(0,10)*0.1
                    sleep(delay)
        
                comment = '@'+follower
                api.post_comment(media_id_sorteio, comment)
                blacklist.append(follower)
                erro = False
                print len(blacklist), comment, delay

    except:
        print "Erro"
        erro = True
    

#for result in results['feed_items']:
#    if 'media_or_ad' in result.keys():
#        if 'sorteio' in result['media_or_ad']['caption']['text']:
#            possibles.append(result)

#for possible in possibles:
#    api.post_comment(possibles['media_or_ad']['caption']['media_id'], 'pessoa')
