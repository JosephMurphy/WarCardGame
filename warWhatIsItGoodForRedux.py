#this application will hopefully allow a player to simulate a game of WAR against a computer but will more than likely fail
import random

#Take the deck and shuffle. random.shuffle would work but I wanted to do it myself to make sure I could
def shuffleDeck(cardDeck):
	"""
	random.shuffle(cardDeck)
	return cardDeck
	"""
	#define the new deck as blank array
	newCardDeck = []
	while len(cardDeck) > 0:
		rand = random.randrange(len(cardDeck))
		newCardDeck.append(cardDeck[rand])
		del cardDeck[rand]
	return newCardDeck
	
#deal the cards to the player and computer. This works by creating two new lists for the player and the computer decks. 
#The last card in the unshuffled deck is then alternatively placed in the player deck and the computer deck, then deleted.
#Don't ask why I chose the last card instead of the first card, I just did and can't really explain it.
def dealCard(cardDeck):
	playerDeck = []
	computerDeck = []
	
	while len(cardDeck) > 0:
		#deal to the player
		playerDeck.append(cardDeck[len(cardDeck)-1])
		del cardDeck[len(cardDeck)-1]
		
		#deal to the computer
		computerDeck.append(cardDeck[len(cardDeck)-1])
		del cardDeck[len(cardDeck)-1]
	
	return playerDeck, computerDeck
	
#Checks to see if the game is over. If either the computer deck or player deck have a length of zero, they are out of cards and the game is over.
def isGameOver(playerDeck, computerDeck, gameOver):
    if (len(playerDeck) == 0):
        gameOver = True
        print "You lost the game!"
        return gameOver
    elif (len(computerDeck) == 0):
        gameOver = True
        print "You WON the game! Hurray!"
        return gameOver
    else:
        gameOver = False
        print "Keep playing!"
        return gameOver


def compareCards(playerDeck, computerDeck):
	#bool variable to keep track of if the game is over or not
	gameOver = False
	#Keep playing the game as long as 'gameOver' does not equal True
	while gameOver == False:	
		#First, begin by checking to see if the game is over or not
		if isGameOver(playerDeck, computerDeck, gameOver) == True:
			gameOver = True
		
		#assign the player cards by picking the first card in the decks
		print "You have " + str(len(playerDeck)) + " cards left"
		print "The computer has " + str(len(computerDeck)) + " cards left"
		playerCard = playerDeck[0]
		computerCard = computerDeck[0]
		
		#delete the cards from their decks. The winner will have both cards added to their deck later.
		del playerDeck[0]
		del computerDeck[0]
		
		#Show the player the cards being played.
		print "You play: " + str(playerCard)
		print "The computer plays: " + str(computerCard)
		
		#check if the player cards are face cards or not. If it is a face card, assign it a numerical value. Creating variable 'player/computerNumberCard' so the face card symbol isn't destroyed for later printing
		playerNumberCard = checkForFaceCard(playerCard)
		computerNumberCard = checkForFaceCard(computerCard)
		
		#If the player wins the hand
		if playerNumberCard > computerNumberCard:
			print "You win this battle!"
			#the player won, so add both their card and the computer's card to their discard
			playerDeck.append(playerCard)
			playerDeck.append(computerCard)	
		#If the computer wins the hand	
		elif playerNumberCard < computerNumberCard:
			print "You lost this battle D:"
			#the computer wins, so add both cards to the computer's discard
			computerDeck.append(playerCard)
			computerDeck.append(computerCard)
		#If the hand is a tie, oh my!
		elif playerNumberCard == computerNumberCard:
			print "\nIts a tie! This means WAR!\n"	
			playerDeck, computerDeck = war(playerCard, computerCard, playerNumberCard, computerNumberCard, playerDeck, computerDeck)

			
#WAR! for what to do when the hand ends in a draw.
def war(playerCard, computerCard, playerNumberCard, computerNumberCard, playerDeck, computerDeck):

	#first, make sure the players have enough cards for a regular WAR (4)
	if len(playerDeck) > 4 and len(computerDeck) > 4:
		#create the "WAR hands", the cards that are burned during the war
		playerWarHand = [playerDeck[0],playerDeck[1], playerDeck[2]]
		computerWarHand = [computerDeck[0],computerDeck[1], computerDeck[2]]
		
		#remove these cards from the decks
		for row in playerWarHand:
			del playerDeck[0]
		for row in computerWarHand:
			del computerDeck[0]
		
		#draw the card to be used in the WAR
		playerWarCard = playerDeck[0]
		computerWarCard = computerDeck[0]
		#delete the war cards from the decks
		del playerDeck[0]
		del computerDeck[0]
		
		#Display the cards being played.
		print "You play: " + str(playerWarCard)
		print "The computer plays: " + str(computerWarCard)
		
		#check for face cards. If it is a face card, assign it a numerical value. Creating variable 'player/computerNumberCard' so the face card symbol isn't destroyed for later printing
		playerNumberWarCard = checkForFaceCard(playerWarCard)
		computerNumberWarCard = checkForFaceCard(computerWarCard)
		
		if playerNumberWarCard > computerNumberWarCard:
			print "You win this battle of WAR!"
			#the player won, so add both their card and the computer's card to their discard
			playerDeck.append(playerCard)
			playerDeck.append(computerCard)
			playerDeck.append(playerWarCard)
			playerDeck.append(computerWarCard)
			
			#append the WAR hands
			for card in playerWarHand:
				playerDeck.append(card)
			for card in computerWarHand:
				playerDeck.append(card)
		
		elif playerNumberWarCard < computerNumberWarCard:
			print "You lost this battle of WAR D:"
			#the computer wins, so add both cards to the computer's discard
			computerDeck.append(playerCard)
			computerDeck.append(computerCard)
			computerDeck.append(playerWarCard)
			computerDeck.append(computerWarCard)
			
			#append the WAR hands
			for card in playerWarHand:
				computerDeck.append(card)
			for card in computerWarHand:
				computerDeck.append(card)

		elif playerNumberWarCard == computerNumberWarCard:
			print "Its a tie! This means WAR, AGAIN!"
			playerDeck, computerDeck = war(playerCard, computerCard, playerNumberCard, computerNumberCard, playerDeck, computerDeck)		
	#when there are less than 4 cards for WAR, use the length of the smallest deck -1 for the war hand, last card for WAR card
	else:
		#finish later
	return playerDeck, computerDeck

def checkForFaceCard(card):
	if isinstance(card, int) == False:
		if card == 'J':
			card = 11
		elif card == 'Q':
			card = 12
		elif card == 'K':
			card = 13
		elif card == 'A':
			card = 14
	return card
def main():
	#defining an unshuffled deck in a list
	originalDeck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
	print "This is the unshuffled deck: \n " + str(originalDeck)
	
	#creating a new deck using the shuffleDeck function
	newDeck = shuffleDeck(originalDeck)
	print "The deck has now been shuffled: \n" + str(newDeck)
	
	#Deal cards to the player and computer.  This involves creating two arrays of cards
	playerDeck, computerDeck = dealCard(newDeck)
	print "This is the player's deck: \n" + str(playerDeck)
	print "This is the computer's deck: \n" + str(computerDeck)
	
	"""#bool variable to keep track of if the game is over or not
	gameOver = False
	
	while gameOver == False:
	
		#Check to see if the game is over.
		if isGameOver(playerDeck, computerDeck, gameOver) == True:
			gameOver = True"""
	#Play the game by comparing the cards of the player deck and the computer deck
	playerDeck, computerDeck = compareCards(playerDeck, computerDeck)


if __name__ == '__main__':
	main()
