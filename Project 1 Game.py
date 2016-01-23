__author__ = 'Malcolm'
from deck_of_cards import *
#import computer_player
# from player import *
def main():
    discard_pile=[]
    list_of_players=[]
    end_game=False
    play_again=True

    """THIS OPENS AND DISPLAYS THE INSTRUCTIONS FOR THE GAME"""
    def read_and_print_instructions():
        file = open('rules_For_Crazy_8s.txt','r')
        for line in file:
            print(line)
        file.close()
    read_and_print_instructions()
    """THIS ENDS THAT"""



    """THIS IS A CLASS FOR THE PLAYERS"""
    class player:
        def __init__(self,name):
            # Players only have these components when initialized
            self.hand=[]
            self.score=int(0)
            self.name=name

        def __repr__(self):
            # nifty way of overriding the builtin object print method
            return str(self.name)
        # Shortcut for displaying basic info at the end of the game
        def name_and_score(self):
            return self.name+'\'s score:'+str(self.score)

        # This method displays the players hand
        def display_hand(self):
            counter=0
            for card in self.hand:
                print("-[{}]--> {}".format(counter+1,card))
                counter+=1
            print('-----------------------------------')
        # This method scores at the end of the game
        def add_up_points(self):
            scored_this_game = 0
            for a_card in self.hand:
                if a_card.face_or_number in deck_of_cards.dict_of_values:
                    point_value = deck_of_cards.dict_of_values.get(a_card.face_or_number)
                    self.score += point_value

            print(str(self.name_and_score()))
            print('----------------------------------')
            return self.score

        # This method selects the cards correctly from the hand
        def play_card(self, number_in_hand):

            a_card = self.hand[int(number_in_hand)-1]
            # if its an 8 do these things then play it
            if str(a_card)[0] == '8':
                # remove the old suit, replace with the new one
                # But which suit sir or madam?
                eight_suit_menu_choice = True
                while eight_suit_menu_choice == True:
                    counter2 = 1
                    print('------------Suits to choose from------------')
                    # Nice display of suits
                    for suit in deck_of_cards.suits:
                        print('-['+str(counter2)+']--> '+str(suit))
                        counter2 = counter2+1
                    print('--------------------------------------------')
                    # Make sure that they don't give strings
                    try:
                        suitChoice = int(input('Please select the new suit for the 8 you have played.'))
                        # if it isn't an option, don't allow the choice to occur, re-loop.
                        if (suitChoice-1) not in range(3):
                            print('Sorry you must select a suit from the list provided.')
                            eight_suit_menu_choice == True
                        else:
                            a_card.suit = deck_of_cards.suits[suitChoice-1]
                            self.hand.pop(int(number_in_hand)-1)
                            discard_pile.append(a_card)
                            eight_suit_menu_choice = False
                    except ValueError:
                        print('Sorry you must select a suit from the list provided using the numbers 1, 2, 3 or 4.')
                        eight_suit_menu_choice == True

            elif a_card.suit != discard_pile[-1].suit and a_card.face_or_number != discard_pile[-1].face_or_number:
                print(a_card.suit)
                print('You tried to play a card that was the wrong suit and the wrong face value. Try again.')
            elif a_card.face_or_number == discard_pile[-1].face_or_number:
                self.hand.pop(int(number_in_hand)-1)
                discard_pile.append(a_card)
                print('You played a '+str(a_card))
            elif a_card.suit == discard_pile[-1].suit:
                self.hand.pop(int(number_in_hand)-1)
                discard_pile.append(a_card)
                print('You played a '+str(a_card)+'.')
    #        The following Methods are for the computer player only, and will only ever be called by it.
    #        I hadn't done Python in almost 2 years and I barely remember extended class (for inheritence of attributes and such)
    #        So Rather than creating an extended secondary class I wrote all the methods any player could ever have here
    #        TODO Come back and make it sepearte classes once I've figured class extension out.
        def take_computer_turn(self):

            print('THE COMPUTER TAKES ITS TURN')
            # The order of the following list is :'Hearts','Spades','Clubs','Diamonds'
            number_of_suits = [0,0,0,0]
            def count_suits():

                for a_card in self.hand:
                    if a_card.suit == 'Hearts':
                        number_of_suits[0] += 1
                    elif a_card.suit == 'Spades':
                        number_of_suits[1] += 1
                    elif a_card.suit == 'Clubs':
                        number_of_suits[2]+=1
                    elif a_card.suit == 'Diamonds':
                        number_of_suits[3] += 1
                print(number_of_suits)

            def real_comp_turn():
                if len(player.hand) == 0 or len(deck.deck) == 0:
                    pass
                found_a_playable_card = True
                highest_value_on_list = 0
                entry_number_counter = 0
                actual_slot_number = 0
                i = 0

                for a_card in self.hand:
                    if a_card.suit == discard_pile[-1].suit or a_card.face_or_number == discard_pile[-1].face_or_number:
                        print('Computer player found a viable card in it\'s hand')
                        self.hand.pop(i)
                        discard_pile.append(a_card)
                        print('The Computer Played a '+str(a_card))
                        i = i+1
                        found_a_playable_card=True
                        if a_card.face_or_number == '8':
                            count_suits()
                            for entry in number_of_suits:
                                if entry > highest_value_on_list:
                                    highest_value_on_list = entry
                                    actual_slot_number = entry_number_counter
                                entry_number_counter+1
                            if actual_slot_number == 0:
                                a_card.suit = 'Hearts'
                            if actual_slot_number == 1:
                                a_card.suit = 'Spades'
                            if actual_slot_number == 2:
                                a_card.suit = 'Clubs'
                            if actual_slot_number == 3:
                                a_card.suit = 'Diamonds'
                            print('Computer Player Chooses :{}'.format(str(a_player.suit)))
                        break
                    else:
                        found_a_playable_card = False
                        i = i+1
                if found_a_playable_card == False:
                    self.hand.append(deck.deal_a_card_to_player_hand())

            """THIS METHOD CALL RUNS THE COMP'S TURN"""

            real_comp_turn()

    """END PLAYER CLASS"""
    def display_gameBoard():

        print('-----------------Crazy 8\'s-----------------\n'
              +str(list_of_players[0].name)+' \t\t\t\t'+str(list_of_players[1].name)+
              "\nCards in hand: "+str(len(list_of_players[0].hand))+"\t\tCards in hand: "+str(len(list_of_players[1].hand))+
              "\nDiscard Pile Shows: "+str(discard_pile[-1])+'\nCards left in the Deck: '+str(len(deck.deck))+'\n-------------------------------------------')

    def determine_winner():
            print('---------------------------------'
                  '\nThe End of the Game Has Happened!'
                  '\nHands are being Tallied!'
                  '\n---------------------------------')
            for playerForScore in list_of_players:

                    score = playerForScore.add_up_points()
                    playerForScore.score = score
                    playerForScore.name_and_score()
            low_score = 1500
            for playerForScore in list_of_players:
                if playerForScore.score <= low_score:
                    low_score = playerForScore.score
            for playerForScore in list_of_players:
                if playerForScore.score == low_score:
                    print('{} Has won the game with {} points!'.format( str(playerForScore.name), str(playerForScore.score)))
                    print('-------------------------------------------------')

    # make players, computer and human
    player1 = player((input('Please enter your name.\n')))
    # This block is to make sure the player can't be called computer
    if player1.name == 'Computer':
        player1.name = input('Please enter a Name that is NOT "Computer".')
        while player1.name == 'Computer':
            player1.name = input('Please enter a Name that is NOT "Computer".')
    list_of_players.append(player1)
    computer_Player = player('Computer')
    list_of_players.append(computer_Player)
    # determine who goes first
    while play_again == True:
        random.shuffle(list_of_players)
        # Initialize the deck
        deck = deck_of_cards()
        #deal card to discard pile
        discard_pile.append(deck.deal_a_card_to_player_hand())
        # deal the first hands out to the two players
        for i in range(7):
            for player in list_of_players:
                player.hand.append(deck.deal_a_card_to_player_hand())
        #         display game board for the first time
        display_gameBoard()
        print(str(list_of_players[0])+' won the coin flip and will go first.')

    # Here is where the game runs
        while end_game == False:

            for a_player in list_of_players:
                if a_player.name == 'Computer':
                    if len(deck.deck) == 0 or len(a_player.hand) == 0:
                        end_game = True
                        pass
                        break
                    a_player.take_computer_turn()
                    print('-----------------------------------')
                else:
                    if len(deck.deck) == 0 or len(a_player.hand) == 0:
                        end_game = True
                        pass
                        break
                    display_gameBoard()
                    turn_over = False
                    playable_suits = discard_pile[-1].suit
                    print(playable_suits)
                    a_player.display_hand()
                    print('Enter draw, or d to draw a card.  or h or help for the games instructions')
                    print('-----------------------------------')

                    while turn_over == False:
                        if len(deck.deck) == 0:
                            break
                        card_to_play=input('Which card do you want to play? It must be a '+discard_pile[-1].suit+' or an '+discard_pile[-1].face_or_number+'.')
                        try:
                            if card_to_play in 'draw':
                                a_player.hand.append(deck.deal_a_card_to_player_hand())
                                print('You drew a card.')
                                turn_over = True
                                if len(deck.deck) == 0 or len(a_player.hand) == 0:
                                    break
                            elif card_to_play in 'help':
                                read_and_print_instructions()
                                turn_over = False
                            else:
                                a_player.play_card(card_to_play)
                                turn_over = True
                        except ValueError:
                            print('Your response was not understood, please try again. '
                                  'Be more careful with spelling and capitalization')
                            turn_over = False

                    if len(a_player.hand) == 0 or len(deck.deck) == 0:
                        end_game=True
                        break
        determine_winner()
        play_again_method()


        def play_again_method():
            play_again_loop = True
            while play_again_loop == True:
                y_or_n = str(input('Would you like to play another game? Type "y" to play again or "n" to exit the game.'))
                if y_or_n == 'y' or y_or_n == 'Y':

                    for a_player in list_of_players:
                        a_player.hand.clear()
                        print('That was the hand being deleted')
                        a_player.score = 0
                        print('That was the score being deleted.      {}'.format(a_player.score))
                    discard_pile.clear()
                    print(discard_pile)
                    print('Discard Piles...  uhhh... discarded...')
                    del deck.deck
                    play_again_loop = False
                    end_game = False
                    play_again = True
                    print('---------------------------------------------'
                          '\nYOU HAVE SELECTED TO PLAY AGAIN, ENJOY'
                          '\n---------------------------------------------')

                elif y_or_n == 'n' or y_or_n == 'N':
                    play_again = False
                    play_again_loop = False
                    print('---------------------------------------------------'
                          '\nYOU HAVE SELECTED TO EXIT THE GAME, HAVE A NICE DAY'
                          '\n---------------------------------------------------')

                else:
                    play_again_loop = True
                    print('Please select y or n only.')

main()