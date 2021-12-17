import psycopg2
import generate
from helpers import reset_database
from database_requests import *


with psycopg2.connect(dbname='tp_python', user='python_user', password='python', host='127.0.0.1', port='5432') as conn:
    with conn.cursor() as cur:

        # A chaque fois qu'on lance le script, on reset la base pour avoir les mêmes résultats
        #reset_database(cur)

        #Remplissage de la bd avec données aléatoires
        #fill_db(cur)

        # On la joue safe et on recompte le nombre d'utilisateurs depuis la base pour plus tard
        cur.execute('select count(*) from "player";')
    
        # Ici on a un [0] car fetchone() renvoi toujours un tuple, même avec une seule valeur
        player_count = cur.fetchone()[0]

        #get_top_games(cur)
        get_users_games(cur)
        #count_games_by_genre(cur)
        data = cur.fetchall()
        print(data)
        #export_to_csv(cur)

        conn.commit()