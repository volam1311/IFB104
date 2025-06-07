#-----Statement of Authorship----------------------------------------#
#
# This is an individual assessment task for QUT's teaching unit
# IFB104, "Building IT Systems", Semester 2, 2024. By submitting
# this code I agree that it represents my own work. I am aware of
# the University rule that a student must not act in a manner
# which constitutes academic dishonesty as stated and explained
# in QUT's Manual of Policies and Procedures, Section C/5.3
# "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
# Put your student number here as an integer and your name as a
# character string:
#
student_number = 11912839
student_name = "Phuc Lam Vo"
#
# NB: All files submitted for this assessable task will be subjected
# to automated plagiarism analysis using a tool such as the Measure
# of Software Similarity (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#

#-----Assessment Task 1 Description----------------------------------#
#
# This assessment task tests your skills at processing large data
# sets, creating reusable code and following instructions to retrieve
# information. The incomplete Python program below is
# missing a crucial function. You are required to complete this
# function so that when the program runs it interacts with the user
# to perform a range of functionalities.
#  See the instructions in part A and part B for full details.
#
# Note that this assessable assignment is in multiple parts,
# simulating incremental release of instructions by a paying
# "client". This single template file will be used for all parts
# and you will submit your final solution as this single Python 3
# file only, whether or not you complete all requirements for the
# assignment.
#
# This file relies on one other Python modules but all of your code
# must appear in this file only. You may not change any of the code
# in the other module and you should not submit the other module
# with your solution. The markers will use their own copies of the
# other module to test your code, so your solution will not work
# if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#

#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from sys import exit as abort


# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
	print('\nUnable to run: No student number supplied',
	'(must be an integer), aborting!\n')
	abort()
if not isinstance(student_name, str):
	print('\nUnable to run: No student name supplied',
	'(must be a character string), aborting!\n')
	abort()



#-----Student's Solution---------------------------------------------#
#
# Complete the assignment by replacing the dummy function below with
# your own function and any other functions needed to support it.
# All of your solution code must appear in this section. Do NOT put
# any of your code in any other sections and do NOT change any of
# the provided code except as allowed by the comments in the next
# section.
#
# All of your code goes in, or is called from, this function.
#Import necessary library before doing the tasks
from re import findall
from re import sub
import doctest
def make_book_list(booklist): 
	"""
	>>> make_book_list('1. the art of coding: mastering the craft of software development. 2. journey through time: a historical exploration of ancient civilizations. 3. mindful living: techniques for a balanced and peaceful life. 4. the science of success: strategies for achieving your goals. 4. creative writing: unlocking your imagination and storytelling skills. 5. healthy eating: a guide to nutritious and delicious meals. 6. financial freedom: steps to achieve economic independence. 7. the world of art: understanding and appreciating visual masterpieces. 7. digital marketing: tactics for building an online presence. 9. the power of habit: transforming your life one step at a time. ') #Test 1
	[['the art of coding', 'mastering the craft of software development'], ['journey through time', 'a historical exploration of ancient civilizations'], ['mindful living', 'techniques for a balanced and peaceful life'], ['the science of success', 'strategies for achieving your goals'], ['creative writing', 'unlocking your imagination and storytelling skills'], ['healthy eating', 'a guide to nutritious and delicious meals'], ['financial freedom', 'steps to achieve economic independence'], ['the world of art', 'understanding and appreciating visual masterpieces'], ['digital marketing', 'tactics for building an online presence'], ['the power of habit', 'transforming your life one step at a time']]
	>>> make_book_list('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') #Test 2(edge cases, the user enter a random word)
	[]
	>>> make_book_list('11.art of coding, this an edge cases to test whether the function works') #Test 3 (edge cases, the user enter the wrong format)
	[]
	>>> make_book_list('11. art of coding: name lam. 12.art of edge cases, 13: lam vo, stop this case') #Test 4(edge cases, right format mixed with the wrong format)
	[['art of coding', 'name lam']]
	"""
	books = []
	# Find the title by finding the number and the dot, find the subtitle which is before the ':' and then put them in a list
	new_book_list = findall(r'[0-9]+\. ([a-zA-Z ]+): ([a-zA-Z ]+)\.',booklist) 
	for titles, subtitles in new_book_list:
		books.append([titles.strip(),subtitles.strip()])
	return books

