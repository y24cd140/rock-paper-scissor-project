def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "r" and computer == "s") or \
         (user == "s" and computer == "p") or \
         (user == "p" and computer == "r"):
        return "You win!"
    else:
        return "Computer wins!"
end ="no"
while end!="yes":
    print ("\n\nlets play rock paper scissor")
    import time
    import random 
    print('ROCK...')
    time.sleep(1)
    print('PAPER...')
    time.sleep(1)
    print("SCISSOR ?")
    time.sleep(0.5)
    r="rock"
    p="paper"
    s="scissor"
    print('r="rock"\tp="paper"\ts="scissor"')
    choice=input("please enter your choice : ").lower()
    while choice not in ['r','p','s']:
        print('invalid choice.\nplease choose again\nr="rock"\tp="paper"\ts="scissor"')
        choice=input("please enter your choice again : ").lower()
    computer_choice=random.choice(['r','p','s'])
    if computer_choice=="r":
        print("computer chooses:",r)
    elif computer_choice=="p":
        print("computer chooses:",p)
    elif computer_choice=="s":
        print("computer chooses:",s)
    print(".", end='', flush=True)
    time.sleep(0.1)
    print(".", end='', flush=True)
    time.sleep(0.1)
    print(".", end='', flush=True)
    time.sleep(0.1)
    print(".", end='', flush=True)
    time.sleep(0.1)
    print(determine_winner(choice, computer_choice))
    end=input("willing to end the game(yes,no) : ")