#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ASSIGNMENT FOR PROGRAMMING: INTERMEDIATE


# In[2]:


#ITEM NUMBER ONE

def shift_letter(letter, shift):

    letter_set =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0 #for finding the letter to begin with

    
    for i in letter_set: 
        if i == letter: #if i is already the starting letter, there will be no more need to shift and thus, it stays the same
            break
        count = count + 1 #if i is not yet the starting letter, the count will add by one every time until index or i matches the letter
        if count == 26: 
            return letter #if it cannot find the character from letter_set, reaching index 26, it just returns the character inputted
   
    resultingletter = (count+shift)%26 #formula for finding the shifted letter, %26 is to wrap it around the 26 letters, will be called on in the following blocks of code
    
    if count+shift > 26: #if the letter index and the number of times its being asked to shift is greater than the list of letters, it performs the next line of code
        return letter_set [resultingletter] #performs the formula for resultingletter as seen above and returns that value
    return letter_set[resultingletter]

print("The resulting letter is " + shift_letter("Z", 1))


# In[3]:


#ITEM NUMBER TWO

def shift_letter(letter, shift):
    letter_set =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    
    for i in letter_set: 
        if i == letter: #if i is already the starting letter, there will be no more need to shift and thus, it stays the same
            break
        count = count + 1 #if i is not yet the starting letter, the count will add by one every time until index or i matches the letter
        if count == 26: 
            return letter #if it cannot find the character from letter_set, reaching index 26, it just returns the character inputted
   
    resultingletter = (count+shift)%26 #formula for finding the shifted letter, %26 is to wrap it around the 26 letters, will be called on in the following blocks of code
    
    if count+shift > 26: #if the letter index and the number of times its being asked to shift is greater than the list of letters, it performs the next line of code
        return letter_set [resultingletter] #performs the formula for resultingletter as seen above and returns that value
    return letter_set[resultingletter]

def caesar_cipher(message, shift): #the first block of code above takes care of shifting individual letters, while this takes care of shifting the entire message
    resultingmessage = ""
    for i in message: #for the index of every letter in the message, it performs the next line
        resultingmessage = resultingmessage + shift_letter(i, shift)  #the index of each letter of the message is shifted using the shift_letter function, where the index is the starting letter
    return resultingmessage #returns the resulting message 

print("The resulting message is " + caesar_cipher("CHECKS OVER STRIPES", 2))


# In[19]:


#ITEM NUMBER THREE

def shift_letter(letter, shift):
    letter_set =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    
    for i in letter_set: 
        if i == letter: #if i is already the starting letter, there will be no more need to shift and thus, it stays the same
            break
        count = count + 1 #if i is not yet the starting letter, the count will add by one every time until index or i matches the letter
        if count == 26: 
            return letter #if it cannot find the character from letter_set, reaching index 26, it just returns the character inputted
   
    resultingletter = (count+shift)%26 #formula for finding the shifted letter, %26 is to wrap it around the 26 letters, will be called on in the following blocks of code
    
    if count+shift > 26: #if the letter index and the number of times its being asked to shift is greater than the list of letters, it performs the next line of code
        return letter_set [resultingletter] #performs the formula for resultingletter as seen above and returns that value
    return letter_set[resultingletter]

def shift_by_letter(letter, letter_shift):
    letter_settwo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    for i in letter_settwo:  #finds the index value of the inputted letter_shift in the second letter set
        if i == letter_shift: #once found, it returns the following line of code
            return shift_letter(letter, count) #returns the shifted letter value starting with the inputted letter and then the index value of the other letter found by the count
        count = count + 1 #does this if second letter is not yet found and until it is found

print("The resulting letter is " + shift_by_letter("B", "K"))


# In[4]:


#ITEM NUMBER FOUR

def vigenere_cipher(message, key):
    letter_set =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #the set of letters for this part of the code
    vigenerekey = " "
    
    for char in message: # for each character in the inputted message, the following lines of code are performed
        if len(key) == len(message):
            if char != " ":
                message_character = message.find(char) #finds each of the characters of the message
                analog_character = key[message_character] #finds the analogous characters of the key
                key_character = letter_set.find(analog_character) #finds where each character of the key lies 
                vigenerekey += letter_set[(letter_set.find(char) + key_character) % 26] #gets the ciphered message
            else:
                vigenerekey += " "
        elif len(message) > len(key):
            remainder = len(message)%len(key) #gets the number of characters that need to be filled up for the new key
            newkey = (key*int(len(message)/len(key))) + key[:remainder] #fills up the remaining characters of the message so that the key will be of the same length as the message
            if char != " ":
                message_character = message.find(char) #finds each of the characters of the message
                analog_character = newkey[message_character] #finds the analogous characters of the key
                key_character = letter_set.find(analog_character) #finds where each character of the key lies 
                vigenerekey += letter_set[(letter_set.find(char) + key_character) % 26] #gets the ciphered message
            else:
                vigenerekey += " "
       
    return vigenerekey

print(vigenere_cipher("A C", "KEY"))


# In[18]:


#ITEM NUMBER FIVE

def scytale_cipher(message, shift):
    
    underscore = "_"
    formedmessage = ""
    
    if len(message) % shift == 0: #if the length of the message gets a remainder of 0 when divided by shift, it performs the following lines
        for i in range(len(message)):
            index = (i // shift) + (len(message) // shift) * (i % shift) #the given formula
            formedmessage += message[index]
            
    elif len(message) % shift != 0: #if the length of the message does not get a remainder of 0 when divided by shift, it performs the following lines
        message += underscore * int(shift - (len(message) % shift)) #for adding underscores at the end of the message until the length of the message is a multiple of shift
        for i in range(len(message)):
            index = (i // shift) + (len(message) // shift) * (i % shift) #same as above
            formedmessage += message[index]
    else:
        print("An error has occured.") #if an invalid character was inputted
        
    return formedmessage
    
print(scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8))


# In[10]:


#ITEM NUMBER SIX

def scytale_decipher(message, shift):
    
    decipheredmessage = "" #to contain the deciphered message of that which is about to be deciphered
    
    for i in range(len(message)):
        index = (i // (len(message) // shift)) + (len(message) // (len(message) // shift)) * (i % (len(message) // shift)) #for deciphering the message
        decipheredmessage += message[index] 
    return decipheredmessage
    

print(scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8))

