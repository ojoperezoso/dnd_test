import uuid
import hashlib
#user1: ojo
#password: password

#user2:jonarap03
#password: password

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
CRIATURAS = []
PERSONAJES = []
ITEMS = []
VESTIMENTAS = []
ARMAS = []



#Relations
R_USUARIO_PERSONAJE = []
R_USUARIO_JUEGO = []
R_PERSONAJE_AVENTURA = []
R_AVENTURA_JUEGO = []
R_PERSONAJE_RAZA = []
R_PERSONAJE_CLASE = []
R_PERSONAJE_ITEM = []



#Juego definition
class Juego():
    def __init__(self, nombre, duenio, *args, **kwargs):
        self.id = (len(JUEGOS) + 1)
        self.nombre = nombre
        self.duenio = duenio
    
    def create_table_sql(self):
        query = (
            'create table if not exist Juego(\n'
            'id int unsigned not null auto_increment,\n'
            'nombre varchar(30) not null,\n'
            'duenio_id int unsigned not null,\n'                  
            'primary key (id),\n'
            'foreign key (duenio_id) references Usuario(id)\n'
            ');'
        )
        
        print(query)
        return query

    def create_self_sql(self):
        query = f'insert into Juego(nombre, duenio)\nvalues ({self.nombre}, {self.duenio});'

        print(f'{query}\n')
        return query
    
    def __str__(self):
        return f'{self.nombre}, {self.duenio}'

    def save(self):
        self.create_table_sql()
        self.create_self_sql()
        JUEGOS.append(self)


#Aventura definition
class Aventura():
    def __init__(self, nombre, gm_id, diary_id, *args, **kwargs):
        self.id = (len(AVENTURAS) + 1)
        self.nombre = nombre
        self.gm_id = gm_id
        self.diary_id = diary_id

    def create_table_sql(self):
        query = (
            'create table if not exist Aventura(\n'
            'id int unsigned not null auto_increment,\n'
            'nombre varchar(30) not null,\n'
            'gm_id int unsigned not null,\n'
            'diary_id int unsigned not null,\n'
            'primary key (id),\n'
            'foreign key (gm_id) references Usuario(id)\n'
            ');'
        )
        
        print(f'{query}\n')
        return query

    def create_self_sql(self):
        query = f'insert into Aventura(nombre, gm_id, diary_id)\nvalues ({self.nombre}, {self.gm_id}, {self.diary_id});'
        

    def __str__(self):
        return f'{self.nombre}, {self.gm_id} - {self.diary_id}'

    def save(self):
        self.create_table_sql()
        self.create_self_sql()
        AVENTURAS.append(self)


#Usuario definition
class Usuario():
    def __init__(self, nombre, password, *args, **kwargs):#*args, **kwargs):
        self.id = (len(USUARIOS) + 1)
        self.nombre = nombre
        self.password = password #Have to hash it using sha1

    def create_table_sql(self):
        query = (
            'create table if not exist Usuarios(\n'
            'id int unsigned not null auto_increment,\n'
            'nombre varchar(30) not null,\n'
            'password varchar(30) not null,\n'
            'primary key (id)\n'
            ');'
        )

        print(f'{query}\n')
        return query

    def create_self_sql(self):
        query = (
            f'insert into Usuarios (nombre, password)\nvalues ({self.nombre},{self.password});'
        )

        print(f'{query}\n')
        return query

    def __str__(self):
        return f'{self.nombre}'

    def save(self):
        self.create_table_sql()
        self.create_self_sql()
        USUARIOS.append(self)


