#----------Data type---------- 
#String "test"
"Hello"[4]

#Integer 100_000_000
print(10+20)

# Float : 1.2
print(1.3+2.3)

#Boolean : True or False


#------------Funcations------------------
num_char=len(input("What is your name?"))
# type() : is to check a Type of veriabel
type(num_char) # Integer

# connverting a veriabel on ather Datatype
str(num_char)   # Now is a String

float(num_char) # float 

int(num_char)   # Integer

# round() : 1.3 = 1
round(3/2) # 1
# //
print(3 // 2) # 1 type of than is Integer
# User scores a point 
score=0
score+=1
#f-String !!!
f"your scores is {score}"
#--------Exercise---------
two_digit_number=input("Type a two digit number: ")
print(int(two_digit_number[1])+int(two_digit_number[0]))
# PEMDAS
# parenthese        (2 + 2)
# Exponents         2 ** 2
# Multiplication    2 * 2
# Division          2 / 2
# Addition          2 + 2
# Subtraction       2 + 2

print(2*2+2/3-3**3)

print((2*(2+2)/(3-3))**3)

#--------Ex1------
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=int(weight)/(float(height)**2)
print(int(bmi))

#-------Ex2-------