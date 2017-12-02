# For the quiz_final function 'sys.exit()', for stopping the program if the user types no
import sys


# For the quiz_final function, so the percentage of how many questions the user got correct can be calculated 
import operator


# Variable for the first line printed in the program (it introduces the user to the quiz program)
introduction = 'Hello! Welcome to the "Ultimate Quiz"!'

paragraph_filled_static = []
paragraph_filled_modified = paragraph_filled_static

options = ['easy', 'medium', 'hard']
questions = ['What word could fill in __1__ ? ', 'What word could fill in __2__ ? ', 'What word could fill in __3__ ? ', 'What word could fill in __4__ ? ']
blanks = ['__1__', '__2__', '__3__', '__4__']

easy = options[0]
medium = options[1]
hard = options[2]

first_question_location = 0
initial_win_counter = 0

# Dictionary for the answers of each level of difficulty
data = {
    'easy':{
        'answers': ['Earth', 'Moon', 'Sun', 'stars'], 
        'accepted_answers': ['earth', 'moon', 'sun', 'Stars'], 
        'paragraph': '''As you may know, __1__ is the planet we live on. The __2__ takes 27.3 days both to rotate on its axis and to orbit __1__. This rock is the magnificent object we see every night above us. Isn't it weird that the __2__ is bigger than something like Pluto? The __3__ is a massive ball of energy that is one of the most important resources necessary for human survival. Our __3__ is one of many __4__ in the vast universe. __4__ fill our sky everynight and we see them as flickering little dots. We see those __4__ as they were many years in the past. This happens because of the amount of time it takes for the light to reach our eyes on __1__.'''
    },
    'medium':{
        'answers': ['Intelligence', 'machines', 'neural', 'Learning'], 
        'accepted_answers': ['intelligence', 'Machines', 'Neural', 'learning'], 
        'paragraph': '''Many people are afraid of what Artificial __1__ will bring and ultimately do to humanity. Will __2__ take over the world and cause an apocolypse like its depicted in the movies? __2__ that are programmed with Artificial __1__, have a "mind" composed of many __3__ networks. These __3__ networks combined seem to simulate a fully self-aware brain. A similar concept to Artificial __1__, is Deep __4__! Deep __4__ is when a bot is given certain rules or parameters to a game or program, having it learn from mistakes to improve. When do you think we will consider __2__ as normal to our societies?'''
    },
    'hard':{
        'answers': ['program', 'advance', 'science', 'quantum'], 
        'accepted_answers': ['Program', 'Advance', 'Science', 'Quantum'],
        'paragraph': '''Do you think learning to __1__ will soon be a necessity in all societies? Those who make __1__s may be considered the most powerful people in the world as technology becomes exponentially __2__d. __4__ computing, Artificial Intelligence, and general computer __3__s bring concepts and ideas that will contribute to the technological __2__ments we will experience in the coming years. Computer __3__ is the scientific study of how computers work and what their limits are. __4__ mechanics has come a long way since it has been theorized and is now helping __4__ computing emerge.'''
    }
}


# Must print introduction here, so it is the first line printed in the program
print introduction


# The paragraphUpdate function takes in 4 inputs, 'paragraph', 'toReplace', 'answer', and level
def paragraph_update(paragraph, toReplace, answer, level):
    '''The function outputs the first input, the 'paragraph' string, after going 
    through each element in that string and replacing all elements that have the 
    'toReplace' string in it or are equivalent to the 'toReplace' string with the 
    'answer' string while keeping all puncuation and grammar effects consistent.'''
    replaced = []
    paragraph_list = paragraph.split()
    period = '.'
    list_index = 0
    for item in paragraph_list:
        if period in paragraph_list[list_index - 1] and toReplace in item:
            item = item.replace(toReplace, answer)
            item = item.title()
            replaced.append(item)
        elif period not in paragraph_list[list_index - 1] and toReplace in item:
            item = item.replace(toReplace, answer)
            replaced.append(item)
        else:
            replaced.append(item)
        list_index += 1
    return ' '.join(replaced)


def paragraph_update_assist(level):
    '''The paragraph_update_assist function takes in one input, level, to help 
    determine which difficulty level is chosen in order to get the corresponding 
    paragraph. The function then creates a list of the paragraphs with answers 
    filled in incriments, so other functions can call from the list to print out 
    the needed paragraph depending on the circumstances.'''
    question_index = 0
    max_index = (len(blanks) - 1)
    paragraph_filled_modified.append(data[level]['paragraph'])
    while question_index < max_index:
        answer = data[level]['answers'][question_index]
        paragraph = paragraph_filled_modified[question_index]
        blank = blanks[question_index]
        paragraph_filled_modified.append(paragraph_update(paragraph, blank, answer, level))
        question_index += 1
    answer = data[level]['answers'][max_index]
    paragraph = paragraph_filled_modified[max_index]
    blank = blanks[max_index]
    paragraph_filled_modified.append(paragraph_update(paragraph, blank, answer, level))


# Below is a function for getting the amount of guesses the user chooses for the quiz
def get_guess_amount():
    guess_amount = raw_input('How many guesses would you like? Please type a number: ')
    while str(guess_amount) == '0' or guess_amount.isdigit() is False:
        print 'Error: ' + str(guess_amount) + ' is invalid'
        guess_amount = raw_input('How many guesses would you like? Please type a number: ')
    print 'Guess amount set to ' + str(guess_amount)
    return int(guess_amount)


