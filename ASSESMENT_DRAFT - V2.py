"""
Filename: Quiz
Name:Nabhi
Date:28/06/22
Description: A quiz that has mitluple choice for the user to answer
"""
import time 
q1_answers = ["1. Wellington","2. Auckland","3. Christchurch","4. Dunedin"]
  
overall_score = 0
print("Welcome to the Quiz")
time.sleep(1) 

user_name = input("Please Enter Your Name:").replace(" ", "")
print("hello there ,{}, good to meet you!".format(user_name))
print("Lets start off easy ,{}".format(user_name))
print()
q1 = print("What is the Capital of New Zealand?")
print(q1_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 1:
    print("Good job, you earnt a point")
    print("Remaining questions: 9 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 9 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))



print()
q2_answers = ["1. Oxygen","2. Sodium Carbonate","3. Carbon Dioxide","4. Helium"]
print("Question Two")
q2 = print("Which one of these contains Green House Gases? ")
print(q2_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 3:
    print("Good job, you earnt a point")
    print("Remaining questions: 8 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 8 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))



print()
q3_answers = ["1. Neptune","2. Uranus","3. Jupiter","4. Saturn"]
print("Question Three")
q3 = print("Which planet has the most gravity?")
print(q3_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 3:
    print("Good job, you earnt a point")
    print("Remaining questions: 7 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 7 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))



print()
q4_answers = ["1.  7","2.  8","3.  11","4.  12"]
print("Question Four")
q4 = print("How many faces does a dodecahedron have?")
print(q4_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 4:
    print("Good job, you earnt a point")
    print("Remaining questions: 6 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 6 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))



print()
q5_answers = ["1. K2","2. Mount Everest","3. Mount Taranaki","4. Kangchenjunga"]
print("Question Five")
q5 = print("What is the tallest mountain in the world?")
print(q5_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 2:
    print("Good job, you earnt a point")
    print("Remaining questions: 5 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 5 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))



print()
q6_answers = ["1. India","2. Russia","3. America","4. China"]
print("Question Six")
q6 = print("Which is the worlds largest country")
print(q6_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 2:
    print("Good job, you earnt a point")
    print("Remaining questions: 4 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 4 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))



print()
q7_answers = ["1. Tokyo","2. Yokohama","3. Kyoto","4. Nagasaki"]
print("Question Seven")
q7 = print("What is the capital of Japan? ")
print(q7_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 1:
    print("Good job, you earnt a point")
    print("Remaining questions: 3 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 3 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))



print()
q8_answers = ["1. United States","2. Pakistan","3. China","4. Brazil"]
print("Question Eight")
q8 = print("Largest Populated Country in the world?")
print(q8_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 3:
    print("Good job, you earnt a point")
    print("Remaining questions: 2 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 2 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))



print()
q9_answers = ["1. Chick-Fil-A","2. KFC","3. McDonalds","4. Subway"]
print("Question Nine")
q9 = print("What is the best fast food chain in the world?")
print(q9_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 3:
    print("Good job, you earnt a point")
    print("Remaining questions: 1 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 1 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))



print()
q10_answers = ["1. Sydney","2. Melbourne","3. Canberra","4. Brisbane"]
print("Question Ten")
q10 = print("What is the Capital of Australia")
print(q10_answers)
guess = int(input("Please select one by using the integers: "))
if guess == 3:
    print("Good job, you earnt a point")
    print("Remaining questions: 0 ")
    overall_score += 1
    print("your score now is :{} ".format(overall_score))
else:
    print("Incorrect Answer")
    print("Remaining questions: 0 ")
    overall_score += 0
    print("you score now is :{} ".format(overall_score))


