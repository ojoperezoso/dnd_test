import uuid
import hashlib
import classes

#Juego definition
class Juego():

    def __init__(self, nombre, duenio, *args, **kwargs):
        self.id = (len(JUEGOS) + 1)
        self.nombre = nombre
        self.duenio = duenio

    def __str__(self):
        return f'{self.nombre}, {self.duenio}'

    def save(self):
        JUEGOS.append(self)
        """
        JUEGOS.append({
                      'id': self.id,
                      'nombre': self.nombre,
                      'duenio': self.duenio,
        })
        """

#Aventura definition
class Aventura():
    def __init__(self, nombre, gm, diary, *args, **kwargs):
        self.id = (len(AVENTURAS) + 1)
        self.nombre = nombre
        self.gm = gm
        self.diary = diary

    def __str__(self):
        return f'{self.nombre}, {self.gm} - {self.diary}'

    def save(self):
        AVENTURAS.append(self)
        """
        AVENTURAS.append({
                          'id': self.id,
                          'nombre': self.nombre,
                          'gm': self.gm,
                          'diary': self.diary
        })
        """

#Usuario definition
class Usuario():
    def __init__(self, nombre, password, *args, **kwargs):#*args, **kwargs):
        self.id = (len(USUARIOS) + 1)
        self.nombre = nombre
        self.password = password #Have to hash it using sha1

    def __str__(self):
        return f'{self.nombre}'

    def save(self):
        USUARIOS.append(self)
        """
        USUARIOS.append({
                      'id': self.id,
                      'nombre': self.nombre,
                      'password': self.password,
        })
        """

#Raza definition
class Raza():
    def __init__(self, nombre, puntos, *args, **kwargs):
        self.id = (len(RAZAS) + 1)
        self.nombre = nombre
        self.puntos = puntos


    def __str__(self):
        return f'{self.nombre}, {self.puntos}'

    def save(self):
        RAZAS.append(self)
        """
        RAZAS.append({
                      'id': self.id,
                      'nombre': self.nombre,
                      'puntos': self.puntos,
        })
        """

#Clases definition
class Clases():
    def __init__(self, nombre, *args, **kwargs):
        self.id = (len(CLASES) + 1)
        self.nombre = nombre    
        self

    def __str__(self):
        return f'{self.nombre}'

    def save(self):
        CLASES.append(self)
        """
        CLASES.append({
                        'id': self.id,
                        'nombre': self.nombre,
        })
        """



#Personaje definition
class Personaje():
    def __init__(self, usuario_id, nombre, raza_id, clase_id, lvl, puntos, *args, **kwargs):
        self.id = (len(PERSONAJES) + 1)
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.raza_id = raza_id #fk
        self.clase_id = clase_id #fk
        self.lvl = lvl
        self.puntos = puntos

    def __str__(self):
        raza_nombre = clase_nombre = usuario_nombre = ''
        for raza in RAZAS:
            if raza.id == self.raza_id:
                raza_nombre = raza.nombre
        for clase in CLASES:
            if clase.id == self.clase_id:
                clase_nombre = clase.nombre
        for usuario in USUARIOS:
            if usuario.id == self.usuario_id:
                usuario_nombre = usuario.nombre
        
        return f'Personaje: {self.nombre}, {raza_nombre} {clase_nombre} level: {self.lvl} puntos: {self.puntos}Usuario: {usuario_nombre}'

    def save(self):
        #Calculating Point Modifiers
        #Raza Point Modifiers
        race_puntos = RAZAS[self.raza_id - 1].puntos

        for key in race_puntos:
            self.puntos[key] += race_puntos[key]

        PERSONAJES.append(self)
        """
        PERSONAJES.append({
                           'id': self.id,
                           'usuario_id': self.usuario_id,
                           'nombre': self.nombre,
                           'raza_id': self.raza_id,
                           'clase_id': self.clase_id,
                           'lvl': self.lvl,
                           'puntos': self.puntos,
        })
        """


