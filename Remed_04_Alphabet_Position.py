"""
Title         : alphabeth_position.py
Source        : Module 1 Remed Purwadhika no.4

Summary       : Buatlah suatu fungsi yang menerima string, dimana setiap huruf di string tersebut digantikan dengan posisinya di urutan alphabet. 
                Bila ada string lain selain huruf alphabet, jangan dihiraukan (30 point).

Feat Req      : 

                
"""

def alphabeth_position(x):
    z = x.lower()                                           # First we lower all the sentences in the string to make it has an universal value
    element = [char for char in z]                          # Then we separate each of its element using list comprehenesion and store it in variable element
    newell = []                                             # Create an empty list to later store the new value later
    alphabetsmol = list('abcdefghijklmnopqrstuvwxyz')       # Create a list of alphabet consists of lower cases
    
    for i in element:                                       # Create a loop to see if every element in element variable, does exist in alphabetsmol
        if i in alphabetsmol:
            newell.append(str(alphabetsmol.index(i)+1))     # If it does, append the word from the index of alphabetsmol plus 1 converted as string, as range always started from 0 while the real alphabet count doesn't start with 0

    return ' '.join(newell)                                 # All of the index number of words from x now are made of lists, as it was asked to be presented as string with different of space for each words and ignoring non-alphabet character


print(alphabeth_position('Have you done your homework?'))