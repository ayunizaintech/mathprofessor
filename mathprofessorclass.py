import random

class Game():
    def __init__(self):
        pass

    def run(self):
        print()
        while True:
            chosen_level = input("Choose a level between 1 and 3: ")
            if chosen_level == "1":
                print("You have chosen Level 1.")
                print()
                self.ten_questions(0,9)

            elif chosen_level == "2":
                print("You have chosen Level 2.")
                print()
                self.ten_questions(10,99)
                
            elif chosen_level == "3":
                print("You have chosen Level 3.")
                print()
                self.ten_questions(100,999)
                
            else:
                continue

            play_again_input = input("Do you want to play again? Y or N: ")
            print()
            while play_again_input not in ("Y", "y", "N", "n"):
                print("Please enter either Y or N only.")
                print()
                play_again_input = input("Do you want to play again? Y or N: ")
                print()
            if play_again_input == "N" or play_again_input == "n":
                print("Thank you for playing. Goodbye!")
                break

    def ten_questions(self, first_digit_range, second_digit_range):
        correct_answer = 0

        # Create 2 random integers, and then add them up. Create 10 sums.
        for index in range(10):

            # Create 2 random integers.
            first_digit = random.randint(first_digit_range,second_digit_range)
            second_digit = random.randint(first_digit_range,second_digit_range)
            
            # The formula for the sum of 2 random digits.
            sum_of_two_digits = first_digit + second_digit

            # A user might enter a wrong answer format at this block. Like "ten" instead of "10".
            try:

                # User enters an input which is in string format. This string format is then converted to an integer. 
                user_answer = int(input(f"{index + 1}. What is the sum of {first_digit} + {second_digit}?: "))

                # If the user enters the correct answer to the sum, the program will print "Correct."
                if user_answer == sum_of_two_digits:
                    correct_answer += 1
                    print("Correct.")
                    print()

                # If the user enters the wrong integer answer to the sum, the program will give the user 2 more attempts.
                else:
                    attempt = 2
                    print(f"Try again. You have 2 more attempt(s).")
                    count = 1
                    while count < 3:
                        answer_again = int(input("Answer: "))
                        if answer_again == sum_of_two_digits:
                            correct_answer += 1
                            print("Correct.") 
                            print()
                            break
                        else:
                            count += 1
                            attempt -= 1
                            print(f"You have {attempt} more attempt(s).")
                            print()


            # If the user enters a wrong format answer like "one" instead of "1", this block will be triggered. 
            except: 
                # If the user keeps entering a word instead of an integer, the program will keep asking her
                # to enter the correct format. No limit.
                while True:
                    try:
                        except_block_user_answer = int(input("Please enter a numerical input like '1': "))
                    except ValueError:
                        print("Sorry. I didn't understand that.")
                        print()
                        continue
                    else:
                        break

                # If the user finally enters the correct integer answer instead of a string, this block is triggered: 
                if except_block_user_answer == sum_of_two_digits:
                    correct_answer += 1
                    print("Correct.")
                    print()
                
                # If the user finally enters an integer but a wrong answer to the question, this will be triggered. 
                # The program will give the user 2 more attempts for correct integer answer before moving to the next question. 
                else:
                    attempt = 2
                    print(f"Try again. You have 2 more attempt(s).")
                    count = 1
                    while count < 3:
                        answer_again = int(input("Answer: "))
                        if answer_again == sum_of_two_digits:
                            correct_answer += 1
                            print("Correct!")
                            print()
                            break
                        else:
                            count += 1
                            attempt -= 1
                            print(f"You have {attempt} more attempt(s).")
                            print()
                        
        # Print out the score report.
        print(f"Your score: {correct_answer} corrects and {10 - correct_answer} wrongs.")
        print()

math_prof_game = Game()
math_prof_game.run()