class Item():
    def __init__(self, nombre, descripcion, puntos, visible, valor, *args, **kwargs):
        self.id = (len(ITEMS) + 1)
        self.nombre = nombre
        self.tipo = 'otro'
        self.descripcion = descripcion
        self.puntos = puntos
        self.visible = visible
        self.valor = valor

    def __str__(self):
        return f'{self.tipo} - {self.nombre}, ${self.valor}\nmodificador de puntos {self.puntos}'

    def save(self):
        ITEMS.append(self)


class Vestimenta(Item):
    def __init__(self, posicion, tipo_armadura, armadura, nombre, descripcion, puntos, visible, valor, *args, **kwargs):
        super().__init__(nombre, descripcion, puntos, visible, valor, *args, **kwargs)
        self.POSICIONES = {
                           1: 'cabeza',
                           2: 'torzo',
                           3: 'brazos',
                           4: 'piernas',
                           5: 'manos',
                           6: 'pies',
                           7: 'otro',
        }
        self.TIPOS_ARMADURA = {
                               1: 'tela',
                               2: 'cuero',
                               3: 'malla',
                               4: 'placa',
                               5: 'otro',
        }
        self.posicion = posicion #1.Cabeza 2.Torso 3.Brazos 4.Piernas 5.Manos 6.Pies 7.Otro
        self.tipo = tipo_armadura #1.Vestimenta 2.Cuero 3.Malla 4.Placa 5.Otro
        self.armadura = armadura # + Puntos de armadura

    def __str__(self):
        return f'{self.nombre} - {self.TIPOS_ARMADURA[self.tipo]}, {self.POSICIONES[self.posicion]} - ${self.valor}\narmadura: {self.armadura}\nmodificador de puntos: {self.puntos}'



class Arma(Item):
    def __init__(self, posicion, tipo_ataque, tipo_arma, daño, nombre, descripcion, puntos, visible, valor, *args, **kwargs):
        super().__init__(nombre, descripcion, puntos, visible, valor, *args, **kwargs)
        self.POSICIONES = {
                          1: 'una mano',
                          2: 'dos manos',
        }
        self.TIPOS_ATAQUE = {
                           1: 'cuerpo a cuerpo',
                           2: 'distancia',
        }
        self.TIPOS_ARMA = {
                           1: 'espada',
                           2: 'hacha',
                           3: 'baston',
                           4: 'arco',
                           5: 'varita',
        }
        self.posicion = posicion #1.una mano 2.dos manos
        self.tipo_ataque = tipo_arma #1.cuerpo a cuerpo 2.a distancia
        self.tipo_arma = tipo_arma #1.espada 2.hacha 3.baston 4.arco 5.varita
        self.daño = daño

    def __str__(self):
        return f'{self.nombre} {self.TIPOS_ATAQUE[self.tipo_ataque]} - {self.TIPOS_ARMA[self.tipo_arma]}, {self.POSICIONES[self.posicion]} ${self.valor}\ndaño: {self.daño}\nmodificador de puntos: {self.puntos}'

    

"""

RELATION CREATION
RELATIONS FOR THE MySQL DATABASE

"""

class usuario_juego():
    def __init__(self, juego_id, usuario_id, usuario_rol, *args, **kwargs):
        super(usuario_juego, self).__init__(*args, **kwargs)
        self.juego_id = juego_id
        self.usuario_id = usuario_id
        self.usuario_rol = usuario_rol

    def __str__(self):
        return f'{self.juego_id}, {self.usuario_id} - {self.usuario_rol}'

    def save(self):
        R_USUARIO_JUEGO.append(self)
        """
        R_USUARIO_JUEGO.append({
                            'juego_id': self.juego_id,
                            'usuario_id': self.usuario_id,
                            'usuario_rol': self.usuario_rol,
        })
        """



