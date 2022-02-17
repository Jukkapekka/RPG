import random
import time
from gameinfo import available_races
from gameinfo import racial_bonus
from story import welcome
from story import stat_explain
from gameinfo import stats
from gameinfo import bonus_map
from dieroll import dice
from dieroll import d4
from gameinfo import important_person

#print(welcome)

Name = input('Your name, please: ').title()
Nickname = input('What would you like your character to be called? ').title()
print('Pick a race from the following list that you want to play as: ')


#try to make a function where the races get printed. Try a for-loop.
def playable_race(available_races):
    for x in available_races:
        print(x)
    return available_races
playable_race(available_races)
race = input("").title()

def racial(stats):
    stats[bonus_map.get(race)] += 1
    return stats

print(f'Alright, so, you are {Name}, your character is called {Nickname}, and you\'re going to be a {race}? Very well! \nBecause you\'ve chosen to play as a {race}, you have an increased {bonus_map.get(race)}.')
print(stat_explain)


#intro for the quest, for whom do they have to get the medicine?
#print(random.choice(important_person).title())