import random
from faker import Faker

faker = Faker()

def player_first_name():
    return faker.first_name()

def player_last_name():
    return faker.last_name()

def player():
  return (player_first_name(), player_last_name())

def game_name():
    return ' '.join(faker.words())

def metacritic():
    return random.randrange(20, 95, 1)

def pegi():
    list = ['NA', 3, 7, 12, 16, 18]
    return random.choice(list)

def release():
    return faker.date()

def game():
    added_by = random.randint(1,10)
    return (game_name(), metacritic(), pegi(), release(), random.choice([added_by, None]) )
  
def genre():
  list = ['Action', 'Adventure', 'Role-playing', 'Simulation', 'Strategy', 'Sports', 'MMO']
  return random.choice(list)

def games_genre():
  return (random.randint(1, 100), random.randint(1, 7))