def make_index(booklist,index_type):
	"""
	>>> make_index([['the art of coding', 'mastering the craft of software development'], ['journey through time', 'a historical exploration of ancient civilizations'], ['mindful living', 'techniques for a balanced and peaceful life'], ['the science of success', 'strategies for achieving your goals'], ['creative writing', 'unlocking your imagination and storytelling skills'], ['healthy eating', 'a guide to nutritious and delicious meals'], ['financial freedom', 'steps to achieve economic independence'], ['the world of art', 'understanding and appreciating visual masterpieces'], ['digital marketing', 'tactics for building an online presence'], ['the power of habit', 'transforming your life one step at a time']],0)
	[['the', [0, 3, 7, 9]], ['art', [0, 7]], ['of', [0, 3, 7, 9]], ['coding', [0]], ['journey', [1]], ['through', [1]], ['time', [1]], ['mindful', [2]], ['living', [2]], ['science', [3]], ['success', [3]], ['creative', [4]], ['writing', [4]], ['healthy', [5]], ['eating', [5]], ['financial', [6]], ['freedom', [6]], ['world', [7]], ['digital', [8]], ['marketing', [8]], ['power', [9]], ['habit', [9]]]
	>>> make_index([['the art of coding', 'mastering the craft of software development'], ['journey through time', 'a historical exploration of ancient civilizations'], ['mindful living', 'techniques for a balanced and peaceful life'], ['the science of success', 'strategies for achieving your goals'], ['creative writing', 'unlocking your imagination and storytelling skills'], ['healthy eating', 'a guide to nutritious and delicious meals'], ['financial freedom', 'steps to achieve economic independence'], ['the world of art', 'understanding and appreciating visual masterpieces'], ['digital marketing', 'tactics for building an online presence'], ['the power of habit', 'transforming your life one step at a time']],1)
	[['mastering', [0]], ['the', [0]], ['craft', [0]], ['of', [0, 1]], ['software', [0]], ['development', [0]], ['a', [1, 2, 5, 9]], ['historical', [1]], ['exploration', [1]], ['ancient', [1]], ['civilizations', [1]], ['techniques', [2]], ['for', [2, 3, 8]], ['balanced', [2]], ['and', [2, 4, 5, 7]], ['peaceful', [2]], ['life', [2, 9]], ['strategies', [3]], ['achieving', [3]], ['your', [3, 4, 9]], ['goals', [3]], ['unlocking', [4]], ['imagination', [4]], ['storytelling', [4]], ['skills', [4]], ['guide', [5]], ['to', [5, 6]], ['nutritious', [5]], ['delicious', [5]], ['meals', [5]], ['steps', [6]], ['achieve', [6]], ['economic', [6]], ['independence', [6]], ['understanding', [7]], ['appreciating', [7]], ['visual', [7]], ['masterpieces', [7]], ['tactics', [8]], ['building', [8]], ['an', [8]], ['online', [8]], ['presence', [8]], ['transforming', [9]], ['one', [9]], ['step', [9]], ['at', [9]], ['time', [9]]]
	>>> make_index([],0) #Test 2(edge cases, there is no booklist)
	[]
	"""
	word_list = []
	before_words = []
	for index, book in enumerate(booklist):
		words = book[index_type].split() #Split the title or subtitle
		for word in words:
			word = word.lower()
			# Conver the word into the lowercase, if it has been seen before, we append the index of the word into the word_list
			if word in before_words:
				for entry in word_list:
					if entry[0] == word:
						entry[1].append(index)
						break
			else: #if it has not been seen before, we append the word into the before_words list and append the word and its index into the word_list
				before_words.append(word)
				word_list.append([word, [index]])
	return word_list

