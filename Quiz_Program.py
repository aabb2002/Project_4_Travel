# A quiz program that tests your kownledge on topics like art, sports, and space. 
# The user inputs what topic they want to test on and it's validated to make sure it's an offered topic.
# The user answers 5 questions and are told if they are wrong or correct.
# At the end of the quiz they are told how many they got right out of 5 and have the option of
# ending the program or taking another quiz.

total_score = 0

def main():
    topic_choices = ['art', 'space', 'sports']

    # I forgot how to do validation with while loops in python so I adapted this loop I found.
    # Source:https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
    while True:
        topic = input('Would you like a art, space, or sports questions? ')
        if topic.lower() not in topic_choices:
            print('Not a valid choice.')
        else:
            break
    
    # Show user questions based on topic selection
    if topic.lower() == 'art':
        topic_art(topic)
    elif topic.lower() == 'space':
        topic_space(topic)
    elif topic.lower() == 'sports':
        topic_sports(topic)

    
    

def topic_art(topic):
    # I had forgotten how to let functions access variables outside it's scope so I looked it up
    # Source:https://www.w3schools.com/python/python_scope.asp
    global total_score
    
    # Dictionary with topic questions and they're correct answers
    art_questions = {'Who painted the Mona Lisa?':'Leonardo Da Vinci', 
    'What precious stone is used to make the artist\'s pigment ultramarine?':'Lapiz lazuli',
    'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?':'Chicago',
    'Which kid\'s TV characters are named after Renaissance artists?':'Teenage Mutant Ninja Turtles',
    'The graphite in an artist\'s pencil is made of what chemical element?':'Carbon'}

    # Displays questions
    for question in art_questions:
        print(question)
        answer = input('Enter your answer: ')
        if answer.lower() == art_questions[question].lower():
            print('Correct!')
            total_score += 1
        else:
            print('Sorry the correct is ' + art_questions[question])

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 5.')

    if total_score == 5:
        print('You got all the answers correct!')
    
    # User can take a different test if they want to or end program
    restart = input('Would you like to take a different quiz? Enter Yes or No: ')
    if restart.lower() == 'yes':
        total_score = 0
        main()
    else:
        print('Goodbye')
        exit()

# The following functions copy the same structure as the previous
def topic_space(topic):

    global total_score

    space_questions = {'Which planet is closest to the sun?':'Mercury',
    'Which planet spins in the opposite direction to all the others in the solar system?':'Venus',
    'How many moons does Mars have?':'2',
    'What was the first human-made object to leave the solar system?':'Voyager 1',
    'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?':'Meteor'}

    for question in space_questions:
        print(question)
        answer = input('Enter your answer: ')
        if answer.lower() == space_questions[question].lower():
            print('Correct!')
            total_score += 1
        else:
            print('Sorry the correct is ' + space_questions[question])

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 5.')

    if total_score == 5:
        print('You got all the answers correct!')

    restart = input('Would you like to take a different quiz? Enter Yes or No: ')
    if restart.lower() == 'yes':
        total_score = 0
        main()
    else:
        print('Goodbye')
        exit()

def topic_sports(topic):

    global total_score

    sports_questions = {'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?':'Simone Biles',
    'Which country has won the soccer world cup the most times?':'Brasil',
    'What does MLB stand for?':'Major League Baseball',
    'Which basketball team won the 2016 NBA championship?':'Cleveland Cavaliers',
    'Which boxer fought against Muhammad Ali and won?':'Joe Frazier'}

    for question in sports_questions:
        print(question)
        answer = input('Enter your answer: ')
        if answer.lower() == sports_questions[question].lower():
            print('Correct!')
            total_score += 1
        else:
            print('Sorry the correct is ' + sports_questions[question])

    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of 5.')

    if total_score == 5:
        print('You got all the answers correct!')

    restart = input('Would you like to take a different quiz? Enter Yes or No: ')
    if restart.lower() == 'yes':
        total_score = 0
        main()
    else:
        print('Goodbye')
        exit()


main()