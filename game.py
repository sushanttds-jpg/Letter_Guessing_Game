word = "github" #you can add any accordingly to your choice
guess_word = "" #used to store strings 
chances = 3 #used chances variable to give user chances

print("\n======= Welcome To word guessing game =======")
while chances > 0:
    show = ""
    for letter in word:        
        if letter in guess_word:
            show = show + letter
        else:
            show = show + "_"
    print("Word:", show)       
    
    if show == word:          
        print("You won yaay 👏")
        break

    inputt = input("Enter what you've guessed :")
    guess_word = guess_word + inputt

    if inputt not in word:
        chances = chances - 1
        print("Sorry you've guessed wrong")
        print("chances left :", chances)

    if chances == 0:
        print("you lost")
        print("Youre word was :", word)
        break                