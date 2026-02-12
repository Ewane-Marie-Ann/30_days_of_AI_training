#day 1 
print('Hello AI world')

#Day 2: Learned variables & data types. Built my first interactive Python script 
name=input('what is your name? ')
age=int(input('Input your age please!'))
print(f'\n Greetings {name}, you are {age}years old.') #f means print after and \n means go to the next line

#Day 3: Learned decision-making in Python. Code now thinks logically 
#Build a grade checker
score=int(input('\n Enter score please!'))
if score>= 18:
	print('EXCELENT')
elif score >= 16:
	print('upper credit')
elif score>=14: 
	print('lower credit')
elif score>=10:
	print('AVERAGE')
elif score <=9:
	print('Below AVERAGE')

#Build a password checker
password=input('\nEnter your password please!')
con_password=input('\n Confirm password!')
if password  == con_password:
	print('your password is correct!')
elif  password  != con_password:
	print ('password incorrect try again')

#day 4  Loops (Automation Begins)
# Print numbers 1–100
for i in range ( 1,100): # for loop
	print (i) 
i=1
while i <=	100: #while loop
	print(i)
	i +=1

#Guess-the-number game
import random
attempt=0
num = random.randint(1,10)
while True:
	guess=int(input('guess a number'))
	attempt +=1
	if guess<num:
		print('guess too low')
	elif guess >num:
		print('guess too high')
	else:
		print(f"you guessed it in {attempt} tries")
		break
