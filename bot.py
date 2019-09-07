"""
    Example script that will be executed everyday by Travis-CI.

    
    This script take my likers who don't follow me and like them. 
"""


import os
import time
import random
from instabot import Bot
from tqdm import tqdm


def like_media_likers(bot, media, nlikes=2):
    for user in bot.get_media_likers(media):
        bot.like_user(user, nlikes)
    return True


bot = Bot()
bot.login(
    username=os.getenv("INSTAGRAM_USERNAME"),
    password=os.getenv("INSTAGRAM_PASSWORD"),
)


def like_and_follow(bot, user_id, nlikes=3):
    bot.like_user(user_id, amount=nlikes)
    bot.follow(user_id)
    return True


def like_and_follow_media_likers(bot, media, nlikes=3):
    for user in tqdm(bot.get_media_likers(media), desc="Media likers"):
        like_and_follow(bot, user, nlikes)
        time.sleep(10 + 20 * random.random())
    return True


def like_and_follow_your_feed_likers(bot, nlikes=3):
    bot.logger.info("Starting like_and_follow_your_feed_likers")
    last_media = bot.get_your_medias()[0]
    return like_and_follow_media_likers(bot, last_media, nlikes=nlikes)


like_and_follow_your_feed_likers(bot)
