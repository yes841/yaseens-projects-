# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 21:56:10 2021

@author: yasee
"""

#Encryption with python dictonary

my_dict = {"A": "T", "B": "D", "C": "L", "D": "O", "E": "F",
              "F": "A", "G": "G", "H": "J", "I": "K", "J": "R",
              "K": "I", "L": "C", "M": "V", "N": "P", "O": "W",
              "P": "U", "Q": "X", "R": "Y", "S": "B", "T": "E",
              "U": "Z", "V": "Q", "W": "S", "X": "N", "Y": "M",
              "Z": "H"}



message = input("Enter the message :").upper()

encrypted = ""

for letters in message:
    if letters in my_dict:
         encrypted += my_dict[letters]
else:
    encrypted +=letters
    
    
print (encrypted.lower())