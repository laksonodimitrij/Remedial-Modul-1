"""
Title         : find_short.py
Source        : Module 1 Remed Purwadhika no.1

Summary       : Buatlah suatu fungsi yang mengembalikan panjang terpendek dari suatu string kata 
                yang terpisahkan oleh spasi (20 Point)

Feat Req      : Note: Kembalikan panjang dari kata yang terpendek, bukan katanya yang dikembalikan

                
"""

def find_short(x):
    pecah = x.split()                                       # First split the strings into each element
    baru = min(len(ele) for ele in pecah)                   # Create variabel to store the value of the minimum length inside the sentence by checking each one of them with for loop
    return baru                                             # Return the value of the length.

print(find_short('Many people get up early in the morning'))

