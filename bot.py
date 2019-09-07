"""
    Example script that will be executed everyday by Travis-CI.

    
    This script take my likers who don't follow me and like them. 
"""


import os
import time
import random
from instabot import Bot


def like_media_likers(bot, media, nlikes=2):
    for user in bot.get_media_likers(media):
        bot.like_user(user, nlikes)
    return True


comments_file_name = 'comments.txt'
if not os.path.exists(comments_file_name):
    print("Can't find '%s' file." % comments_file_name)
    exit()

bot = Bot(comments_file=comments_file_name)
bot.login(
    username=os.getenv("INSTAGRAM_USERNAME"),
    password=os.getenv("INSTAGRAM_PASSWORD"),
)

hashtags = ['']
for hashtag in hashtags:
    bot.comment_hashtag(hashtag, 100)
bot.logout()
