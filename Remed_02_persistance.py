"""
Title         : persistance.py
Source        : Module 1 Remed Purwadhika no.2

Summary       : Buatlah suatu fungsi yang menerima parameter angka positif
                dan mengembalikan total berapa kali harus dikalikan digit dari angka tersebut 
                hingga mencapai 1 digit (20 Point).

Feat Req      : 

                
"""

def persistance(x):
    list1 = map(int,str(x))             # First we need to separate each of the conjuncted numbers into a list of integers
    var1 = 1                            # We then create a variable of 1 for multiplier later
    
    for i in list1:                     # Then we multiply each of the elements inside the list with redefined variable
        var1 = var1 * i

    jumlah = map(int,str(var1))         # now create a variable from previously update multiplication variable
    z = sum(jumlah)                     # create another variable to store the value of total sum of the newly separated multiplied variable
    
    return z                            # return the value

print(persistance(999))