class aventura_juego():
    def __init__(self, aventura_id, juego_id, *args, **kwargs):
        self.aventura_id = aventura_id
        self.juego_id = juego_id

    def __str__(self):
        return f'{self.aventura_id}, {self.juego_id}'

    def save(self):
        R_AVENTURA_JUEGO.append(self)
        """
        R_AVENTURA_JUEGO.append({
                                 'aventura_id': self.aventura_id,
                                 'juego_id': self.juego_id,
        })
        """



class personaje_aventura():
    def __init__(self, personaje_id, aventura_id, *args, **kwargs):
        self.personaje_id = personaje_id
        self.aventura_id = aventura_id

    def __str__(self):
        return f'{self.personaje_id}, {self.aventura_id}'

    def save(self):
        R_PERSONAJE_AVENTURA.append(self)
        """
        R_PERSONAJE_AVENTURA.append({
                                      'personaje_id': self.personaje_id,
                                      'aventura_id': self.aventura_id,
        })
        """



class usuario_personaje():
    def __init__(self, usuario_id, personaje_id):
        self.usuario_id = usuario_id
        self.personaje_id = personaje_id

    def __str__(self):
        return f'{self.usuario_id}, {self.personaje_id}'

    def save(self):
        R_USUARIO_PERSONAJE.append(self)
        """
        R_USUARIO_PERSONAJE.append({
                                 'usuario_id': self.usuario_id,
                                 'personaje_id': self.personaje_id,
        })
        """



class personaje_item():
    def __init__(self, personaje_id, item_id, *args, **kwargs):
        self.personaje_id = personaje_id
        self.item_id = item_id
        #self.date = now() to keep a log of the history of the item... might be interesting for multiplayer like ears from diablo

    def __str__(self):
        return f'{self.personaje_id} - {self.item_id}'

    def save(self):
        R_PERSONAJE_ITEM.append(self)

"""
DATABASE

TABLE DECLARATION
TABLES FOR THE MySQL DB

"""
#Tables
JUEGOS = []
AVENTURAS = []
USUARIOS = []
CLASES = []
RAZAS = []
PERSONAJES = []
ITEMS = []



#Relations
R_USUARIO_PERSONAJE = []
R_USUARIO_JUEGO = []
R_PERSONAJE_AVENTURA = []
R_AVENTURA_JUEGO = []
R_PERSONAJE_RAZA = []
R_PERSONAJE_CLASE = []
R_PERSONAJE_ITEM = []


#INPUT DATA
#Users
usuario = ''
usuario = Usuario('ojo','password')
usuario.save()
usuario = Usuario('jonarap03', 'password')
usuario.save()

#Races
raza = Raza('enano', {'fuerza': 0,'destreza': 0,'constitucion': 2,'inteligencia': 0,'sabiduria': 1,'carisma': 0})
raza.save()

#Clases
clase = Clases('guerrero')
clase.save()

#Characters
personaje = Personaje(1,'Gralok',1,1,1,{'fuerza': 11,'destreza': 10,'constitucion': 13,'inteligencia': 9,'sabiduria': 12,'carisma': 4})
personaje.save()
personaje = Personaje(2,'Marihuen',1,1,1,{'fuerza': 13,'destreza': 12,'constitucion': 13,'inteligencia': 9,'sabiduria': 11,'carisma': 8})
personaje.save()

#Games
juego = Juego('First play', 2)
juego.save()
juego = Juego('Second juego', 1)
juego.save()

#Adventures
aventura = Aventura('Into the abiss',2,1,)
aventura.save()
aventura = Aventura('Out of the abiss',1,1)
aventura.save()

#Items
#Vestimentas
vestimenta = Vestimenta(1,2,1,'Gorro de Goblin', 'Gorro de goblin comun, con manchas de nagre seca', {'fuerza':0,'destreza':0,'constitucion':0,'inteligencia':0,'sabiduria':0,'carisma':0}, True, 100)
vestimenta.save()

