# Description: This scipt tests various numeric 
# conversion techniques
#Author: Rodolfo Lopez. Newprogrammer

# defining the following variables
a = "  101.1 " 
b = '55'
c = "402 Stevens"
d = 'Number 5  '

# cast as integar using int()
# a_int = int(a)   invalid literal for int()

# cast as float using float()
a_float = float(a.strip()) # removes unneeded spaces
print(a_float, type(a_float)) # output was (101.1 <class 'float'>)

# cast as a float then coverting into an integar

a_float_int = int(float(a.strip())) # used to make into a float then int
print(a_float_int, type(a_float_int)) # output was (101 <class 'int'>)

# cast b as an int 
b_int = int(b) # changes '55' to simply 55
print(b_int, type(b_int)) # shows 55 and it's int type 

# extract numeric portion in c and coverting into int 
c_num = int(c[:2]) # isolates 40 from 402 stevens and converts into int 
print(c_num, type(c_num)) # shows 40 (<class 'int'>)

# stripping of d 
d_trim = d.strip() # removing the space between 'Number 5 '
print(d_trim, type(d_trim)) # shows (Number 5 <class 'str'>)

# or you can 
d_trim = int(d.strip().split()[1]) # used to split number 5 into just 5
print(d_trim, type(d_trim)) # shows 5 ( 5 <class 'str'>)