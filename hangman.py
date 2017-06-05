from collections import Counter
import random

class Hangman():
	'''
	Constructor
	'''
	def __init__(self, filePath):
		self.file = filePath # File path global variable
		self._word = self.findWord() # The word associated with a single hangman instance - private
		while len(self._word) < 3: # Re-roll if word is less than 3 characters long
			self._word = self.findWord()

	'''
	Finds a word based on a randomly generated number line. Closes
	file after finding word
	'''
	def findWord(self):
		file = open(self.file)
		lineNum = self.randomWordLine()
		for i, line in enumerate(file):
			if i == lineNum:
				word = line.strip()
			elif i > lineNum:
				break
		file.close()
		return word

	'''
	Generates random number given a range from 0 to max # of lines of file
	'''
	def randomWordLine(self):
		numWords = 0
		with open(self.file) as f:
			for i, l in enumerate(f):
				numWords = i + 1
		randomNumber = random.randrange(0, numWords)
		return randomNumber

h = Hangman('word-files/google-10000-english-usa-no-swears.txt')