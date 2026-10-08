import math
import time
fibonacci_sequence = [0, 1]
powers_series = []
correct_answers = []
time_over = 0
skip_all_other = 0

def printing(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
        
def fibonacci_guessing_sequence(num_questions, time_limit):
    start_time = time.time()
    global skip_all_other
    printing("You will have " + str(time_limit) + " seconds to answer " + str(num_questions)+ " questions.")
    print("")
    printing("If you take to long to answer, the remaining questions will be skipped.")
    print("")
    printing("You will not gain time if you get an incorrect or correct answer.")
    time.sleep(1)
    print("")
    print("3.")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Start!")
    print("")
    for i in range(num_questions):
        if skip_all_other != 1:
            skip_all_other = 0
        if skip_all_other == 1:
            continue
        if time.time() - start_time - time_limit >= time_limit:
            if time_over == 0:
                printing("Times up! Skipping all other questions")
                print("")
                skip_all_other = 1
                continue
        fibonacci_answer = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        user_answer = int(input("What's the next number: "))
        if user_answer == fibonacci_answer:
            fibonacci_sequence.append(user_answer)
            correct_answers.append(user_answer)
            printing("Correct!")
            print("")
            print(fibonacci_sequence)
            print("")
        else:
            printing("False.")
            print("")
            printing("The answer was: " + str(fibonacci_answer))
            fibonacci_sequence.append(fibonacci_answer)
            print("")
            print(fibonacci_sequence)
            print("")
    print("")
    printing("Finished!")

def powers_guessing_sequence(base, num_questions, time_limit):
    start_time = time.time()
    global skip_all_other
    printing("You will have " + str(time_limit) + " seconds to answer " + str(num_questions)+ " questions.")
    print("")
    printing("If you take to long to answer, the remaining questions will be skipped.")
    print("")
    printing("You will not gain time if you get an incorrect or correct answer.")
    time.sleep(1)
    print("")
    print("3.")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Start!")
    print("")
    for i in range(num_questions):
        if skip_all_other != 1:
            skip_all_other = 0
        if skip_all_other == 1:
            continue
        if time.time() - start_time - time_limit >= time_limit:
            if time_over == 0:
                printing("Times up! Skipping all other questions")
                print("")
                skip_all_other = 1
                continue
        powers_answer = math.pow(base, i)
        user_answer = int(input("What's the next number: "))
        if user_answer == powers_answer:
            powers_series.append(user_answer)
            correct_answers.append(user_answer)
            printing("Correct!")
            print("")
            print(powers_series)
        else:
            printing("False.")
            print("")
            printing("The answer was: " + str(powers_answer))
            print("")
            powers_series.append(powers_answer)
            print(powers_series)
    print("")
    printing("Finished!")

def scoring(num_questions):
    print("")
    printing("Calculating........")
    print("")
    printing("You got " + str(total) + " out of the " + str(num_questions) + " questions right.")
    accuracy = total / num_questions
    percent = accuracy * 100
    rounded_percent = round(percent, 2)
    print("")
    if rounded_percent == 100:
        printing("You have a " + str(rounded_percent) + "% accuracy. Amazing!")
    else:
        printing("You have a " + str(rounded_percent) + "% accuracy for this time.")

printing("Please answer using Fibonacci or Powers. Spell it as stated.")
print("")
time.sleep(0.5)
which_sequence = input("Which type of sequence do you want to do?: ")
time.sleep(1)
printing("The time for this game goes by very quickly.")
print("")
time.sleep(0.5)
time_limit = int(input("How many seconds do you want for all the questions?: "))
time.sleep(1)

if(time_limit > 0):
    if (which_sequence == "Fibonacci"):
        printing("The sequence will begin after the numbers 0 and 1.")
        print("")
        time.sleep(1)
        how_many_questions = int(input("How many numbers would you like to guess?: "))
        if how_many_questions<= 0:
            printing("You can not use " + str(how_many_questions) + "for this code.")
        else:
            num_questions = how_many_questions
            fibonacci_guessing_sequence(num_questions, time_limit)
            total = len(correct_answers)
            scoring(num_questions)
    elif (which_sequence == "Powers"):
        printing("The sequence will start at the zero power.")
        print("")
        time.sleep(1)
        base = int(input("What base number do you want to use: "))
        if base <= 0:
            printing("You can not use " + str(base) + "for this code.")
            print("")
        else:    
            how_many_questions = int(input("How many numbers would you like to guess?: "))
            if how_many_questions<= 0:
                printing("You can not use " + str(how_many_questions) + "for this code.")
            else:
                num_questions = how_many_questions
                powers_guessing_sequence(base, num_questions, time_limit)
                total = len(correct_answers)
                scoring(num_questions)
    else:
        printing("That sequence is not possible. Try again")
else:
    printing("I am sorry, you can not have that much time. Try again.")