#Raza definition
class Raza():
    def __init__(self, nombre, puntos, *args, **kwargs):
        self.id = (len(RAZAS) + 1)
        self.nombre = nombre
        self.puntos = puntos

    def create_table_sql(self):
        query = (
            'create table if not exist Razas(\n'
            'id int unsigned not null auto_increment,\n'
            'nombre varchar(30) not null,\n'
            'puntos ALGUNA MANERA DE GUARDAR UN DICCIONARIO O UN JSON TAL VEZ SIMPLEMENTE UN STRING\nprimary key (id),\n'
            'primary key (id)\n'
            ');'
        )

        print(f'{query}\n')
        return query

    def create_self_sql(self):
        query = f'insert into Razas (nombre, puntos)\nvalues ({self.nombre}, {self.puntos});'

        print(f'{query}\n')
        return query

    def __str__(self):
        return f'{self.nombre}, {self.puntos}'

    def save(self):
        self.create_table_sql()
        self.create_self_sql()
        RAZAS.append(self)


#Clases definition
class Clases():
    def __init__(self, nombre, *args, **kwargs):
        self.id = (len(CLASES) + 1)
        self.nombre = nombre    

    def create_table_sql(self):
        query = (
            'create table if not exist Clases(\n'
            'id int unsigned not null auto_increment,\n'
            'nombre varchar(30) not null,\n'
            'primary key (id),\n'
            ');'
        )

        print(f'{query}\n')
        return query

    def create_self_sql(self):
        query = f'insert into Razas (nombre)\nvalues({self.nombre});'

        print(f'{query}\n')
        return query

    def __str__(self):
        return f'{self.nombre}'

    def save(self):
        self.create_table_sql()
        self.create_self_sql()
        CLASES.append(self)


class Criatura():
    def __init__(self, nombre, raza_id, clase_id, lvl, puntos, *args, **kwargs):
        self.id = (len(CRIATURAS) + 1)
        self.nombre = nombre
        self.raza_id = raza_id #fk
        self.clase_id = clase_id #fk
        self.lvl = lvl
        self.puntos = puntos

    def create_table_sql(self):
        query = (
            'create table if not exist Criaturas(\n'
            'id int unsigned not null auto_increment,\n'
            'nombre varchar(30),\n'
            'raza_id int unsigned,\n'
            'clase_id int unsigned,\n'
            'lvl smallint unsigned not null,\n'
            'puntos ALGUNA MANERA DE GUARDAR UN DICCIONARIO O UN JSON TAL VEZ SIMPLEMENTE UN STRING\nprimary key (id),\n'
            'primary key (id),\n'
            'foreign key (raza_id) references Razas(id),\n'
            'foreign key (clase_id) references Clases(id));\n'
        )

        print(f'{query}\n')
        return query

    def create_self_sql(self):
        query = (f'insert into Criaturas (nombre, raza_id, clase_id, lvl, puntos)\nvalues({self.nombre},{self.raza_id},{self.clase_id},{self.lvl},{self.puntos}')
        
        print(f'{query}\n')
        return query

    def __str__(self):
        raza_nombre = clase_nombre = ''
        for raza in RAZAS:
            if raza.id == self.raza_id:
                raza_nombre = raza.nombre
        for clase in CLASES:
            if clase.id == self.clase_id:
                clase_nombre = clase.nombre

        return f'id:*{self.id}* - {self.nombre}, {raza_nombre} - {clase_nombre} lvl: {self.lvl}\npuntos: {self.puntos}'
        

    def save(self):
        #Calculating Point Modifiers
        #Raza Point Modifiers
        self.create_table_sql()
        self.create_self_sql()
        race_puntos = RAZAS[self.raza_id - 1].puntos

        for key in race_puntos:
            self.puntos[key] += race_puntos[key]

        CRIATURAS.append(self)
        

