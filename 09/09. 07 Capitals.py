import random
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 
}

state, capital = random.choice(list(capitals_dict.items()))
answer = 0
while True:
    answer = input(f"What is the capital of {state} :").lower()
    if answer == "exit":
        print(f"The capital of '{state}' is '{capital}'.")
        print("Goodbye")
        break
    elif answer == capital.lower():
        print("Correct! Nice job.")
        break
