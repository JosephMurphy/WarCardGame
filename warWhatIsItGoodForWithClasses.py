#this application will hopefully allow a player to simulate a game of WAR against a computer but will more than likely fail
import random

#create a class to store valuse for the card hands
class CardHand(object):
	def __init__(self, deck, playingCard, warCardPile):
		self.deck = deck
		self.playingCard = playingCard
		self.warCardPile = warCardPile

#create global variables to be used for the decks
player = CardHand(None,None,[])		
computer = CardHand(None,None,[])

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
	#define the decks as blank lists
	player.deck = []
	computer.deck = []
	
	while len(cardDeck) > 0:
		#deal to the player
		player.deck.append(cardDeck[len(cardDeck)-1])
		del cardDeck[len(cardDeck)-1]
		
		#deal to the computer
		computer.deck.append(cardDeck[len(cardDeck)-1])
		del cardDeck[len(cardDeck)-1]
	
def compareCards():
	#create a bool variable to keep track of whether the game is over or not.
	gameOver = False
	
	#While loop to continue playing the game as long as gameOver equals false
	while gameOver == False:
		#First, check to make sure the game is not over
		if isGameOver(gameOver) == True:
			gameOver = True

		#draw the playing cards from the decks.
		player.playingCard = player.deck[0]
		computer.playingCard = computer.deck[0]
	
		#Display the cards to the player
		print "You play: " + player.playingCard
		print "The computer plays: " + computer.playingCard
	
		#remove the playing cards from the players' decks
		del player.deck[0]
		del computer.deck[0]
	
		#Check if the playing card is a face card or not. If it is, assign the card a numerical value. Creating new variable player/computerNumberCard for comparisons.
		playerNumberCard = checkForFaceCard(player.playingCard)
		computerNumberCard = checkForFaceCard(computer.playingCard)
		
		#Begin comparing the cards
		#The player wins
		if playerNumberCard > computerNumberCard:
			print "You win this battle!"
			#add the playing cards to the player's deck
			player.deck.append(player.playingCard)
			player.deck.append(computer.playingCard)
		#The computer wins
		elif playerNumberCard < computerNumberCard:
			print "You lost this battle D:"
			#add the playing cards to the computer's deck
			computer.deck.append(player.playingCard)
			computer.deck.append(computer.playingCard)
		#If there is a tie
		elif playerNumberCard == computerNumberCard:
			print "\nIts a tie! This means WAR!\n"	
			war()

