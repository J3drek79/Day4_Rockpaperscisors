# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
endval = len(names)
rndsel = random.randint(1, endval)
namepay = names[rndsel]
print(f"{namepay} is going to buy the meal today!")
