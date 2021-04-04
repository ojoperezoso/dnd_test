
#Game definition
class Game():

    def __init__(self, name, owner, *args, **kwargs):
        self.id = (len(GAMES) + 1)
        self.name = name
        self.owner = owner

    def __str__(self):
        return f'{self.name}, {self.owner}'

    def save(self):
        GAMES.append({
                      'id': self.id,
                      'name': self.name,
                      'owner': self.owner,
        })

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
        ADVENTURES.append({
                          'id': self.id,
                          'name': self.name,
                          'gm': self.gm,
                          'diary': self.diary
        })

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
        USERS.append({
                      'id': self.id,
                      'name': self.name,
                      'password': self.password,
        })


#Race definition
class Race():
    def __init__(self, name, puntos, *args, **kwargs):
        self.id = (len(RACES) + 1)
        self.name = name
        self.puntos = puntos
        self

    def __str__(self):
        return f'{self.name}, {self.puntos}'

    def save(self):
        RACES.append({
                      'id': self.id,
                      'name': self.name,
                      'puntos': self.puntos,
        })


#Classes definition
class Classes():
    def __init__(self, name, *args, **kwargs):
        self.id = (len(CLASSES) + 1)
        self.name = name    
        self

    def __str__(self):
        return f'{self.name}'

    def save(self):
        CLASSES.append({
                        'id': self.id,
                        'name': self.name,
        })


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
        race_name = RACES.get('id', self.race_id)
        class_name = CLASSES.get('id', self.class_id)
        user_name = USERS.get('id', self.user_id)
        return f'Usuario: {user_name} Personaje: {self.name}, {race_name} {class_name} level: {self.lvl}'

    def save(self):
        #Calculating Point Modifiers
        #Race Point Modifiers
        race_puntos = RACES[self.race_id - 1]['puntos']

        for key in race_puntos:
            self.puntos[key] += race_puntos[key]

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
        R_USER_GAME.append({
                            'game_id': self.game_id,
                            'user_id': self.user_id,
                            'user_role': self.user_role,
        })




class adventure_game():
    def __init__(self, adventure_id, game_id, *args, **kwargs):
        self.adventure_id = adventure_id
        self.game_id = game_id

    def __str__(self):
        return f'{self.adventure_id}, {self.game_id}'

    def save(self):
        R_ADVENTURE_GAME.append({
                                 'adventure_id': self.adventure_id,
                                 'game_id': self.game_id,
        })




class character_adventure():
    def __init__(self, character_id, adventure_id, *args, **kwargs):
        self.character_id = character_id
        self.adventure_id = adventure_id

    def __str__(self):
        return f'{self.character_id}, {self.adventure_id}'

    def save(self):
        R_CHARACTER_ADVENTURE.append({
                                      'character_id': self.character_id,
                                      'adventure_id': self.adventure_id,
        })




class user_character():
    def __init__(self, user_id, character_id):
        self.user_id = user_id
        self.character_id = character_id

    def __str__(self):
        return f'{self.user_id}, {self.character_id}'

    def save(self):
        R_USER_CHARACTER.append({
                                 'user_id': self.user_id,
                                 'character_id': self.character_id,
        })