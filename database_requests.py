import generate

def fill_db(cur):
  # On ajoute 10 utilsateurs
  for i in range(10):
    cur.execute('insert into "player" (first_name, last_name) values (%s, %s);', generate.player() )

  # On ajoute 100 jeux
  for i in range(100):
    cur.execute('''
      insert into "game" (title, metacritic, pegi, release, added_by) values (%s, %s, %s, %s, %s);''', generate.game() )

  genre_list = ["Action", "Adventure", "Role-playing", "Simulation", "Strategy", "Sports", "MMO"]

  # On crée des genre de jeux
  for i in genre_list:
    cur.execute('''
      insert into "genre" (name) values (%s);''', (i,) )


  # On definit des genres aux jeux
  for i in range(100):
    cur.execute('''
      insert into "games_genre" (game_id, genre_id) values (%s, %s);''', generate.games_genre() )

def get_top_games(cur):
  cur.execute('''
    select
      g.title,
      g.metacritic,
      date_part('year', g."release") as release_year
    from game g
    where
      g.metacritic = (
          select max(metacritic)
          from game
          where date_part('year', "release") = date_part('year', g."release")
      )
    order by release_year''')

def get_worst_games(cur):
  cur.execute('''
    select
      g.title,
      g.metacritic,
      date_part('year', g."release") as release_year
    from game g
    where
      g.metacritic = (
          select min(metacritic)
          from game
          where date_part('year', "release") = date_part('year', g."release")
      )
    order by release_year''')

def get_users_games(cur):
  cur.execute('''
    select
      g.added_by,
      count(g.added_by),
      round(avg(g.metacritic))
    from game g
    group by g.added_by

  ''')

def count_games_by_genre(cur):
  cur.execute('''
    select
      g.genre_id,
      count(g.genre_id)
    from games_genre g
    group by g.genre_id
  ''')

def export_to_csv(cur):
  data = cur.fetchall()
  field_names = [("title", "metacritic", "release_year")]
  data = field_names + data

  data_string = "\n".join("%s;%s;%s" % rows for rows in data )

  with open('./exports/stats.csv', 'w') as file:
    file.write(data_string)

def parse_game(gametuple):
  (id, title, added_at, metacritic, pegi, release, added_by) = gametuple
  return {
    '_id': id,
    'title': title,
    'added_at': added_at,
    'added_by': added_by,
    'infos': {
      'metacritic': metacritic,
      'pegi': pegi,
      'release': release,
      'genres': []
    }
  }

def game_table(cur):
    cur.execute('select * from "game"')
    res = cur.fetchall()

    games = list(map(parse_game, res))

