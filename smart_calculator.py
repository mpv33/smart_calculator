import my_module
import sys
sys.path.append('/my_module/')
from my_module.sc_math import *
        
print('--------------'+response[0]+'------------')
print('--------------'+response[1]+'--------------------')

a=input('what is your name :: ')

while True:
    print()
    text=input('Enter your queries:  ')
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_from_text(text)
                r=operations[word.upper()] (l[0],l[1])
                print(r)
            except:
                print('something went wrong going plz enter again !!!!! ')
            finally:
                      break
        elif word.upper() in commands.keys():
                      commands[word.upper()]()
                      break
    else:
        
        sorry()
        