class Personaje(Criatura):
    def __init__(self, usuario_id, nombre, raza_id, clase_id, lvl, puntos, *args, **kwargs):
        super().__init__(nombre, raza_id, clase_id, lvl, puntos)
        self.id = (len(PERSONAJES) + 1)
        self.usuario_id = usuario_id

    def create_table_sql(self):
        query = (
            'create table if not exist Personaje(\n'
            'id int unsigned not null auto_increment,\n'
            'usuario_id int unsigned not null,\n'
            'nombre varchar(30) not null,\n'
            'raza_id int unsigned not null,\n'
            'clase_id int unsigned not null,\n'
            'lvl smallint unsigned not null,\n'
            'puntos ALGUNA MANERA DE GUARDAR UN DICCIONARIO O UN JSON TAL VEZ SIMPLEMENTE UN STRING\nprimary key (id),\n'
            'primary key (id),\n'
            'foreign key (usuario_id) references Usuario(id),\n'
            'foreign key (raza_id) references Raza(id),\n'
            'foreign key (clase_id) references Clase(id));'
        )
                
        print(f'{query}\n')
        return query
    
    def create_self_sql(self):
        query = (f'insert into Personaje(usuario_id, nombre, raza_id, clase_id, lvl, puntos)\nvalues ({self.usuario_id}, {self.nombre}, {self.raza_id}, {self.clase_id}, {self.lvl}, {self.puntos});')
        
        print(f'{query}\n')
        return query

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
        self.create_table_sql()
        self.create_self_sql()
        race_puntos = RAZAS[self.raza_id - 1].puntos

        for key in race_puntos:
            self.puntos[key] += race_puntos[key]

        PERSONAJES.append(self)
        self.create_self_sql()


class Item():
    def __init__(self, nombre, descripcion, puntos, visible, valor, *args, **kwargs):
        self.id = (len(ITEMS) + 1)
        self.nombre = nombre
        self.descripcion = descripcion
        self.puntos = puntos
        self.visible = visible
        self.valor = valor

    def create_table_sql(self):
        query = (
            'create table if not exist Items(\n'
            'id int unsigned not null auto_increment,\n'
            'nombre varchar(30),\n'
            'descripcion text,\n'
            'puntos ALGUNA MANERA DE GUARDAR UN DICCIONARIO O UN JSON TAL VEZ SIMPLEMENTE UN STRING\nprimary key (id),\n'
            'visible tinyint not null default=1,\n'
            'valor smallint not null default=0,\n'
            'primary key (id)\n'
            ');'
        )

        print(f'{query}\n')
        return query

    def create_self_sql(self):
        query = f'insert into Items (nombre, tipo, descripcion, puntos, visible, valor\nvalues ({self.nombre}, {self.tipo}, {self.descripcion}, {self.puntos}, {self.visible}, {self.valor});'

        print(f'{query}\n')
        return query

    def __str__(self):
        return f'{self.tipo} - {self.nombre}, ${self.valor}\nmodificador de puntos {self.puntos}'

    def save(self):
        self.create_table_sql()
        self.create_self_sql()
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

    def create_table_sql(self):
        query = (
            'create table if not exist Vestimentas(\n'
            'id int unsigned not null auto_increment,\n'
            'nombre varchar(30),\n'
            'descripcion text,\n'
            'puntos ALGUNA MANERA DE GUARDAR UN DICCIONARIO O UN JSON TAL VEZ SIMPLEMENTE UN STRING\nprimary key (id),\n'
            'visible tinyint not null default=1,\n'
            'valor smallint not null default=0,\n'
            'posicion tinyint unsigned not null,\n'
            'tipo tinyint unsigned not null,\n'
            'armadura smallint unsigned not null,\n'
            'primary key (id)\n'
            ');'
        )

        print(f'{query}\n')
        return query

    def create_self_sql(self):
        query = f'insert into Vestimentas (nombre,descripcion,puntos,visible,valor,posicion,tipo,armadura)\nvalues ({self.nombre}, {self.descripcion}, {self.puntos}, {self.visible}, {self.valor}, {self.posicion}, {self.valor}, {self.tipo}, {self.armadura});'

        print(f'{query}\n')
        return query

    def __str__(self):
        return f'{self.nombre} - {self.TIPOS_ARMADURA[self.tipo]}, {self.POSICIONES[self.posicion]} - ${self.valor}\narmadura: {self.armadura}\nmodificador de puntos: {self.puntos}'

    def save(self):
        self.create_table_sql()
        self.create_self_sql()
        VESTIMENTAS.append(self)

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
        self.tipo_ataque = tipo_ataque #1.cuerpo a cuerpo 2.a distancia
        self.tipo_arma = tipo_arma #1.espada 2.hacha 3.baston 4.arco 5.varita
        self.daño = daño

    def create_table_sql(self):
        query = (
            'create table if not exist Armas(\n'
            'id int unsigned not null auto_increment,\n'
            'nombre varchar(30),\n'
            'descripcion text,\n'
            'puntos ALGUNA MANERA DE GUARDAR UN DICCIONARIO O UN JSON TAL VEZ SIMPLEMENTE UN STRING\nprimary key (id),\n'
            'visible tinyint not null default=1,\n'
            'valor smallint not null default=0,\n'
            'posicion tinyint unsigned not null,\n'
            'tipo_ataque tinyint unsigned not null default=1,\n'
            'tipo_arma tinyint unsigned not null default=1\n'
            'daño smallint unsigned not null,\n'
            'primary key (id)\n'
            ');'
        )

        print(f'{query}\n')
        return query

    def create_self_sql(self):
        query = f'insert into Armas (nombre,descripcion,puntos,visible,valor,posicion,tipo_ataque,tipo_arma,daño)\nvalues ({self.nombre}, {self.descripcion}, {self.puntos}, {self.visible}, {self.valor}, {self.posicion}, {self.valor}, {self.tipo_ataque}, {self.tipo_arma}, {self.daño});'

        print(f'{query}\n')
        return query

    def __str__(self):
        return f'{self.nombre} {self.TIPOS_ATAQUE[self.tipo_ataque]} - {self.TIPOS_ARMA[self.tipo_arma]}, {self.POSICIONES[self.posicion]} ${self.valor}\ndaño: {self.daño}\nmodificador de puntos: {self.puntos}'    

    def save(self):
        self.create_table_sql()
        self.create_self_sql()
        ARMAS.append(self)

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
        

