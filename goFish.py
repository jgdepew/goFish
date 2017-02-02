import random

class Player(object):
	def __init__(self, name):
		self.name = name
		self.score = 0;
		self.hand = [];
		self.matches = [];

	def playTurn(self, players, deck, turn):
		card = random.randrange(0, len(players[turn].hand))	# will find a random card index from player's hand to request
		requestedPlayer = -1 # will find a random player from which to request a card value
		while requestedPlayer < 0 or requestedPlayer == turn:
			requestedPlayer = random.randrange(0, 4)
		print players[turn].name, "is requesting from player ", players[requestedPlayer].name, "the card value of", players[turn].hand[card].value
		result = players[turn].requestCard(players[requestedPlayer], players[turn].hand[card].value)
		if result == False:
			if len(deck.deck) > 0:
				players[turn].goFish(deck)
				print players[turn].name, "went fish"
			else:
				print players[turn].name, "passed"
		self.findMatches()


	def requestCard(self, player2, value):
		for card in xrange(len(player2.hand)): 
			if player2.hand[card].value == value:
				temp = player2.hand[card]
				player2.hand[card] = player2.hand[len(player2.hand)-1]
				player2.hand.pop()
				
				self.hand.append(temp)
				return True
		return False

	def goFish(self, deck):
		self.hand.append(deck.deck[len(deck.deck)-1])
		deck.deck.pop()

	def drawHand(self, deck):
		for i in range(0, 7):
			self.goFish(deck)
		matches = self.findMatches()
		while matches == True:
			matches = self.findMatches

	def findMatches(self): # will find matches in self's hand. 
		for i in xrange(len(self.hand)):
			for j in xrange(len(self.hand)):
				if i == j:
					continue
				else:
					if self.hand[i].value == self.hand[j].value:
						print self.name, " found a match!"
						print self.hand[i].value + "of" + self.hand[i].suit + "matches with" + self.hand[j].value + "of" + self.hand[j].suit		
						self.score += 1
						self.discardMatch(i, j)
						return True
		return False

	def printHand(self):
		for i in range(0, len(self.hand)):
			print self.hand[i].value + " of " + self.hand[i].suit

	def discardMatch(self, i, j):
		self.printHand()

		self.matches.append(self.hand[i])
		self.matches.append(self.hand[j])
		print "DISCARDING:", self.hand[i].value, self.hand[i].suit
		print "DISCARDING:", self.hand[j].value, self.hand[j].suit
		if (j != (len(self.hand)-1) and i != (len(self.hand)-2)) and (j != (len(self.hand)-2) and i != (len(self.hand)-1)):	# if both aren't the last indexes of the hand, swap both
			temp = self.hand[i]
			self.hand[i] = self.hand[len(self.hand)-1]
			self.hand[len(self.hand)-1] = temp

			temp = self.hand[j]
			self.hand[j] = self.hand[len(self.hand)-2]
			self.hand[len(self.hand)-2] = temp
		elif j == (len(self.hand)-1) and i != (len(self.hand)-2): # if j is the last index of the hand but not i, swap i to second last index
			temp = self.hand[i]
			self.hand[i] = self.hand[len(self.hand)-2]
			self.hand[len(self.hand)-2] = temp
		elif j ==(len(self.hand)-2) and i != (len(self.hand)-1): # if j is the second last index of the hand but not i, swap i to last index
			temp = self.hand[i]
			self.hand[i] = self.hand[len(self.hand)-1]
			self.hand[len(self.hand)-1] = temp
		elif j != (len(self.hand)-1) and i == (len(self.hand)-2): # if i is the last index of the hand but not j, swap j to second last index
			temp = self.hand[j]
			self.hand[j] = self.hand[len(self.hand)-2]
			self.hand[len(self.hand)-2] = temp
		elif j != (len(self.hand)-2) and i == (len(self.hand)-1): # if i is the second last index of the hand but not j, swap j to last index
			temp = self.hand[j]
			self.hand[j] = self.hand[len(self.hand)-1]
			self.hand[len(self.hand)-1] = temp		
		
		# if both i and j are the last two indexes, it will just pop off the end

		self.hand.pop()
		self.hand.pop()


class Deck(object):

	def __init__(self):
		values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
		suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
		deck = []
		for suit in range(0, 4):
			for value in range(0,13):
				deck.append(Card(values[value], suits[suit]))
		self.deck = deck

	def shuffle(self):
		for i in range(0,1000):
			idx1 = random.randrange(0, 52)
			idx2 = random.randrange(0, 52)
			while(idx1 == idx2):
				idx1 = random.randrange(0, 52)
				idx2 = random.randrange(0, 52)
			self.swap(idx1, idx2, self.deck)
		return self.deck

	def swap(self, i, j, arr):
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp

	def printDeck(self):
		for i in range(0, len(self.deck)):
			print self.deck[i].value + " of " + self.deck[i].suit

class Card(object):
	def __init__(self, value, suit):
		self.value = value;
		self.suit = suit;

def createPlayers(deck):
	player0 = Player('Joe')
	player1 = Player('Jam')
	player2 = Player('Jeff')
	player3 = Player('Evan')
	player1.drawHand(deck)
	player2.drawHand(deck)
	player3.drawHand(deck)
	player0.drawHand(deck)
	players = [player0, player1, player2, player3]
	return players

def printResults(players):
	maxScore = players[0]
	for i in range(1, len(players)):
		if players[i].score > maxScore.score:
			maxScore = players[i]
	print maxScore.name, " wins with a score of ", maxScore.score




def playGame():
	newDeck = Deck()
	newDeck.shuffle()
	players = createPlayers(newDeck)
	turn = 0

	while len(players[0].hand) > 0 and len(players[1].hand) > 0 and len(players[2].hand) > 0 and len(players[3].hand) > 0:
		if turn == 0:
			players[turn].playTurn(players, newDeck, turn)
			turn += 1
		elif turn == 1:
			players[turn].playTurn(players, newDeck, turn)
			turn += 1
		elif turn == 2:
			players[turn].playTurn(players, newDeck, turn)
			turn += 1
		else:
			players[turn].playTurn(players, newDeck, turn)
			turn = 0

	printResults(players)


playGame()
