






quiz = {
    "question1":{
        "question" : "What is the capital of France",
        "answer" : "Paris"
    },
    "question2":{
        "question":"What is the capital of Germany?",
        "answer":"Berlin"
    },
    "question3":{
    "question" : "What is the capital of Italy?",
    "answer":"Rome"
    }
}

score = 0 

for key, value in quiz.items():
    print(value['question'])
    answer = input("What is your answer? ")

    if answer.lower() == value['answer'].lower():
        print("This is correct")
        score = score + 1
        print("Your score is: " + str(score))

    else: print('You are wrong')


