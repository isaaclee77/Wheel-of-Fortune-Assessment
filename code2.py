#Import file
import random
f = open('words.txt')
words_list = f.read().splitlines()
f.close()


theWord = random.choice(words_list).lower()
theWord2 = random.choice(words_list).lower()
theWord3 = random.choice(words_list).lower()

#Round 1 Bank

player1bank = 0
player2bank = 0
player3bank = 0

#Round 2 Bank

player1bank2 = 0
player2bank2 = 0
player3bank2 = 0

#Round 3 Bank

player1bank3 = 0
player2bank3 = 0
player3bank3 = 0

round_1 = False
round_2 = False
round_3 = False

players = ['p1', 'p2', 'p3']

puzzle = theWord

word_underlist1 = []

word_underlist2 = []

word_underlist3 = []

#Wheel segments

wheel_list = ["bankrupt", 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
600, 650, 700, 750, 800, 850, 900, 950, 1000, "Lose a Turn"]

#Adding "_"
for char in theWord:
    word_underlist1.append('_')

for char in theWord2:
    word_underlist2.append('_')

for char in theWord3:
    word_underlist3.append('_')


word = list(theWord)
word2 = list(theWord2)
word3 = list(theWord3)

#Wheel function

def get_spin():

    spin = random.choice(wheel_list)
    spin = spin
    return spin

spin = get_spin()

#consonants and vowels
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']

#Next player function
def Next_Player(current_player):
    position = players.index(current_player)
    if position == 0 or position == 1:
        next_player = players[position + 1]
    else:
        next_player = players[0]
    return next_player

#Players
player1 = "Player 1"
player2 = "Player 2"
player3 = "Player 3"
players = [player1, player2, player3]

#ROUND 1
currentplayer = player1
roundisHappening = 1
FirstTurn = True
first_consonant_player_1 = False
while roundisHappening == 1:
    wheel_spin = get_spin()
    print(word)
    if wheel_spin == "bankrupt":
        player1bank = 0
        print(currentplayer, 'You got Bankrupt')
        currentplayer = Next_Player(currentplayer)
        print(currentplayer, "it is your turn")
        spin = get_spin()
        first_consonant_player_1 = True
        FirstTurn = True
        continue
    elif spin == "Lose a Turn":
        print('You lose a turn')
        currentplayer = Next_Player(currentplayer)
        print(currentplayer, "it is your turn")
        spin = get_spin()
        first_consonant_player_1 = True
        FirstTurn = True
        continue
    else:
        print(' '.join(word_underlist1))
        print(currentplayer, 'It is your turn. You are playing for $',wheel_spin)
        userinput = input('Guess a consonant: ').lower()
        if len(userinput) == 1 and userinput in consonants:
            if userinput in word:
                for position in range(len(word)):
                    if word[position] == userinput:
                        word_underlist1[position] = userinput
                        if currentplayer == player1:
                            player1bank = player1bank + wheel_spin
                            print('Good job! You currently have $', player1bank)
                        if currentplayer == player2:
                            player2bank = player2bank + wheel_spin
                            print('Good job! You currently have $', player2bank)
                        if currentplayer == player3:
                            player3bank = player3bank + wheel_spin
                            print('Good job! You currently have $', player3bank)     
                        first_consonant_player_1 = True
                print(' '.join(word_underlist1))    

                #After intial consonant guess
                while FirstTurn == True:
                    #PLAYER1

                    userinput = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                    if userinput == 'consonant':
                        spin = get_spin()
                        if spin == "bankrupt":
                            print("you got bankrupt")
                            player1 = 0
                            currentplayer = Next_Player(currentplayer)
                            print(currentplayer, "it is your turn")
                        elif spin == "Lose a Turn":
                            print("You spun on Lose a Turn")
                            currentplayer = Next_Player(currentplayer)
                            print(currentplayer, "it is your turn")
                        else:
                            print(currentplayer, "you are playing for $", spin)
                            userinput = input('Guess a consonant: ').lower()
                            if len(userinput) == 1 and userinput in consonants:
                                if userinput in word:
                                    if currentplayer == player1:
                                        player1bank = player1bank + spin
                                        print('Good job! You currently have $', player1bank)
                                    if currentplayer == player2:
                                        player2bank = player2bank + spin
                                        print('Good job! You currently have $', player2bank)
                                    if currentplayer == player3:
                                        player3bank = player3bank + spin
                                        print('Good job! You currently have $', player3bank)   
                                    for position in range(len(word)):
                                        if word[position] == userinput:
                                            word_underlist1[position] = userinput
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            FirstTurn = False
                                            first_consonant_player_1 = True
                                    print(' '.join(word_underlist1))