class aventura_juego():
    def __init__(self, aventura_id, juego_id, *args, **kwargs):
        self.aventura_id = aventura_id
        self.juego_id = juego_id

    def __str__(self):
        return f'{self.aventura_id}, {self.juego_id}'

    def save(self):
        R_AVENTURA_JUEGO.append(self)


class personaje_aventura():
    def __init__(self, personaje_id, aventura_id, *args, **kwargs):
        self.personaje_id = personaje_id
        self.aventura_id = aventura_id

    def __str__(self):
        return f'{self.personaje_id}, {self.aventura_id}'

    def save(self):
        R_PERSONAJE_AVENTURA.append(self)
        

class usuario_personaje():
    def __init__(self, usuario_id, personaje_id):
        self.usuario_id = usuario_id
        self.personaje_id = personaje_id

    def __str__(self):
        return f'{self.usuario_id}, {self.personaje_id}'

    def save(self):
        R_USUARIO_PERSONAJE.append(self)


class personaje_item():
    def __init__(self, personaje_id, item_id, *args, **kwargs):
        self.personaje_id = personaje_id
        self.item_id = item_id
        #self.date = now() to keep a log of the history of the item... might be interesting for multiplayer like ears from diablo

    def __str__(self):
        return f'{self.personaje_id} - {self.item_id}'

    def save(self):
        R_PERSONAJE_ITEM.append(self)





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




criatura = Criatura('Bulrog',1,0,22,{'fuerza': 15,'destreza': 14,'constitucion': 18,'inteligencia': 12,'sabiduria': 15,'carisma': 2})#nombre, raza_id, clase_id, lvl, puntos, *args, **kwargs):
personaje = Personaje(1,'Garlic',1,1,7,{'fuerza': 10,'destreza': 14,'constitucion': 9,'inteligencia': 11,'sabiduria': 8,'carisma': 14})#user_id, nombre, raza_id, clase_id, lvl, puntos, *args, **kwargs):
criatura.save()
personaje.save()