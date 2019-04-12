'''
This is a programmed version of the card game Mau, using Python (mostly without OOP)
It was coded by ArtiMe, 6 April 2019
If you use it for a project, please give credit to ArtiMe for the code! 
'''

#import modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spades','Hearts','Diamonds','Clubs']))
hand = [] #list to represent player's hand
ophand = [] #list to represent opponent's hand
discard_pile = ["bsolutely nothing"] #list to represent pile where played cards go
original = [] #empty list to reset other lists
rounds = 0 #integer to represent how many rounds have been played
opwins = 0 #integer to represent how many times the AI opponent has won
playerwins = 0 #integer to represent how many times the player has won
rules = []
rules_in_play= []


discard_card = discard_pile[-1]
for rule in rules:
    if rule in rules_in_play:
        rules.remove(rule)


def shuffle():
    # shuffle the cards in your deck
    random.shuffle(deck)
    
# draw function to draw cards from deck
def draw(ran, person): # variable "ran" represents range (or number of cards drawn) and "person" represents who is drawing the card 
    
    drawn = False
    if person == "player": # The player draws cards
        print("You draw a card.")
        # draw a card
        #print("You got:\n")
        while drawn == False:
            for i in range(ran):
                if [i][0] in range(2, 11):
                    card =(str(deck[i][0]) + " of " + str(deck[i][1]))
                    hand.append(card)
                    print(card)
                elif [i][0] == 11:
                    card =("Jack of " + str(deck[i][1]))
                    print(card)
                    hand.append(card)
                elif str(deck[i][0]) == 12:
                    card =("Queen of "+ str(deck[i][1]))
                    print(card)
                    hand.append(card)
                elif str(deck[i][0]) == 13:
                    card =("King of " +str(deck[i][1]))
                    print(card)
                    hand.append(card)
                elif str(deck[i][0]) == 1:
                    card =("Ace of " + str(deck[i][1]))
                    print(card)
                    hand.append(card)
            drawn = True
    elif person == "opponent": # The opponent draws cards
        while drawn == False:
            for i in range(ran):
                if [i][0] in range(2, 11):
                    card =(str(deck[i][0]) + "of" + str(deck[i][1]))
                    ophand.append(card)
                elif [i][0] == 11:
                    card =("Jack of " + str(deck[i][1]))
                    ophand.append(card)
                elif [i][0] == 12:
                    card =("Queen of " + str(deck[i][1]))
                    ophand.append(card)
                elif [i][0] == 13:
                    card =("King of "+ str(deck[i][1]))
                    ophand.append(card)
                elif str(deck[i][0]) == 1:
                    card =("Ace of " + str(deck[i][1]))
                    ophand.append(card)
            drawn = True
            if ran > 1:
                print("Your opponent drew " + str(ran) + " cards.")
            elif ran == 1:
                print("Your opponent drew a card.")
    elif person == "discard":
        if "none" in discard_pile:
            discard_pile.remove("none")
        for i in range(ran):
            if [i][0] in range(2, 11):
                card =(str(deck[i][0])+ "of"+ str(deck[i][1]))
                discard_pile.append(card)
            elif [i][0] == 11:
                card =("Jack of "+ str(deck[i][1]))
                discard_pile.append(card)
            elif str(deck[i][0]) == 12:
                card =("Queen of "+ str(deck[i][1]))
                discard_pile.append(card)
            elif str(deck[i][0]) == 13:
                card =("King of "+ str(deck[i][1]))
                discard_pile.append(card)  
            elif str(deck[i][0]) == 1:
                card =("Ace of "+ str(deck[i][1]))
                discard_pile.append(card)
                                        
    shuffle()
    
            
def setup(): #Setting up the game and going over the rules
    print("Ready to play a game of Mau?\nThis game plays with multiple decks, so do not be surprised if you draw a card more than once.")
    if rounds == 0:    
        r = raw_input("Do you know the rules of Mau? y/n ")
        if r == "y":
            print("Now begins the game of Mau.")
        elif r == "n":
            print("The first rule of the game of Mau is that you do not share the rules of Mau.")
            print('Really persistent? Go to "https://en.wikipedia.org/wiki/Mao_(card_game)" to learn the basic rules of the game.')
    else:
        print("The deck has been shuffled for the new round.")
    hand == original
    ophand == original
    
    print("Now begins the game of Mau.")
    shuffle()
    draw(7,"player")
    draw(7,"opponent")
    #print("You and your opponent each drew 7 cards.") REPETITIVE
    draw(1, "discard")
    print("There is a " + discard_card + " in the discard pile.")
    shuffle()
    your_turn()
    
def your_turn(): #The player takes their turn
    print("It is your turn.")
    draw(1, "player")
    print("Cards in your hand:")
    for c in hand:
        print(c)
    print("There is a "+ discard_card + " in the discard pile.")
    n = raw_input('What card would you like to play?\nIf you have no cards to play, type "draw" ')
    con = False
    while con != True: 
        for card in hand:
            if n == card:
                if n[1] == card[1] or n[-2] == card[-2]: 
                    hand.remove(card)
                    discard_pile.append(card)
                con = True
            elif n == "draw":
                draw(1, "player")
                con == True
        print("That card is not in your hand, try again!")
        print("Cards in your hand:")
        for c in hand:
            print(c)
        n = raw_input("What card would you like to play? ")
    shuffle()
    if len(hand) < 2:
        print("You have one card left! You call Mau. This round is over. You win!")
        rounds + 1
        playerwins + 1
        c = False
        while c != False:
            n = raw_input("Would you like to play again? y/n")
            if n == "y" or n == "Y":
                #rule_function
                c = True
            elif n == "n" or n == "N":
                print("Thanks for playing!")
                if playerwins > opwins:
                    print("You won by " + str(playerwins-opwins) + " rounds.")
                elif opwins < playerwins:
                    print("Your opponent won by " + str(opwins-playerwins) + "rounds.")
                elif playerwins == opwins:
                    print("You and your opponent tied. Good game!")
                c = True
            else:
                print("Sorry, could you repeat that?\nWould you like to play again? y/n")
    else:
        opp_turn()
         
def opp_turn(): #The opponent takes their turn
    print("It is your opponent's turn")
    draw(1, "opponent")
    con = False
    while con != True:
        for card in ophand:
            if discard_card[1] == card[1] or discard_card[-2] == card[-2]:
                discard_pile.append(card)
                ophand.remove(card)
                con == True
        draw(1, "opponent")
        con == True
    shuffle()
    if len(ophand) < 2: 
        print("Your opponent calls Mau. This round is over. They win.")
        rounds + 1
        opwins + 1
        c = False
        while c != False:
            n = input(str("Would you like to play again? y/n"))
            if n == "y":
                #rule_function
                c = True
            elif n == "n":
                print("Thanks for playing!")
                if playerwins > opwins:
                    print("You won by " + str(playerwins-opwins) + " rounds.")
                elif opwins < playerwins:
                    print("Your opponent won by " + str(opwins-playerwins) + "rounds.")
                elif playerwins == opwins:
                    print("You and your opponent tied. Good game!")
                c = True
            else:
                print("Sorry, could you repeat that?\nWould you like to play again? y/n")
    else:
        your_turn()
setup()