#ighaihgugjifjgiajfgi                                    print('Good job! You currently have $', player1bank)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    currentplayer = Next_Player(currentplayer)
                                    print(currentplayer, "it is your turn")
                                    FirstTurn = True
                                    first_consonant_player_1 = True

                    if userinput == 'vowel':
                        userinput = input('Guess a vowel: ').lower()
                        player1bank = player1bank - 250
                        if len(userinput) == 1 and userinput in vowels:
                            if userinput in word:
                                for position in range(len(word)):
                                    if word[position] == userinput:
                                        word_underlist1[position] = userinput
                                    if '_' not in word_underlist1:
                                        print('You now won!')
                                        FirstTurn = False
                                        first_consonant_player_1 = True
                                print(' '.join(word_underlist1))
                            else:
                                print('Bad guess. You lost your turn')
                                currentplayer = Next_Player(currentplayer)
                                FirstTurn = False
                                first_consonant_player_1 = True
                        else:
                            print('Bad guess. You lost your turn')
                            FirstTurn = False
                            first_consonant_player_1 = True

                    if userinput == 'word':
                        def convert(s):
                            new = ''
                            for x in s:
                                new += x
                            return new                            
                        userinput = convert(input('Guess a word: ').lower())
                        word = convert(word)
                        if userinput == word:
                            print(word, 'is correct!')
                            print('You won the round! You won $', player1bank)
                            FirstTurn = False
                            first_consonant_player_1 = True
                            roundisHappening = 2
                        else:
                            print('That is not the full word. Try again.')
                            FirstTurn = False
                            first_consonant_player_1 = True

            else:
                print('That is not in the word. You lost your turn')
                currentplayer = Next_Player(currentplayer)
                print(currentplayer, "it is your turn")
                first_consonant_player_1 = True
                FirstTurn = False
        else:
            print('That is not one letter and a consonant. Try again')
            first_consonant_player_1 = True
            FirstTurn = False



