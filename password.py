from math import floor
import random

text_list = ['qwerty', 'cvbnm', 'bangtansoneyodan', 'bts', 'poop', 'asdfgh', 'abcdef', 'password', 'hdljfhljd', 'bndvmnb', 'mnsjdkjs', 'nadfgek', 'memories', 'leonidas', 'cristiano', 'fortnite', 'john']
characters_list = [ '!', '@', '#', '$', '%', '^', '&', '*', '|']

ask_text = input('Any specific text you want to be in the passoword')
ask_numbers = input('Any specific numbers you want to be in the passoword')
ask_characters = input('Any specific characters you want to be in the password')

text = random.choice(text_list)
numbers = random.randint(100, 1000)
characters = random.choice(characters_list)
password = True

if ask_numbers == 'No':
    password = ask_text + str(numbers) + ask_characters
if ask_text == 'No':
    password = text + str(ask_numbers) + ask_characters
if ask_characters == 'No':
    password = ask_text + str(ask_numbers) + characters
    
if ask_characters == 'No' and ask_numbers == 'No':
    password = ask_text + str(numbers) + characters
if ask_text == 'No' and ask_numbers == 'No':
    password = text + str(numbers) + ask_characters
if ask_text == 'No' and ask_characters == 'No':
    password = text + str(ask_numbers) + characters
if ask_text == 'No' and ask_characters == 'No' and ask_numbers == 'No':
    password = text + str(numbers) + characters
if ask_text != 'No' and ask_characters != 'No' and ask_numbers != 'No':
    password = ask_text + str(ask_numbers) + ask_characters
print(password)