def title_length(booklist): 
	"""
	>>> title_length([['the art of coding', 'mastering the craft of software development'], ['journey through time', 'a historical exploration of ancient civilizations'], ['mindful living', 'techniques for a balanced and peaceful life'], ['the science of success', 'strategies for achieving your goals'], ['creative writing', 'unlocking your imagination and storytelling skills'], ['healthy eating', 'a guide to nutritious and delicious meals'], ['financial freedom', 'steps to achieve economic independence'], ['the world of art', 'understanding and appreciating visual masterpieces'], ['digital marketing', 'tactics for building an online presence'], ['the power of habit', 'transforming your life one step at a time']]) #Test 1
	2.9
	>>> title_length([]) #Test 2(edge cases, empty booklist)
	0
	"""
	if not booklist: #Handle edge cases, if there is no booklist then return 0
		return 0
	else:
		total_title_length =  sum(len(title.split()) for title, subtitle in booklist) #calculate the number of words in the title
		average_length = total_title_length / len(booklist) # calculate the average_length by dividing the total length by the length of the booklist
		return average_length

def search_word(word, subtitle_index, booklist): 
	"""
	>>> search_word('life',[['mastering', [0]], ['the', [0]], ['craft', [0]], ['of', [0, 1]], ['software', [0]], ['development', [0]], ['a', [1, 2, 5, 9]], ['historical', [1]], ['exploration', [1]], ['ancient', [1]], ['civilizations', [1]], ['techniques', [2]], ['for', [2, 3, 8]], ['balanced', [2]], ['and', [2, 4, 5, 7]], ['peaceful', [2]], ['life', [2, 9]], ['strategies', [3]], ['achieving', [3]], ['your', [3, 4, 9]], ['goals', [3]], ['unlocking', [4]], ['imagination', [4]], ['storytelling', [4]], ['skills', [4]], ['guide', [5]], ['to', [5, 6]], ['nutritious', [5]], ['delicious', [5]], ['meals', [5]], ['steps', [6]], ['achieve', [6]], ['economic', [6]], ['independence', [6]], ['understanding', [7]], ['appreciating', [7]], ['visual', [7]], ['masterpieces', [7]], ['tactics', [8]], ['building', [8]], ['an', [8]], ['online', [8]], ['presence', [8]], ['transforming', [9]], ['one', [9]], ['step', [9]], ['at', [9]], ['time', [9]]],[['the art of coding', 'mastering the craft of software development'], ['journey through time', 'a historical exploration of ancient civilizations'], ['mindful living', 'techniques for a balanced and peaceful life'], ['the science of success', 'strategies for achieving your goals'], ['creative writing', 'unlocking your imagination and storytelling skills'], ['healthy eating', 'a guide to nutritious and delicious meals'], ['financial freedom', 'steps to achieve economic independence'], ['the world of art', 'understanding and appreciating visual masterpieces'], ['digital marketing', 'tactics for building an online presence'], ['the power of habit', 'transforming your life one step at a time']]) # Test 1 (Handle cases with the word power)
	'Mindful Living;The Superpower of Habit'
	>>> search_word('power',[['mastering', [0]], ['the', [0]], ['craft', [0]], ['of', [0, 1]], ['software', [0]], ['development', [0]], ['a', [1, 2, 5, 9]], ['historical', [1]], ['exploration', [1]], ['ancient', [1]], ['civilizations', [1]], ['techniques', [2]], ['for', [2, 3, 8]], ['balanced', [2]], ['and', [2, 4, 5, 7]], ['peaceful', [2]], ['life', [2, 9]], ['strategies', [3]], ['achieving', [3]], ['your', [3, 4, 9]], ['goals', [3]], ['unlocking', [4]], ['imagination', [4]], ['storytelling', [4]], ['skills', [4]], ['guide', [5]], ['to', [5, 6]], ['nutritious', [5]], ['delicious', [5]], ['meals', [5]], ['steps', [6]], ['achieve', [6]], ['economic', [6]], ['independence', [6]], ['understanding', [7]], ['appreciating', [7]], ['visual', [7]], ['masterpieces', [7]], ['tactics', [8]], ['building', [8]], ['an', [8]], ['online', [8]], ['presence', [8]], ['transforming', [9]], ['one', [9]], ['step', [9]], ['at', [9]], ['time', [9]]],[['the art of coding', 'mastering the craft of software development'], ['journey through time', 'a historical exploration of ancient civilizations'], ['mindful living', 'techniques for a balanced and peaceful life'], ['the science of success', 'strategies for achieving your goals'], ['creative writing', 'unlocking your imagination and storytelling skills'], ['healthy eating', 'a guide to nutritious and delicious meals'], ['financial freedom', 'steps to achieve economic independence'], ['the world of art', 'understanding and appreciating visual masterpieces'], ['digital marketing', 'tactics for building an online presence'], ['the power of habit', 'transforming your life one step at a time']]) #Test 2 (edge cases, no words appear in the list)
	'no book contains power'
	"""
	word = word.lower()
	results = []
	#Search for word in the subtitle and then check where the word appear on the booklist by using its index.
	for entry in subtitle_index:
		if entry[0] == word:
			for index in entry[1]:
				title = booklist[index][0]
				title = sub(r'\bpower\b', 'superpower', title) # Replace the word power by superpower if it appear
				#Split the title into list of words and then formatted by captializing the first word and words that are not 'and', 'of', 'the'
				words = title.split()
				formatted_title = ' '.join([words[0].capitalize()] + [word.capitalize() if word.lower() not in ['the', 'of', 'and'] else word for word in words[1:]])
				results.append(formatted_title)
	if not results: # Handle cases when there are no title that contains the word.
		return f'no book contains {word}'
	else:
		return ";".join(results) 

