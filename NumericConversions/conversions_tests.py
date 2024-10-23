# Description: This scipt tests various numeric 
# conversion techniques
#Author: Rodolfo Lopez. Newprogrammer

# defining the following variables
a = "  101.1 " 
b = '55'
c = "402 Stevens"
d = 'Number 5  '

# cast as integar using int()
# a_int = int(a) invalid literal for int()

# cast as float using float()
a_float = float(a.strip()) # removes unneeded spaces
print(a_float, type(a_float)) # output was (101.1 <class 'float'>)

# cast as a float then coverting into an integar

a_float_int = int(float(a.strip())) # used to make into a float then int
print(a_float_int, type(a_float_int)) # output was (101 <class 'int'>)

# cast b as an int 
b_int = int(b) # changes '55' to simply 55
print(b_int, type(b_int)) # shows 55 and it's int type 

