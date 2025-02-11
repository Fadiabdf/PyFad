# ----------------------------------------------------------
def new_game():
    guesses = []# empty list
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("-----------------------------")
        print(key)#print the question
        for i in options[question_num-1]:
            print(i)# the ieme ... list of possible answers for the ieme question
        guess = input("Enter (A, B, C, or D) :")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)

        question_num += 1
    display_score(correct_guesses,guesses)
# ----------------------------------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG :(")
        return 0


# ----------------------------------------------------------
def display_score(correct_guesses,guesses):
    print("------------------------------------")
    print(" RESULTS")
    print("------------------------------------")

    print("Answers :", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print("")

    print("Guesses :", end=" ")
    for i in guesses:
        print(i, end=" ")
    print("")

    score = int((correct_guesses/len(questions))*100)
    print("your score is : "+str(score)+"%")

# ----------------------------------------------------------
def play_again():
    response = input("Do you want to play again, (yes or no) :")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# ----------------------------------------------------------
# a dictionary
#Global variable
questions = {
    # "key":"value",
    "who created Python ?": "A",
    "what year was Python created ?": "B",
    "Python is tributed to which comedy group ?": "C",
    "Is the Earth round ?": "A"
}
# 2D LIST: list of list
#Global variable
options = [
    ["A.Guido van Rossum", "B.Elon Musk", "C.Bill Gates", "D.Mark Zuckerberg"],
    ["A.1989", "B.1991", "C.2000", "D.2016"],
    ["A.Lonely Island", "B.Smosh", "C.Monty Python", "D.SNL"],
    ["A.True", "B.False", "C.sometimes", "D.What's Earth?"]
]

new_game()
while play_again():
    new_game()
print("Byeeeeeee !")
