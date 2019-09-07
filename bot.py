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


bot = Bot()
bot.login(
    username=os.getenv("INSTAGRAM_USERNAME"),
    password=os.getenv("INSTAGRAM_PASSWORD"),
)

bot.unfollow_non_followers()
