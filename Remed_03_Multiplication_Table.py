"""
Title         : multiplication_table.py
Source        : Module 1 Remed Purwadhika no.3

Summary       : Buatlah suatu fungsi yang menerima dimensi dari Rows x Columns, sebagai parameter 
                untuk membuat tabel multipikasi dengan ukuran sesuai dari dimensi yang diberikan 
                dimana setiap value di tabel row berikutnya adalah hasil perkalian value 
                di row pertama dengan row keberapa value tersebut berada (30 point)

Feat Req      : 

                
"""

def multiplication_table(x,y):
    var1=1                                               # Create a default integer 1 variable as a mover of value later
    buffer_i = []                                        # Create a list buffer for the row
    for i in range(x):                                   # loop the row starting until reached the number of x
        buffer_j = []                                    # Create a list buffer for the column
        for j in range(y):                               # loop the row starting until x row then append the value of var1 into column buffer
            buffer_j.append(var1)
            var1 += 1                                    # For every value var1 able to be stored into buffer column, the value got additional one number until all the loop finished
        
        buffer_i.append(' '.join(map(str, buffer_j)))    # append the buffer row with buffer column using join function so it won't come out as list with coma

    return '\n'.join(buffer_i)                           # finally return the joined buffer row with column with adding final break join so the output has breaks for every fulffiled rows

print(multiplication_table(5,3))