def word_occurrences(word, index_titles, index_subtitles): #
	"""
	>>> word_occurrences('life',[['the', [0, 3, 7, 9]], ['art', [0, 7]], ['of', [0, 3, 7, 9]], ['coding', [0]], ['journey', [1]], ['through', [1]], ['time', [1]], ['mindful', [2]], ['living', [2]], ['science', [3]], ['success', [3]], ['creative', [4]], ['writing', [4]], ['healthy', [5]], ['eating', [5]], ['financial', [6]], ['freedom', [6]], ['world', [7]], ['digital', [8]], ['marketing', [8]], ['power', [9]], ['habit', [9]]], [['mastering', [0]], ['the', [0]], ['craft', [0]], ['of', [0, 1]], ['software', [0]], ['development', [0]], ['a', [1, 2, 5, 9]], ['historical', [1]], ['exploration', [1]], ['ancient', [1]], ['civilizations', [1]], ['techniques', [2]], ['for', [2, 3, 8]], ['balanced', [2]], ['and', [2, 4, 5, 7]], ['peaceful', [2]], ['life', [2, 9]], ['strategies', [3]], ['achieving', [3]], ['your', [3, 4, 9]], ['goals', [3]], ['unlocking', [4]], ['imagination', [4]], ['storytelling', [4]], ['skills', [4]], ['guide', [5]], ['to', [5, 6]], ['nutritious', [5]], ['delicious', [5]], ['meals', [5]], ['steps', [6]], ['achieve', [6]], ['economic', [6]], ['independence', [6]], ['understanding', [7]], ['appreciating', [7]], ['visual', [7]], ['masterpieces', [7]], ['tactics', [8]], ['building', [8]], ['an', [8]], ['online', [8]], ['presence', [8]], ['transforming', [9]], ['one', [9]], ['step', [9]], ['at', [9]], ['time', [9]]] ) #Test 1
	2
	>>> word_occurrences('neural',[['the', [0, 3, 7, 9]], ['art', [0, 7]], ['of', [0, 3, 7, 9]], ['coding', [0]], ['journey', [1]], ['through', [1]], ['time', [1]], ['mindful', [2]], ['living', [2]], ['science', [3]], ['success', [3]], ['creative', [4]], ['writing', [4]], ['healthy', [5]], ['eating', [5]], ['financial', [6]], ['freedom', [6]], ['world', [7]], ['digital', [8]], ['marketing', [8]], ['power', [9]], ['habit', [9]]], [['mastering', [0]], ['the', [0]], ['craft', [0]], ['of', [0, 1]], ['software', [0]], ['development', [0]], ['a', [1, 2, 5, 9]], ['historical', [1]], ['exploration', [1]], ['ancient', [1]], ['civilizations', [1]], ['techniques', [2]], ['for', [2, 3, 8]], ['balanced', [2]], ['and', [2, 4, 5, 7]], ['peaceful', [2]], ['life', [2, 9]], ['strategies', [3]], ['achieving', [3]], ['your', [3, 4, 9]], ['goals', [3]], ['unlocking', [4]], ['imagination', [4]], ['storytelling', [4]], ['skills', [4]], ['guide', [5]], ['to', [5, 6]], ['nutritious', [5]], ['delicious', [5]], ['meals', [5]], ['steps', [6]], ['achieve', [6]], ['economic', [6]], ['independence', [6]], ['understanding', [7]], ['appreciating', [7]], ['visual', [7]], ['masterpieces', [7]], ['tactics', [8]], ['building', [8]], ['an', [8]], ['online', [8]], ['presence', [8]], ['transforming', [9]], ['one', [9]], ['step', [9]], ['at', [9]], ['time', [9]]] ) #Test 2(word not in the booklist)
	0
	"""
	word = word.lower()
	count = 0
	# Search for word in both title and subtitle, and then count the number of the occurences by calculating the length of the index
	for entry in index_titles + index_subtitles:
		if entry[0] == word:
			count += len(entry[1])
	return count

