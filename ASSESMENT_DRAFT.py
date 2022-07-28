"""
Filename: Quiz
Name:Nabhi
Date:28/06/22
Description: A quiz that has mitluple choice for the user to answer
"""
q1_answers = ["1. Wellington","2. Auckland","3. Christchurch","4. Dunedin"]
  
overall_score = 0
print("Welcome to the Quiz")
user_name = str(input("Please Enter Your Name:")).strip()
print("hello there ,{}, good to meet you!".format(user_name))
print("Lets start off easy ,{}".format(user_name))
print()
q1 = print("What is the Capital of New Zealand?")
print(q1_answers)
guess = str(input("Please select one by using the integers: ")).strip()
if guess == "1":
    print("Good job, you earnt a point")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))
    
print()
q2_answers = ["1. Oxygen","2. Sodium Carbonate","3. Carbon Dioxide","4. Helium"]
print("Question Two")
q2 = print("Which one of these contains Green House Gases? ")
print(q2_answers)
guess = str(input("Please select one by using the integers: ")).strip()
if guess == "3":
    print("Good job, you earnt a point")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))
    
print()
q3_answers = ["Neptune","Uranus","Jupiter","Saturn"]
print("Question Three")
q3 = print("Which planet has the most gravity?")
print(q3_answers)
guess = str(input("Please select one by using the integers: ")).strip()
if guess == "3":
    print("Good job, you earnt a point")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))
("How many faces does a Dodecahedron have?")
