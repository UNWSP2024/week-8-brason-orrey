import random

# Dictionary of U.S. states and their capitals
states_capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
    'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
    'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
    'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
    'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# Initialize counters for correct and incorrect answers
correct_count = 0
incorrect_count = 0

# Convert the dictionary keys (states) to a list and shuffle it
states = list(states_capitals.keys())
random.shuffle(states)  # Shuffle to randomize the order of questions

# Quiz the user on each state once
for state in states:
    capital = states_capitals[state]  # Get the correct capital for the chosen state

    # Ask the user to guess the capital
    user_answer = input(f"What is the capital of {state}? ").strip()

    # Check if the answer is correct
    if user_answer.lower() == capital.lower():
        print("Correct!")
        correct_count += 1
    else:
        print(f"Incorrect. The capital of {state} is {capital}.")
        incorrect_count += 1

# Display the final score
print(f"\nQuiz complete! You got {correct_count} correct and {incorrect_count} incorrect.")