def interact():
	#Ask for user booklist, if the length of the booklist is less than 50 then user has to type again
	user_booklist = input("Please enter your booklist:")
	while len(user_booklist) < 50:
		user_booklist = input("Your booklist is too short, please enter at least 50 characters.")
	formatted_booklist = make_book_list(user_booklist) #Convert the booklist into new format
	index_titles=make_index(formatted_booklist, 0) #Make title index
	index_subtitles=make_index(formatted_booklist, 1) #Make subtitle index
	# Handle user choices by asking the user to enter the number they want, if it is 1 we return the average title length, if it is 2 we return the matching titles of the word that users search for and finally if it is 3 we return how many time the word appears
	# While the user enter choice 1 or 2 or 3 we can ask them to enter the action again. If the user enter other numbers we ask them to enter the number again
	# The user enter number 0 to exit the program
	while True:
		print("Choose an action:")
		print("1.Get the average length of the title of the books")
		print("2.Search for a word in subtitles")
		print("3.Count word occurrences in titles and subtitles")
		print("0.Exit the program")
		user_choice = input("Enter your choice (1-3):")
		if user_choice == '1':
			print("Average title length:",title_length(formatted_booklist))
		elif user_choice == '2':
			user_word = input("Enter a word to search:")
			print("Matching titles:",search_word(user_word,index_subtitles, formatted_booklist))
		elif user_choice =='3':
			user_input_word = input("Enter a word to count occurrences:")
			print("Word occurrences:",word_occurrences(user_input_word,index_titles, index_subtitles))
		elif user_choice == '0':
			break
		else:
			print("Error! Enter the number again")
			continue
	print("Goodbye!")

#-----Main Program to Run Student's Solution-------------------------#
#You must NOT change any of the code in this section.
if __name__ == "__main__":
	print(doctest.testmod(verbose = True, optionflags= doctest.REPORT_ONLY_FIRST_FAILURE)) #Test all the function
	interact()
