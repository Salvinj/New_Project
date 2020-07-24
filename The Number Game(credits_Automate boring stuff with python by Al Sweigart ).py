#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This is guess The Number Game.

import random

print('Hello. what is your name?')
name=input()

print('Well,'+name+',I am thinking of a number between 1 and 20.')
secretNumber=random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess=int(input())
    
    if guess<secretNumber:
        print('your guess is too low.')
    elif guess>secretNumber:
        print('your guess is too High.')
    else:
        break #This condition is for correct guess!
        
if guess==secretNumber:
    print('Good Job,'+name+'!You guessed my number in'+" "+'str(guessesTaken)'+" "+'guesses.')
else:
    print('Nope.The number i was thinking was'+" "+str(secretNumber))
        


# In[ ]:


#This is guess My Age Game.Minor edits to the Above code.

import random
from datetime import date 

print('Hello. what is your name?')
name=input()

print('Well,'+name+',Can you guess my Age,its between 20 and 35.')
birthDate=date(1992,9,10)
secretNumber=int((date.today() - birthDate).days/365.2425)

for guessesTaken in range(1,4):
    print('Take a guess.')
    guess=int(input())
    
    if guess<secretNumber:
        print('your guess is too low.')
    elif guess>secretNumber:
        print('your guess is too High.')
    else:
        break #This condition is for correct guess!
        
if guess==secretNumber:
    print('Good Job,'+name+'!You guessed my Age in' +" "+ str(guessesTaken) +" "+ 'guesses.')
else:
    print('Nope.My Age is'+' '+str(secretNumber))
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




