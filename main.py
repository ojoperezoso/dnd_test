import uuid
import hashlib
import classes

#Game definition
class Game():

    def __init__(self, name, owner, *args, **kwargs):
        self.id = (len(GAMES) + 1)
        self.name = name
        self.owner = owner

    def __str__(self):
        return f'{self.name}, {self.owner}'

    def save(self):
        GAMES.append(self)
        """
        GAMES.append({
                      'id': self.id,
                      'name': self.name,
                      'owner': self.owner,
        })
        """

#Adventure definition
class Adventure():
    def __init__(self, name, gm, diary, *args, **kwargs):
        self.id = (len(ADVENTURES) + 1)
        self.name = name
        self.gm = gm
        self.diary = diary

    def __str__(self):
        return f'{self.name}, {self.gm} - {self.diary}'

    def save(self):
        ADVENTURES.append(self)
        """
        ADVENTURES.append({
                          'id': self.id,
                          'name': self.name,
                          'gm': self.gm,
                          'diary': self.diary
        })
        """

#User definition
class User():
    def __init__(self, name, password, *args, **kwargs):#*args, **kwargs):
        self.id = (len(USERS) + 1)
        self.name = name
        self.password = password #Have to hash it using sha1
        self

    def __str__(self):
        return f'{self.name}'

    def save(self):
        USERS.append(self)
        """
        USERS.append({
                      'id': self.id,
                      'name': self.name,
                      'password': self.password,
        })
        """

#Race definition
class Race():
    def __init__(self, name, puntos, *args, **kwargs):
        self.id = (len(RACES) + 1)
        self.name = name
        self.puntos = puntos


    def __str__(self):
        return f'{self.name}, {self.puntos}'

    def save(self):
        RACES.append(self)
        """
        RACES.append({
                      'id': self.id,
                      'name': self.name,
                      'puntos': self.puntos,
        })
        """

#Classes definition
class Classes():
    def __init__(self, name, *args, **kwargs):
        self.id = (len(CLASSES) + 1)
        self.name = name    
        self

    def __str__(self):
        return f'{self.name}'

    def save(self):
        CLASSES.append(self)
        """
        CLASSES.append({
                        'id': self.id,
                        'name': self.name,
        })
        """



#Character definition
class Character():
    def __init__(self, user_id, name, race_id, class_id, lvl, puntos, *args, **kwargs):
        self.id = (len(CHARACTERS) + 1)
        self.user_id = user_id
        self.name = name
        self.race_id = race_id #fk
        self.class_id = class_id #fk
        self.lvl = lvl
        self.puntos = puntos

    def __str__(self):
        race_name = class_name = user_name = ''
        for race in RACES:
            if race.id == self.race_id:
                race_name = race.name
        for clase in CLASSES:
            if clase.id == self.class_id:
                class_name = clase.name
        for user in USERS:
            if user.id == self.user_id:
                user_name = user.name
        
        return f'Personaje: {self.name}, {race_name} {class_name} level: {self.lvl} puntos: {self.puntos}Usuario: {user_name}'

    def save(self):
        #Calculating Point Modifiers
        #Race Point Modifiers
        race_puntos = RACES[self.race_id - 1].puntos

        for key in race_puntos:
            self.puntos[key] += race_puntos[key]

        CHARACTERS.append(self)
        """
        CHARACTERS.append({
                           'id': self.id,
                           'user_id': self.user_id,
                           'name': self.name,
                           'race_id': self.race_id,
                           'class_id': self.class_id,
                           'lvl': self.lvl,
                           'puntos': self.puntos,
        })
        """

"""

RELATION CREATION
RELATIONS FOR THE MySQL DATABASE

"""

class user_game():
    def __init__(self, game_id, user_id, user_role, *args, **kwargs):
        super(user_game, self).__init__(*args, **kwargs)
        self.game_id = game_id
        self.user_id = user_id
        self.user_role = user_role

    def __str__(self):
        return f'{self.game_id}, {self.user_id} - {self.user_role}'

    def save(self):
        R_USER_GAME.append(self)
        """
        R_USER_GAME.append({
                            'game_id': self.game_id,
                            'user_id': self.user_id,
                            'user_role': self.user_role,
        })
        """



class adventure_game():
    def __init__(self, adventure_id, game_id, *args, **kwargs):
        self.adventure_id = adventure_id
        self.game_id = game_id

    def __str__(self):
        return f'{self.adventure_id}, {self.game_id}'

    def save(self):
        R_ADVENTURE_GAME.append(self)
        """
        R_ADVENTURE_GAME.append({
                                 'adventure_id': self.adventure_id,
                                 'game_id': self.game_id,
        })
        """



