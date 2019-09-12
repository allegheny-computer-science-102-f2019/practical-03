#!/usr/bin/env python3
# Date: 13 Sept 2019
# Name:

### TODO: Finish the below functions to approximate roots

def NM2(n, guess):
    print("  Initial values:  n = ",n, "and guess = ",guess)
#end of NM2()

def NM3(n, guess):
    print("  Initial values:  n = ",n, "and guess = ",guess)
#end of NM3()

def NM4(n, guess):
    print("  Initial values:  n = ",n, "and guess = ",guess)
#end of NM4()



### The following code calls the approximation functions and then prints the returned output

# square roots
#################
#get parameters to call function NM()
#get parameters to call function NM()
n = 2 # the number from which to find square root.
guess = 1.0 # initial value for approx
print("\n Finding square root of : ",n)
#print(" Approx guess : ", guess)
print("  Square root result : ",NM2(n, guess))

# cube roots
##################
#get parameters to call function NM()
n = 175616 # the number from which to find square root.
guess = 1.0 # initial value for approx
print("\n Finding cube root of : ",n)
print(" Approx guess : ", guess)
print("  Cube root result : ",NM3(n, guess))

# forth roots
##################
#get parameters to call function NM()
n = 9834496 # the number from which to find square root.
guess = 1.0 # initial value for approx
print("\n Finding forth root of : ",n)
#print(" Approx guess : ", guess)
print("  Forth root result : ",NM4(n, guess))
