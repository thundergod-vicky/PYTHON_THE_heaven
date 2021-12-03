a = input ("enter a 3 digit number  \n:" )
a = int (a)  #153
b = a/100    #53
b = int (b)  
c = a%100    #1
c = int (c)
d = b*b*b    #1
d = int (d)
e = c/10     #5
e = int (e)
f = c%10     #3
f = int (f)
g = e*e*e    #125
g = int (g)
h = f*f*f    #27
h = int (h)

i = d+h+g    #153
i = int (i) 

if i!= a:
    print ("YOU ARE FUCKING WRONG")
else: 
    print ("you are correct")



