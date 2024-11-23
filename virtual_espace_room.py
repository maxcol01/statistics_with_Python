from data import puzzles, welcome_message
import time
import random as rd

# 2. Display the welcome message 
def display_welcome(welcome):
    print(welcome)
# 6. we will see

DURATION = 10 #  5 min
timer = DURATION
penality = 0
# Displaying the welcome message
display_welcome(welcome_message)
# Starting to play
stored_question = list()
num_questions = len(puzzles)
timer_start = time.time()
while (len(stored_question) < num_questions):
    num_choice = rd.randint(0, num_questions-1)
    timer_end = time.time()
    timer = DURATION-round(timer_end-timer_start)-penality
    print(f"Your have {timer} s remaining")
    if timer < 0:
        print("Time is up !")
        break
    else:
        if num_choice not in stored_question:
            choice = puzzles[num_choice]
            user_answer = input(f"{choice["question"]}")
            if user_answer != choice["solution"]:
                penality = 3 
            else:
                stored_question.append(num_choice)
        else:
            continue