def war():
	#first, make sure that the players have enough remaining cards in their deck for a regular game of WAR (4)
	if len(player.deck) > 4 and len(computer.deck) > 4:
		#create the "WAR hands", the cards that are burned during the war. This is done by adding them to the .warCardPile
		i = 0
		while i < 3:
			player.warCardPile.append(player.deck[i])
			computer.warCardPile.append(computer.deck[i])
			
			i += 1
		
		#remove the cards that were just added to the warCardPiles from the players' decks. This is three cards
		i = 0
		while i < 3:
			del player.deck[0]
			del computer.deck[0]
			
			i += 1
			
		#Now draw each players' playing card for the WAR
		player.playingCard = player.deck[0]
		computer.playingCard = computer.deck[0]
		
		#remove the playing cards from the deck
		del player.deck[0]
		del computer.deck[0]
		
		#Check if the playing card is a face card or not. If it is, assign the card a numerical value. Creating new variable player/computerNumberCard for comparisons.
		playerNumberCard = checkForFaceCard(player.playingCard)
		computerNumberCard = checkForFaceCard(computer.playingCard)
		
		#Begin comparing the cards
		#The player wins
		if playerNumberCard > computerNumberCard:
			print "You win this battle of WAR!"
			#Add the playing cards to the player's deck
			player.deck.append(player.playingCard)
			player.deck.append(computer.playingCard)
			#Add the warCardPiles to the player's deck
			for card in player.warCardPile:
				player.deck.append(card)
			for card in computer.warCardPile:
				player.deck.append(card)
			
			#reset the warCardPiles for the next game of war
			player.warCardPile = []
			computer.warCardPile = []
			
		#The computer wins
		if playerNumberCard < computerNumberCard:
			print "You lost this battle of WAR D:"
			#Add the playing cards to the computer's deck
			computer.deck.append(player.playingCard)
			computer.deck.append(computer.playingCard)
			#Add the warCardPiles to the computer's deck
			for card in player.warCardPile:
				computer.deck.append(card)
			for card in computer.warCardPile:
				computer.deck.append(card)
				
			#reset the warCardPiles for the next game of war
			player.warCardPile = []
			computer.warCardPile = []

		#There is a tie DOUBLE WAR
		if playerNumberCard == computerNumberCard:
			print "Its a tie! This means ANOTHER WAR (Oh the humanity!)"
			#Add the playing cards to their respective warCardPiles so they are not lost in the ether when re-running the war() function
			player.warCardPile.append(player.playingCard)
			computer.warCardPile.append(computer.playingCard)
			war()
	#If one player does not have enough cards for a full WAR, draw so their last remaining card is their playing card
	else:
		#check to see which deck has the least amount of cards
		if len(player.deck) > len(computer.deck):
			shortestDeck = len(computer.deck)
		elif len(player.deck) < len(computer.deck):
			shorestDeck = len(player.deck)
		else:
			shortestDeck = len(player.deck)
		
		#Create the warCardPiles based on the shortest deck length. do this only if the shortest deck length is greater than 1
		if shortestDeck > 1:
			#create the pile
			i = 0
			while i < (shortestDeck - 10:
				player.warCardPile.append(player.deck[i])
				computer.warCardPile.append(computer.deck[i])
			
				i += 1
			#remove the cards in the pile from the deck
			i = 0
			while i < (shortestDeck - 1):
				del player.deck[i]
				del computer.deck[i]
			
				i += 1
		#Now draw each players' playing card for the WAR
		player.playingCard = player.deck[0]
		computer.playingCard = computer.deck[0]
		
		#remove the playing cards from the deck
		del player.deck[0]
		del computer.deck[0]
		
		#Check if the playing card is a face card or not. If it is, assign the card a numerical value. Creating new variable player/computerNumberCard for comparisons.
		playerNumberCard = checkForFaceCard(player.playingCard)
		computerNumberCard = checkForFaceCard(computer.playingCard)
		
		#Begin comparing the cards
		#The player wins
		if playerNumberCard > computerNumberCard:
			print "You win this battle of WAR!"
			#Add the playing cards to the player's deck
			player.deck.append(player.playingCard)
			player.deck.append(computer.playingCard)
			#Add the warCardPiles to the player's deck
			for card in player.warCardPile:
				player.deck.append(card)
			for card in computer.warCardPile:
				player.deck.append(card)
			
			#reset the warCardPiles for the next game of war
			player.warCardPile = []
			computer.warCardPile = []
			
		#The computer wins
		if playerNumberCard < computerNumberCard:
			print "You lost this battle of WAR D:"
			#Add the playing cards to the computer's deck
			computer.deck.append(player.playingCard)
			computer.deck.append(computer.playingCard)
			#Add the warCardPiles to the computer's deck
			for card in player.warCardPile:
				computer.deck.append(card)
			for card in computer.warCardPile:
				computer.deck.append(card)
				
			#reset the warCardPiles for the next game of war
			player.warCardPile = []
			computer.warCardPile = []

		#There is a tie DOUBLE WAR
		if playerNumberCard == computerNumberCard:
			print "Its a tie! This means ANOTHER WAR (Oh the humanity!)"
			#Add the playing cards to their respective warCardPiles so they are not lost in the ether when re-running the war() function
			player.warCardPile.append(player.playingCard)
			computer.warCardPile.append(computer.playingCard)
			war()

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
	
#The game is over when one of the playing decks has no more cards. This function checks to see if either deck has cars remaining.			
def isGameOver(gameOver):
	if (len(player.deck) == 0):
        gameOver = True
        print "You lost the game!"
        return gameOver
    elif (len(computer.deck) == 0):
        gameOver = True
        print "You WON the game! Hurray!"
        return gameOver
    else:
        gameOver = False
        print "Keep playing!"
        return gameOver
	
def main():
	#defining an unshuffled deck in a list
	originalDeck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
	print "This is the unshuffled deck: \n " + str(originalDeck)
	
	#creating a new deck using the shuffleDeck function
	newDeck = shuffleDeck(originalDeck)
	print "The deck has now been shuffled: \n" + str(newDeck)
		
	#Deal the cards to the player and the computer
	dealCard(newDeck)
	print player.deck
	print computer.deck
	
	#Start the game once the decks have been dealt.
	compareCards()
	
if __name__ == '__main__':
	main()
