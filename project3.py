# Idea: The bunch of math question

import random
import time

# 4 simple operators
OPERATORS = ["+", "-", "*"] 
MIN_OPERAND = 3
MAX_OPERAND = 20
TOTAL_PROBLEMS = 5

# Generate random easy math
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(exp)
    return exp, answer

wrong = 0
print("This round will have", TOTAL_PROBLEMS, "problems")
input("Press any key to start!")
print("---------------------------------")

# start time
start_time = time.time()

# Loops generate random math question
for i in range(TOTAL_PROBLEMS):
    exp, answer =  generate_problem()  
    print(answer)
    while True:
        guess = input("Problem number " + str(i+1) + ": " + exp + " = ") 
        if guess == str(answer):
            break
        wrong += 1
    
# end time
end_time = time.time()
total_time = round(end_time - start_time, 2)
    
print("---------------------------------")
print("You finished in", total_time, "seconds!")
print("You have", wrong, "wrong answers!")