# If the user chooses 1 guess for each question, the 'guesses' in the text that begins each quiz will be changed to 'guess' for grammar purposes
def text_for_guess_amount(guess_counter):
    '''The guess_text function takes in 1 input, guess_counter, to once again establish 
    the guesses the user has for each question in the quiz.'''
    if guess_counter == 1:
        print
        print 'You will be given ' + str(guess_counter) + ' guess to answer each question!'
        print 'Good Luck!'
        return guess_counter
    else:
        print
        print 'You will be given ' + str(guess_counter) + ' guesses to answer each question!'
        print 'Good Luck!'
        return guess_counter


# User chooses level of difficulty
def difficulty():
    """The user is prompted to choose a level of difficulty (easy, medium, or hard) 
    until a message, which establishes the chosen level as the set difficulty and 
    terminates the difficulty() function, is printed. Otherwise, the function is 
    repeated until satisfied."""
    difficulty_choice = raw_input('Please type your choice of difficulty: | easy | medium | hard | ---> ')
    option_index = 0
    while difficulty_choice in [easy, medium, hard]:
        if difficulty_choice == options[option_index] and option_index < len(options):
            paragraph_update_assist(difficulty_choice)
            print 'Difficulty level set to ' + options[option_index] + '!'
            print
            guess_counter = text_for_guess_amount(get_guess_amount())
            print
            print 'Fill in the blanks for the paragraph below:'
            return quiz_level(options[option_index], guess_counter, first_question_location, initial_win_counter)
        elif difficulty_choice != options[option_index] and option_index < (len(options) - 1):
            option_index += 1
    print 'Error: ' + difficulty_choice + ' is not a difficulty level'
    return difficulty()
  
  
def quiz_to_end(level, guess_counter, question_number, win_counter):
    '''The quiz_to_end function takes in four inputs: level, guess_counter, 
    question_number, and win_counter. The level input is used for calling the 
    correct "answers" from the data dictionary and then sent to the quiz_level 
    function if applicable. The guess_counter input is sent to the quiz_level 
    function if applicable. The question_number input is for determining which 
    question is the user currently on, so the other functions that call on the 
    input can print the correct statements depending on circumstances. The win_counter 
    input is used for the quiz_final function, so it can know how many questions 
    the user answered correctly.'''
    print 'The answer is: ' + data[level]['answers'][question_number]
    if question_number < (len(questions) - 1):
        question_number += 1
        return quiz_level(level, guess_counter, question_number, win_counter)
    else:
        print
        print 'Here is the paragraph fully filled:'
        print
        print paragraph_filled_modified[(len(paragraph_filled_modified) - 1)]
        return quiz_final(win_counter)


# The quiz_level function takes in 4 inputs: level, guess_counter, question_number, and win_counter
def quiz_level(level, guess_counter, question_number, win_counter):
    '''The level input is for determining which difficulty level quiz is occuring. 
    The guess_counter is a constant variable that represents the user's amount of 
    guesses chosen. The question_number determines which question is being asked. 
    The win_counter is a variable that counts how many questions the user got 
    correct, so the quiz_final function can determine how many questions the user 
    was able to answer right.'''
    # I know requirements say that functions should be no longer than 18 lines (This one is 29 lines), but I found this much more efficient to code than making other functions
    guesses = guess_counter
    while guesses > 0 and question_number < len(questions):
        print
        print paragraph_filled_modified[question_number]
        print 
        if raw_input(questions[question_number]) in {data[level]['answers'][question_number], data[level]['accepted_answers'][question_number]}:
            win_counter += 1
            print '\nThat is correct!'
            break
        else:
            guesses = guesses - 1
            print '\nThat is incorrect!'
            if guesses == 1:
                print 'You have ' + str(guesses) + ' guess left!'
            elif guesses == 0:
                print 'You have no guesses left!'
            else:
                print 'You have ' + str(guesses) + ' guesses left!'
    return quiz_to_end(level, guess_counter, question_number, win_counter)
        

# The quiz_final functions takes 1 input, win_counter, to determine how many questions the user answered correctly
def quiz_final(win_counter):
    '''This function is the end of the quiz for all difficulty levels. It prints 
    the user's score using the win_counter variable and then allows the user to 
    restart the program or stop it by typing yes or no. The user can type yes and 
    no as upper or lowercase.'''
    print
    print 'You got ' + str(win_counter) + ' out of 4 correct!'
    print 'Thanks for playing! Your final score is ' + str(operator.truediv(win_counter, len(questions)) * 100) + '% !'
    print
    restart = raw_input('Would you like to play again? Please type Yes or No: ')
    while True:
        if restart in ('Yes', 'yes'):
            print
            del paragraph_filled_modified[:]
            return difficulty()
        elif restart in ('No', 'no'):
            return sys.exit()
        else:
            print 'Error: ' + str(restart) + ' is invalid'
            restart = raw_input('Would you like to play again? Please type Yes or No: ')


# This begins the entire quiz program
print difficulty()
