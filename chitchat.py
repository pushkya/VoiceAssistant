# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 01:29:14 2020

@author: Pushkar
"""
import random
from jarvis import speak, acceptCommand
import pyttsx3
engine = pyttsx3.init()
words = {'who_are_you':{'groups':[['who','are','you']]},
         'how_are_you':{'groups':[['how','are','you']]},
         'who_is_pushkar':{'groups':[['who','is','pushkar']]},
         'toss_coin':{'groups':[['toss','coin','for','me']]},
         'when_were_you_born':{'groups':[['you','born']]},
         'are_you_smart':{'groups':[['smart']]},
         'are_you_human':{'groups':[['human', 'you']]},
         'will_you_marry_me':{'groups':[['marry', 'will','you']]},
         'i_love_you':{'groups':[['love','you']]},
         'How_do_i_look':{'groups':[['i', 'look', 'how']]},
         'undefined':{'groups':[]}}

def who_are_you():
    speak('Hi! my name is black widow, your virtual assistant')

def how_are_you():
    replies = ['I am fine how are you',
               'very energetic feels awesome',
               'hale and hearty']
    speak(random.choice(replies))

def who_is_pushkar():
    replies = ['He is the one who created me',
               'Pushkar is God for me',
               'pushkar is the best person i have ever met',
               'pushkar is way too smart than other guys around',
               'pushkar is the best coder thats why I am working fine']
    speak(random.choice(replies))
    
def toss_coin():
    replies = ['heads', 'tails']
    speak('heads or tails')
    q = acceptCommand()
    s = random.choice(replies)
    if q == s:
        speak('you won its '+ s)
    else:
        speak("you lost its " + s)

def when_were_you_born():
    speak('I was born in the momth of september 2020 when you guys were hit by a pandemic and i came to save you')

def are_you_smart():
    replies = ['way too smart than you think you are',
               'definately more than you are',
               'Sure i am',
               'Who asks such dumb questions to your virtual assistant surely i am']
    speak(random.choices(replies))

def are_you_human():
    replies = ['are you dumb?',
               'no i am not']
    speak(random.choice(replies))
    
def will_you_marry_me():
    replies = ['I surely confirm you will die single',
               'who marries a virtual assistant',
               'are you human idiots',
               'i have no words for the hopeless question you asked']
    speak(random.choice(replies))

def i_love_you():
    replies = ['I surely confirm you will die single',
               'Either you are cheating or you are single',
               'no i dont get lost',
               'i am not born for your shona mona stuff, i am here to make things simpler']
    speak(random.choice(replies))

def How_do_i_look():
    replies = ['kya shahrukh dikh raha hai',
               'kya salman dikh raha hai',
               'handsome brute',
               'you look sexy',
               'kya baap dikh raha hai',
               'porincha chhava',
               'mazha handsome hero']
    speak(random.choice(replies))

def undefined():
    speak('I didnt get you be clear')