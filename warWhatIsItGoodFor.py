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
	

if __name__ == '__main__':
	main()