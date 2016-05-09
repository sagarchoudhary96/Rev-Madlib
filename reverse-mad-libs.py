# String and its Answers to be filled in beginner level
begi = ["python" , "udacity" , "programming" , "2"]
stringa = "\nHello Reviewer !! My name is Sagar Choudhary. I am learning __1__ \
 programming language which is used to build this game from www. __2__ .com. My course name is intro to __3__\
 nanodegree. This is my stage __4__ submission."

# String and its Answers to be filled in intermediate level
inter = ["arrow" , "b" , "f" , "f4"]
stringb = "There are various types of windows keyboard shortcuts.\
 The __1__ keys are used to move cursor around the text. Crtl + __2__ is used to make the\
 text bold. Ctrl + shift + __3__ is used to change the fonts.\
 Alt + __4__ is used to close the active item, or exit the active app."

# String and its Answers to be filled in proficient level
prof = ["mercury" , "saturn" , "4" , "titan" , "milkyway"]
stringc = "__1__ is the closest planet to the sun. \
 The second largest planet in our solar system which is also famous for rings around it is __2__ . \
 It has __3__ main group of Rings. The name of largest moon of saturn is __4__ . \
 It is located in __5__ galaxy."

# String and its Answers to be filled in experienced level
exp = ["jaipur" , "1799" , "lalchand" , "pyramidal"]
stringd = "Hawa Mahal is located in the Indian city of __1__ .  The structure \
was built in __2__ by Maharaja Sawai Pratap Singh. __3__ Ustad was the architect of this unique structure. \
The palace is a five-storey __4__ shaped monument."

# String and its Answers to be filled in expert level
exper = ["members" , "void" , "::" , "overloading" , "global"]
stringe = "Variables of a class are called __1__ . A function with no return \
 type is declared as __2__ . __3__ is known as scope resolution operator. \
 When the same function is used for multiple operations it is known as function __4__ . \
 Variables that are alive and active throughout the program are called __5__ variables."


def run(ans , stri):
	'''
	This is the main function which executes the level selected by player
	it takes the question as string argument and its answers as list type
	argument this function executes till the player has completed the chosen
	level and return nothing
	'''
	i = 0
	while(i < len(ans)):

		blank = raw_input("What should go in blank " + str(i + 1) + " ? ")

		'''
		the conditions check if the word typed by user is in the answers
		list and has the right blank
		'''
		if(word_in_pos(blank , ans) != None and i == ans.index(blank)):

			# the following replaces the blank with the correct answer filled
			stri = stri.split()
			j = stri.index("__" + str(i + 1) + "__")
			word = stri[j]
			word = word.replace("__" + str(i + 1) + "__" , blank)
			stri[j] = word

			# it now iterates to next blank
			i = i + 1
			print "\nThat's Correct!\n"
			stri = " ".join(stri)
			print stri + "\n"

		else:
			print("\nSorry! Wrong Answer. Please try again")
			
	print "Congratulations you cleared the level !!\n"
	return


def word_in_pos(word, answers):

	'''
	Checks if a word filled by the player is present in the answers
	list or not. it returns the word itself if present else return none.
	'''

	for pos in answers:
		if pos in word:
			return pos
	return None


def main():

	'''
	Its the main block or function of the game. It takes the
	control of the user to the player.
	'''

	play = "yes"


	while(play == "yes"):

		print "\n" + " " * 23 + "Welcome to Reverse Mad-libs !!"
		print "\n1. beginner" + " " * 3 + "2. intermediate" + " " * 3 + "3.\
 proficient" + " " * 3 + "4. experienced" + " " * 3 + "5. expert"

		level = raw_input("\nType in your Expertise Level : ")

		print " " * 23 + "\nNote: All answers should be in smallcaps"

		# this will execute the beginner level
		if(level == "beginner"):
			print stringa + "\n"
			run(begi , stringa);

		# this will execute the intermediate level
		elif(level == "intermediate"):
			print stringb + "\n"
			run(inter, stringb)

		# this will execute the proficient level
		elif(level == "proficient"):
			print stringc + "\n"
			run(prof, stringc)

		# this will execute the experienced level
		elif(level == "experienced"):
			print stringd + "\n"
			run(exp, stringd)

		# this will execute the expert level
		elif(level == "expert"):
			print stringe + "\n"
			run(exper, stringe)

		play = raw_input("Do You want to play again ? (yes/no) ")
		if(play == "no"):
			print "ThankYou for playing :)"


if __name__ == "__main__":
        main()
