from collections import Counter
import random
import sys, os

class Hangman():
	'''
	Constructor
	'''
	def __init__(self, filePath=''):
		if (filePath == ''):
			self.file = os.path.join(sys.path[0], 'word-files\\google-10000-english-usa-no-swears.txt')
		else:
			self.file = filePath			# File path global variable
		self._word = self.findWord()		# The word associated with a single hangman instance - private
		while len(self._word) < 3:			# Re-roll if word is less than 3 characters long
			self._word = self.findWord()

	'''
	Finds a word based on a randomly generated number line. Closes
	file after finding word
	'''
	def findWord(self):
		try:
			file = open(self.file, 'r')
		except (FileNotFoundError):
			raise FileNotFoundError('Please include a text file to read from, or create your own.')
		lineNum = self.randomWordLine()		# Generate random number
		for i, line in enumerate(file):		# automatic counter, assigns numbers to words in txt file
			if i == lineNum:
				word = line.strip()			# Find word on line number and set word
			elif i > lineNum:
				break						# Exit 'find word' loop
		file.close()
		return word

	'''
	Generates random number given a range from 0 to max # of lines of file
	'''
	def randomWordLine(self):
		numWords = 0
		with open(self.file) as f:
			for i, l in enumerate(f):
				numWords = i + 1 						# Obtains the number of words in file
		randomNumber = random.randrange(0, numWords)	# From 0 to number of words in file, generate random number
		return randomNumber

	'''
	Starts Hangman game
	'''
	def start(self):
		lives = 6
		secretWord = list(self._word)
		guesses = []
		correctGuesses = list('_'*len(secretWord))
		mistakes = 0
		prompt = '\nWhat letter would you like to guess? '
		nonAlphaErr = 'Please type a roman alphabet letter.\n'
		tooManyErr = 'Hey, are you taking this seriously?\n'
		multLetterErr = 'Please only type one letter per guess.\n'
		alreadyGuessedErr = 'You\'ve already guessed this letter. Try again.\n'
		correctGuessStr = 'Correct!'
		wrongGuessErr = 'Sorry, your letter isn\'t in the word.\n'
		gameOverErr = 'Oops! You\'ve run out of lives. The word was: ' + self._word + '.\nYour guesses were:'
		winMessage = 'Congratulations! You figured out the word! It was: ' + ''.join(secretWord) +'.'

		while (lives > 0):
			print(''.join(correctGuesses))
			print('Guesses thus far:', guesses)
			letter = input(prompt).lower()
			print('Your guess was: \''+letter+'\'')

			if (self.checkWin(correctGuesses, secretWord)):
				print('\n'+winMessage)
				break

			if (not letter.isalpha()):
				print(nonAlphaErr)
				mistakes += 1
				if (mistakes == 3):
					print(tooManyErr)
			elif (len(letter) > 1):
				print(multLetterErr)
				mistakes += 1
				if (mistakes == 3):
					print(tooManyErr)
			else:
				if (letter in guesses):
					print(alreadyGuessedErr)
				else:
					guesses.append(letter)
					if (letter in secretWord):
						indices = self.findAll(secretWord, letter)
						for i in indices:
							correctGuesses[i] = letter
						print(correctGuessStr, '\n', ''.join(correctGuesses))
					else:
						print(wrongGuessErr)
						lives -= 1
			
			if (self.checkWin(correctGuesses, secretWord)):
				print('\n'+winMessage)
				break

		if (lives == 0):
			print(gameOverErr, guesses)

	'''
	Returns path string of input file
	'''
	def getWordFile(self):
		return self.file

	'''
	Returns letter frequency in a word
	'''
	def findAll(self, word, letter):
		return [i for i, guess in enumerate(word) if guess == letter]

	'''
	Returns true if the sorted guess characters are equivalent to the sorted secret word characters
	'''
	def checkWin(self, guesses, secretWord):
		return sorted(guesses) == sorted(secretWord)

if __name__ == '__main__':
	Hangman().start()