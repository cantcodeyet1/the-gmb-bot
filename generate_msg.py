import numpy
import random
import pyperclip
from content import generate_content

# A list of the emoji we want to randomize.
emojilist =  '❤️','💕','💞','💓','💗','💖','💘','❣️','❤‍🔥'
emojilist2 = '🌄','💖','🌸','❤️','🥰','😘','☀️','🥰','🥺','❤️','💖','💕','💓','❤️','💘','☺️','🤗','✨'

def generate_msg():
    '''I love you + heart string'''
    global loveString_c

    array = numpy.random.normal(208.2, 41.8,1000)
    x = int(numpy.random.choice(array))

    heart_string = []
    for heart in range(x):
        choice = numpy.random.choice(emojilist)
        heart_string.append(choice)

    print(f"{len(heart_string)} hearts generated")
    loveString_c = f"I love you {''.join(heart_string)}"

    ########################################################

    '''Good morning baby + 3 emojis'''
    global goodMorning_c

    goodMorningBaby = random.sample(emojilist2,3)
    goodMorning_c = f"Good morning baby {''.join(goodMorningBaby)}"

    ########################################################

    '''contents'''
    contents_c = generate_content()

    #outputting
    goodMorningMessage = f"{goodMorning_c} {contents_c} {loveString_c}"
    
    ########################################################
    msg = generate_msg()
    #Using pyperclip to copy the output directly to the clipboard
    pyperclip.copy(msg)
    spam = pyperclip.paste()

    print("Message generated and copied to clipboard.")
    return goodMorningMessage