# ROUND 2
FirstTurn = True
first_consonant_player_1 = False
while roundisHappening == 2:
    wheel_spin = get_spin()
    print(word2)
    if wheel_spin == "bankrupt":
        player1bank = 0
        print(currentplayer, 'You got Bankrupt')
        currentplayer = Next_Player(currentplayer)
        print(currentplayer, "it is your turn")
        spin = get_spin()
        first_consonant_player_1 = True
        FirstTurn = True
    elif spin == "Lose a Turn":
        print('You lose a turn')
        currentplayer = Next_Player(currentplayer)
        print(currentplayer, "it is your turn")
        spin = get_spin()
        first_consonant_player_1 = True
        FirstTurn = True
    else:
        print(' '.join(word_underlist2))
        print(currentplayer, 'You are playing for $',wheel_spin)
        userinput = input('Guess a consonant: ').lower()
        if len(userinput) == 1 and userinput in consonants:
            if userinput in word2:
                for position in range(len(word2)):
                    if word2[position] == userinput:
                        word_underlist2[position] = userinput
                        if currentplayer == player1:
                            player1bank2 = player1bank2 + wheel_spin
                            print('Good job! You currently have $', player1bank2)
                        if currentplayer == player2:
                            player2bank2 = player2bank2 + wheel_spin
                            print('Good job! You currently have $', player2bank2)
                        if currentplayer == player3:
                            player3bank3 = player3bank3 + wheel_spin
                            print('Good job! You currently have $', player3bank3)     
                        first_consonant_player_1 = True
                print(' '.join(word_underlist2))    

                #After initial consonant guess
                while FirstTurn == True:
                    #PLAYER1

                    userinput = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                    if userinput == 'consonant':
                        spin = get_spin()
                        print(currentplayer, "It is your turn. You are playing for $", spin)
                        userinput = input('Guess a consonant: ').lower()
                        if len(userinput) == 1 and userinput in consonants:
                            if userinput in word2:
                                if currentplayer == player1:
                                    player1bank2 = player1bank2 + spin
                                    print('Good job! You currently have $', player1bank2)
                                if currentplayer == player2:
                                    player2bank2 = player2bank2 + spin
                                    print('Good job! You currently have $', player2bank2)
                                if currentplayer == player3:
                                    player3bank2 = player3bank2 + spin
                                    print('Good job! You currently have $', player3bank2)  
                                for position in range(len(word2)):
                                    if word2[position] == userinput:
                                        word_underlist2[position] = userinput
                                    if '_' not in word_underlist2:
                                        print('You now won!')
                                        FirstTurn = False
                                        first_consonant_player_1 = True
                                print('Good job! You currently have $', player1bank)  
                            else:
                                print('Wrong letter guess. You lost your turn')
                                currentplayer = Next_Player(currentplayer)
                                FirstTurn = True
                                first_consonant_player_1 = True

                    if userinput == 'vowel':
                        userinput = input('Guess a vowel: ').lower()
                        player1bank = player1bank - 250
                        if len(userinput) == 1 and userinput in vowels:
                            if userinput in word2:
                                for position in range(len(word2)):
                                    if word2[position] == userinput:
                                        word_underlist2[position] = userinput
                                    if '_' not in word_underlist2:
                                        print('You now won!')
                                        FirstTurn = False
                                        first_consonant_player_1 = True
                                print(' '.join(word_underlist2))
                                print('Good job! You currently have $', player1bank)  
                            else:
                                print('Bad guess. You lost your turn')
                                currentplayer = Next_Player(currentplayer)
                                FirstTurn = False
                                first_consonant_player_1 = True
                        else:
                            print('Bad guess. You lost your turn')
                            FirstTurn = False
                            first_consonant_player_1 = True

                    if userinput == 'word':
                        def convert(s):
                            new = ''
                            for x in s:
                                new += x
                            return new                            
                        userinput = convert(input('Guess a word: ').lower())
                        word2 = convert(word2)
                        if userinput == word2:
                            print(word2, 'is correct!')
                            print('You won the round! You won $', player1bank)
                            FirstTurn = False
                            first_consonant_player_1 = True
                            roundisHappening = 3
                        else:
                            print('That is not the full word. Try again.')
                            FirstTurn = False
                            first_consonant_player_1 = True

            else:
                print('That is not in the word. You lost your turn')
                currentplayer = Next_Player(currentplayer)
                print(currentplayer, "it is your turn")
                first_consonant_player_1 = True
                FirstTurn = False
        else:
            print('That is not one letter and a consonant. Try again')
            first_consonant_player_1 = True
            FirstTurn = False
#ROUND 3
while roundisHappening == 3:
    print(' '.join(word_underlist3))
    if player1bank + player1bank2 > player2bank + player2bank2 and player1bank + player1bank2 > player3bank + player1bank2:
        currentplayer = player1
    if player2bank + player2bank2 > player1bank + player1bank2 and player2bank + player2bank2 > player3bank + player3bank2:
        currentplayer = player2
    if player3bank + player3bank2 > player1bank + player1bank2 and player3bank + player3bank2 > player2bank2 + player2bank2:
        currentplayer = player3
    print(currentplayer, "Congratulations, you made it to final round")
    userinput = input("Enter R, S, T, L, N, E and 3 consonants of your choice and a vowel of your choice:")
    if len(userinput) == 1 and userinput in consonants or vowels:
            if userinput in word3:
                for position in range(len(word3)):
                    if word3[position] == userinput:
                        word_underlist3[position] = userinput
    final_guess = input("What is your final guess?")
    if final_guess == word3:
        if currentplayer == player1:
            player1bank3 = 3000
        if currentplayer == player2:
            player2bank3 = 3000
        if currentplayer == player3:
            player3bank3 = 3000
        roundisHappening = 4
    else:
        roundisHappening = 4
