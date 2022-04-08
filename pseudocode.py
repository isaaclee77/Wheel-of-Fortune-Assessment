#set up wheel, wheel has 19 cash value segments, 1 BANKRUPT, 1 Lose a Turn

#set up the 3 players: player 1, player 2, and player 3

#Round 1
#show the random word with its lettes as "_"
#Player 1 spins wheel
    #If wheel lands on cash value
        #Player solves or guesses consonant
            #If Player guesses a correct consonant
                #display the consonant if it's there
                #Add money to player's bank
                #give opportunity to buy vowel or spin again
                    #if player has enough money to buy a vowel and wants to buys vowel
                        #subtract $250 from player's bank
                            #if vowel is in the word
                                #display vowel
                            #else
                                #next player spins
                    #else player wants to spin
                        #Player spins again
        #If player solves correctly 
            #End round
        #Else 
            #Next player spins

    #Elif wheel lands on Lose a Turn
        #Next player spins wheel

    #Else: (wheel lands on BANKRUPT)
        #Player bank goes to 0 and next player spins

print('hi')