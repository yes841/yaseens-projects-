# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:29:05 2021

@author: yasee
"""

# Checking validation of passwords
#Validation critera
# At least 1 letter between [a-z]
#At least 1 letter between [A-Z]
#At least 1 number between [0-9]
#At least 1 character from [@#$]
# Minimum length is 6 characters
# Maximum length 16 characters

import re 

p=input("Enter your Password : ")

x = True

while x:
    if (len(p) < 6 or len (p) > 16):
        break
    elif not re.search("[a-z]", p):
        break
    elif not re.search("[A-Z]", p):
        break
    elif not re.search("[0-9]", p):
        break
    elif not re.search("[@#$]", p):
       break
else:
       print("Valid Password : ")
       x = False
       
   
    
if x: 
       print("Not a Valid Password!!!")
       
        