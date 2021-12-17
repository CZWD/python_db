def reset_database(cur):

  #cur.execute('''
  #  GRANT ALL ON SCHEMA public TO python_user;
  #''')

  #cur.execute('''
  #  DROP SCHEMA public CASCADE;
  #  CREATE SCHEMA public;
  #  AUTHORIZATION python_user;
  #''')

  cur.execute('''
    drop owned by python_user;
  ''')

  cur.execute('''
    create table "player" (
        id serial primary key,
        first_name text not null,
        last_name text,
        created_at timestamp default current_timestamp
    );''')

  cur.execute('''
    create table "game" (
        id serial primary key,
        title text not null,
        metacritic int,
        pegi text,
        release Date,
        added_by int references public.player(id),
        created_at timestamp default current_timestamp
    );''')

  cur.execute('''
    create table "genre" (
        id serial primary key,
        name text
    );''')

  cur.execute('''
    create table "games_genre" (
        game_id int references public.game(id),
        genre_id int references public.genre(id)
    );''')

  # On ajoute l'autorisation à l'utilisateur sur toutes les tables et les séquences une fois créées
  cur.execute('grant all privileges on all tables in schema public to python_user;')
  cur.execute('grant all privileges on all sequences in schema public to python_user;')

