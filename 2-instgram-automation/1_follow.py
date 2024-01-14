


'''
depdancey: pip install instabot
'''

from instabot import Bot

bot =Bot()  #using Bot finction we can can call the mothe method

if bot.login(username="amarthonge", password="******"):
    print("Login successful!")
else:
    print("Login failed. Check your credentials or handle the failure appropriately.")
bot.follow('code_8055')


