import random
print("Wordle")
turn = 1
words = open("wordle_words.txt", "r").read().rstrip().split(",")
word = ""
end = False

def wordlegame():
    global turn
    global end
    if(turn > 6) or end == True:
        print("End")
        print(word)
    elif(turn <= 6):
        user_input = input()
        if(len(user_input.replace(' ', '')) == 5) and user_input.isalpha():
            turn += 1
            checkValidity(user_input)
            wordlegame()
        else:
            print("not a valid input")
            wordlegame()

def checkValidity(user_input):
    global word
    global end
    user_word = list(user_input)
    check_word = list(word)
    end_result = ["B","B","B","B","B"]
    for x in range(0, 5):
        if(user_word[x] == check_word[x]):
            end_result[x] = "G"
        elif user_word[x] in check_word:
            end_result[x] = "Y"
    if(set(end_result) == set(['G', 'G', 'G', 'G', 'G'])):
        end = True
    print(end_result)

def randomWord():
    global word
    word = words[random.randint(0,len(words) - 1)]

randomWord()
wordlegame()
