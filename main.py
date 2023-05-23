print("Welcome to Bible Trivia!")

# Python code to retrieve the quiz questions and answers from an array
questions = [["Where did Moses die?", "Mount Nebo", ["Mount Nebo", "Mount Zion", "Mount of Olives", "Mount Sinai"]],
             ["What did God do on the fourth day of Creation?", "He created the sun, moon, and stars",
              ["He created animals", "He created the first man, Adam", "He created the sun, moon, and stars",
               "He created the Empire State Building"]]]

#function to run through quiz questions
def currentQuestion(questionslist):
    qnum = 0
    score = 0
    for question in questionslist:
        (question, answer, choices) = list(questionslist[qnum])
        print(question)
        for choice in choices:
            print(choice)
        userAnswer = input('type your answer here >')
        if userAnswer.lower() == answer.lower():
            score += 1
            print('Your answer is correct')
        else:
            print('Wrong answer, the correct answer is ' + answer)
        qnum += 1
    print("You got " + str(score) + '/' + str(qnum) + " correct")

def buildquiz():
    buildquestions = list()
    questionsnum = input("How many questions?")
    for question in range(int(questionsnum)):
        buildquestion = input("Type your question:")
        buildanswer = input("Type the correct answer:")
        buildchoices = input("Type four choices with a comma between each choice")
        buildquestions.append([buildquestion, buildanswer, list(map(str.strip, buildchoices.split(",")))])
    currentQuestion(buildquestions)


def runquiz():
    welcome_answer = input("Would you like to A. Build a quiz or B. play a quiz that's already built? Type A or B: ")
    if welcome_answer.upper() == 'A':
        buildquiz()
    elif welcome_answer.upper() == 'B':
        currentQuestion(questions)
    else:
        print("This option does not exist, try A or B")
        runquiz()

runquiz()

