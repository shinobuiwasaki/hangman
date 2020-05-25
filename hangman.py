
import random

def hangman():
    word_list =["cat", "dog", "dolphin", "bird", "panda"]
    random_number = random.randint(0,4)
    word = word_list[random_number]

    wrong = 0
    stages = ["",
              "__________          ",
              " |                  ",
              " |        |         ",
              " |        O         ",
              " |       /|\        ",
              " |       / \        ",
              " |                  "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hungman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess what one letter."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You are win!")
            print(" ".join(board))
            win = True
            break
    if not win:
            print("\n".join(stages[0:wrong+1]))
            print("You are lose! The answer is {}.".format(word))


hangman()

