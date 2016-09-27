# Hangman Game
import getpass
import hangman_pic

print("Time to play hangman!")
word = getpass.getpass("Enter the word to guess: ")
word = word.lower()

guesses = ''
turns = 0
current_state = "WORD: " 

def print_word (word, guesses,turns, current_state):
	''' For the new letter guessed. 
		- Update the letters guessed
		- Update the hangman
		- Update any new letters in the word
	'''
	current_state = "WORD: "
	for char in word:      
		if char in guesses:    
			current_state = current_state + char + " " 
		else:
			current_state = current_state + "_ "   
			  	                 
	# Print the hangman state
	print(hangman_pic.HANGMAN[turns])
	print(current_state, "             ", "Letters Guessed:", guesses) 
	return current_state

# Print initial hangman
chars_missing = print_word(word, "",0, "_")	

while True:  
	# ask the user go guess a character
	print("---------------------------------------------------------")
	guess = input("\nGuess a character:") 
	guesses += guess 

	# if the guess is not found in the secret word
	if guess not in word:  
		print(" ** Wrong Guess ** ")
		turns += 1  

	# Print the hangman state
	current_state = print_word(word, guesses,turns, current_state)	

	# Losing Condition
	if turns == 10 :           
		print(" The word was: ", word) 
		break

	# Winning Condition
	if "_" not in current_state:        
		print("\nYou Win! Congratulations\n")
		break 


