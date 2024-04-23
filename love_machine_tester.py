print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total_true = 0
total_love = 0
if "t" in name1.lower():
    #print(f"T occurs {name1.count('t')}")
    total_true += name1.lower().count("t")
if "r" in name1.lower():
    #print(f"R occurs {name1.count('r')}")
    total_true += name1.lower().count("r")
if "u" in name1.lower():
    #print(f"U occurs {name1.count('u')}")
    total_true += name1.lower().count("u")
if "e" in name1.lower():
    #print(f"E occurs {name1.count('e')}")
    total_true += name1.lower().count("e")


if "l" in name2.lower():
    #print(f"L occurs {name2.count('l')}")
    total_love += name2.lower().count("l")
if "o" in name2.lower():
    #print(f"O occurs {name2.count('o')}")
    total_love += name2.lower().count("o")
if "v" in name2.lower():
    #print(f"V occurs {name2.count('v')}")
    total_love += name2.lower().count("v")
if "e" in name2.lower():
    #print(f"E occurs {name2.count('e')}")
    total_love += name2.lower().count("e")

concatenated = str(total_true) + str(total_love)

if int(concatenated) > 10 or int(concatenated) > 90:
  print(f"Your score is {concatenated}, you go together like coke and mentos.")
elif int(concatenated) >=40 and int(concatenated) >= 50:
  print(f"Your score is {concatenated}, you are alright together.")
else:
  print(f"Your score is {concatenated}")
  

    
  