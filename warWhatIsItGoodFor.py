#this application will hopefully allow a player to play a game of WAR against a computer
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
		
	
	

#deal the cards to the player and computer
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

def compareCards(playerDeck, computerDeck, playerDiscard, computerDiscard):
	#keep playing until one player has no more cards in their main deck
	while len(playerDeck) > 0 or len(computerDeck) > 0:
	
		#assign the player cards
		playerCard = playerDeck[len(playerDeck)-1]
		computerCard = computerDeck[len(computerDeck)-1]
		#delete the cards from their decks
		del playerDeck[len(playerDeck)-1]
		del computerDeck[len(computerDeck)-1]
		print "You play: " + str(playerCard)
		print "The computer plays: " + str(computerCard)
	
		#check if the player cards are face cards or not
		playerNumberCard = checkForFaceCard(playerCard)
		computerNumberCard = checkForFaceCard(computerCard)

		if playerNumberCard > computerNumberCard:
			print "You win this battle!"
			#the player won, so add both their card and the computer's card to their discard
			playerDiscard.append(playerCard)
			playerDiscard.append(computerCard)

		elif playerNumberCard < computerNumberCard:
			print "You lost this battle D:"
			#the computer wins, so add both cards to the computer's discard
			computerDiscard.append(playerCard)
			computerDiscard.append(computerCard)

		elif playerNumberCard == computerNumberCard:
			print "Its a tie! This means WAR! \n\n\n"
			war(playerCard, computerCard, playerNumberCard, computerNumberCard, playerDeck, computerDeck, playerDiscard, computerDiscard)
	
	print playerDiscard
	print computerDiscard
	

#For ties, perform the W-A-R actions
def war(playerCard, computerCard, playerNumberCard, computerNumberCard, playerDeck, computerDeck, playerDiscard, computerDiscard):
	#first, make sure the players have enough cards for a regular WAR (4)
	if len(playerDeck) > 4 and len(computerDeck) > 4:
		#create the "WAR hands", the cards that are burned during the war
		playerWarHand = [playerDeck[len(playerDeck)-1],playerDeck[len(playerDeck)-2], playerDeck[len(playerDeck)-3]]
		computerWarHand = [computerDeck[len(computerDeck)-1],computerDeck[len(computerDeck)-2], computerDeck[len(computerDeck)-3]]
		#remove these cards from the decks
		for row in playerWarHand:
			del playerDeck[len(playerDeck)-1]
		for row in computerWarHand:
			del computerDeck[len(computerDeck)-1]
		#draw the card to be used in the WAR
		playerWarCard = playerDeck[len(playerDeck)-1]
		computerWarCard = computerDeck[len(computerDeck)-1]
		
		print "You play: " + str(playerWarCard)
		print "The computer plays: " + str(computerWarCard)
		
		#check for face cards
		playerNumberWarCard = checkForFaceCard(playerWarCard)
		computerNumberWarCard = checkForFaceCard(computerWarCard)
		
		if playerNumberWarCard > computerNumberWarCard:
			print "You win this battle of WAR!"
			#the player won, so add both their card and the computer's card to their discard
			playerDiscard.append(playerCard)
			playerDiscard.append(computerCard)
			
			#append the WAR hands
			for card in playerWarHand:
				playerDiscard.append(card)
			for card in computerWarHand:
				playerDiscard.append(card)
			

		elif playerNumberWarCard < computerNumberWarCard:
			print "You lost this battle of WAR D:"
			#the computer wins, so add both cards to the computer's discard
			computerDiscard.append(playerCard)
			computerDiscard.append(computerCard)
			
			#append the WAR hands
			for card in playerWarHand:
				computerDiscard.append(card)
			for card in computerWarHand:
				computerDiscard.append(card)

		elif playerNumberWarCard == computerNumberWarCard:
			print "Its a tie! This means WAR, AGAIN!"
			war(playerCard, computerCard, playerNumberCard, playerNumberCard, playerDeck, computerDeck, playerDiscard, computerDiscard)
		
	return  playerDeck, computerDeck, playerDiscard, computerDiscard
		
	

#checks to see if the card is a face card. If it is, returns a number value for comparison			
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
	#defining an unshuffled deck
	originalDeck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
	print originalDeck
	#creating a new deck
	newDeck = shuffleDeck(originalDeck)
	print newDeck
	
	#Deal cards to the player and computer.  This involves creating two arrays of cards
	playerDeck, computerDeck = dealCard(newDeck)
	print playerDeck
	print computerDeck
	
	#create discard piles for the player and computer
	playerDiscard = []
	computerDiscard = []
	
	compareCards(playerDeck, computerDeck, playerDiscard, computerDiscard)
	
	

if __name__ == '__main__':
	main()