vestimenta = Vestimenta(2,2,4,'Pechera de cazador', 'Pechera de cazador comun, curtida del uso', {'fuerza':0,'destreza':1,'constitucion':0,'inteligencia':0,'sabiduria':0,'carisma':0}, True, 250)
vestimenta.save()
#Armas
arma = Arma(1,1,1,5,'Daga abisal', 'Daga encontraad en los avismos de la oscuridad', {'fuerza':0,'destreza':1,'constitucion':0,'inteligencia':0,'sabiduria':0,'carisma':0}, True, 2000)
arma.save()

arma = Arma(2,1,1,12,'espada del rey helado','poco a poco su poder consumira tus miembros',{'fuerza':0,'destreza':0,'constitucion':-1,'inteligencia':0,'sabiduria':0,'carisma':0},True, 800)
arma.save()


#usuario_juego RELATION
u_j = usuario_juego(1,1,1)
u_j.save()
u_j = usuario_juego(1,2,0)

#usuario_personaje RELATION
u_p = usuario_personaje(1,1)
u_p.save()
u_p = usuario_personaje(2,2)
u_p.save()

#aventura_juego RELATION
a_j = aventura_juego(1,1)
a_j.save()
a_j = aventura_juego(2,1)
a_j.save()

#personaje_aventura RELATION
p_a = personaje_aventura(1,1)
p_a.save()
p_a = personaje_aventura(2,2)
p_a.save()

#personaje_item RELATION
#self, nombre, tipo, description, puntos, visible, valor, vestimenta_lugar, vestimenta_armadura
c_i = personaje_item(2,1)
c_i.save()

c_i = personaje_item(2,3)
c_i.save()

c_i = personaje_item(1,2)
c_i.save()

c_i = personaje_item(1,4)
c_i.save()


def show_characters(usuario_id):
    result = []
    for character in PERSONAJES:
        if character.usuario_id == usuario_id:
            result.append(character)
            for item in show_inventario(character.id):
                result.append(item)
    
    return result

def show_games(usuario_id):
    result = []
    for relation in R_USUARIO_JUEGO:
        if relation.usuario_id == usuario_id:
            for juego in JUEGOS:
                if juego.id == relation.juego_id:
                    result.append(juego)
                    
    return result

def show_adventures(usuario_id):
    result = []
    for game_relation in R_USUARIO_JUEGO:
        if game_relation.usuario_id == usuario_id:
            for adv_relation in R_AVENTURA_JUEGO:
                if adv_relation.juego_id == game_relation.juego_id:
                    for aventura in AVENTURAS:
                        if aventura.id == adv_relation.aventura_id:
                            result.append(aventura)

    return result

def show_inventario(personaje_id):
    result = []
    for personaje in PERSONAJES:
        if personaje.id == personaje_id:
            for relation in R_PERSONAJE_ITEM:
                if relation.personaje_id == personaje.id:
                    for item in ITEMS:
                        if item.id == relation.item_id:
                            result.append(item)

    return result


def menu():
    CURRENT_USER = {} #{id,nombre,}
    sel = ''
    print('login')
    user_login = input('usuario nombre\n>>>')

    while not CURRENT_USER:
        for usuario in USUARIOS:
            if user_login == usuario.nombre: #usuario['nombre'] == usuario:
                password = input('password\n>>>')
                if password == usuario.password: #usuario['password'] == password:
                    CURRENT_USER = usuario
                else:
                    print('usuario o contraseña incorrecta...')

            
    
    while sel != 'exit':
        print(f'Logged in as {CURRENT_USER}')
        sel = input('1. Characters\n2. Games\n3. Adventures\n (exit to log out)\n>>>')
        
        if sel == '1':
            print(f'Your characters')
            result = show_characters(CURRENT_USER.id)
            for r in result:
                print(f'{r}\n')
            
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

