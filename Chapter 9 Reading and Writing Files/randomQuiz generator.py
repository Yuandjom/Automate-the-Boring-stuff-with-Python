# python 3
#randomQuizgenerator.py Create quizzes with questions and answers in 
#random order , along with the answer key .
import random 
#The quiz data . Keys are states and values are their capitals.
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : ' Scaramento',
    'Colorado': 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Loisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts': "Boston",
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire': 'Concord',
    'New jersey': 'Trenton',
    'New Mexico': 'Santa fe',
    'New York' : 'Albany',
    'North Carolina': 'Raleigh',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salth Lake City',
    'Vermont':'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming':'Cheyenne',
}
#Generate 35 quiz files 
for quizNum in range(35):
    # Create the quiz and answer key files 
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # Write out the header for the quiz 
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + f'State Captials Quiz (Form{quizNum+1})') #leave a lot of spacing 
    quizFile.write('\n\n')
    
    #Shuffle the order of the states.
    states = list(capitals.keys()) #need to list() if not they will be in tuple page 115
    random.shuffle(states)

    #TODO: Loop through all 50 states , making a question for each 
