

from instabot import Bot

bot=Bot()

bot.login(username ="tejasthoge" , password="****")

followers = bot.get_user_followers("amar_rajendra_thoge")#it return the list of the followers of respect user name

for follower in followers:
    print(bot.get_user_info(follower))