class character_adventure():
    def __init__(self, character_id, adventure_id, *args, **kwargs):
        self.character_id = character_id
        self.adventure_id = adventure_id

    def __str__(self):
        return f'{self.character_id}, {self.adventure_id}'

    def save(self):
        R_CHARACTER_ADVENTURE.append(self)
        """
        R_CHARACTER_ADVENTURE.append({
                                      'character_id': self.character_id,
                                      'adventure_id': self.adventure_id,
        })
        """



class user_character():
    def __init__(self, user_id, character_id):
        self.user_id = user_id
        self.character_id = character_id

    def __str__(self):
        return f'{self.user_id}, {self.character_id}'

    def save(self):
        R_USER_CHARACTER.append(self)
        """
        R_USER_CHARACTER.append({
                                 'user_id': self.user_id,
                                 'character_id': self.character_id,
        })
        """
"""
DATABASE

TABLE DECLARATION
TABLES FOR THE MySQL DB

"""
#Tables
GAMES = []
ADVENTURES = []
USERS = []
CLASSES = []
RACES = []
CHARACTERS = []



#Relations
R_USER_CHARACTER = []
R_USER_GAME = []
R_CHARACTER_ADVENTURE = []
R_ADVENTURE_GAME = []
R_CHARACTER_RACE = []
R_CHARACTER_CLASS = []


#INPUT DATA
#Users
user = ''
user = User('ojo','password')
user.save()
user = User('jonarap03', 'password')
user.save()

#Races
race = Race('enano', {'fuerza': 0,'destreza': 0,'constitucion': 2,'inteligencia': 0,'sabiduria': 1,'carisma': 0})
race.save()

#Classes
clase = Classes('guerrero')
clase.save()

#Characters
personaje = Character(1,'Gralok',1,1,1,{'fuerza': 11,'destreza': 10,'constitucion': 13,'inteligencia': 9,'sabiduria': 12,'carisma': 4})
personaje.save()
personaje = Character(2,'Marihuen',1,1,1,{'fuerza': 13,'destreza': 12,'constitucion': 13,'inteligencia': 9,'sabiduria': 11,'carisma': 8})
personaje.save()

#Games
game = Game('First play', 2)
game.save()
game = Game('Second game', 1)
game.save()

#Adventures
adventure = Adventure('Into the abiss',2,1,)
adventure.save()
adventure = Adventure('Out of the abiss',1,1)
adventure.save()

#user_game RELATION
u_g = user_game(1,1,1)
u_g.save()
u_g = user_game(1,2,0)

#user_character RELATION
u_c = user_character(1,1)
u_c.save()
u_c = user_character(2,2)
u_c.save()

#adventure_game RELATION
a_g = adventure_game(1,1)
a_g.save()
a_g = adventure_game(2,1)
a_g.save()

#character_adventure RELATION
c_a = character_adventure(1,1)
c_a.save()
c_a = character_adventure(2,2)
c_a.save()

for game in GAMES:
    print(game)

for adventure in ADVENTURES:
    print(adventure)

for user in USERS:
    print(user)

for clase in CLASSES:
    print(clase)

for race in RACES:
    print(race)

for character in CHARACTERS:
    print(character)


def show_characters(user_id):
    result = []
    for character in CHARACTERS:
        if character.user_id == user_id:
            result.append(character)
    
    return result

def show_games(user_id):
    result = []
    for relation in R_USER_GAME:
        if relation.user_id == user_id:
            for game in GAMES:
                if game.id == relation.game_id:
                    result.append(game)
                    
    return result

def show_adventures(user_id):
    result = []

    for game_relation in R_USER_GAME:
        if game_relation.user_id == user_id:
            for adv_relation in R_ADVENTURE_GAME:
                if adv_relation.game_id == game_relation.game_id:
                    for adventure in ADVENTURES:
                        if adventure.id == adv_relation.adventure_id:
                            result.append(adventure)

    return result



def menu():
    CURRENT_USER = {} #{id,name,}
    sel = ''
    print('login')
    user_login = input('user name\n>>>')

    while not CURRENT_USER:
        for user in USERS:
            if user_login == user.name: #user['name'] == user:
                password = input('password\n>>>')
                if password == user.password: #user['password'] == password:
                    CURRENT_USER = user
                else:
                    print('usuario o contraseña incorrecta...')

            
    
    while sel != 'exit':
        print(f'Logged in as {CURRENT_USER}')
        sel = input('1. Characters\n2. Games\n3. Adventures\n (exit to log out)\n>>>')
        
        if sel == '1':
            print(f'Your characters')
            result = show_characters(CURRENT_USER.id)
            for r in result:
                print(r)
            input()

        elif sel == '2':
            print(f'Your Games')
            result = show_games(CURRENT_USER.id)
            for r in result:
                print(r)
            input()

        elif sel == '3':
            print(f'Your Adventures')
            result = show_adventures(CURRENT_USER.id)
            for r in result:
                print(r)
            input()

menu()

