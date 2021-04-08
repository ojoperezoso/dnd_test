import uuid
class Criatura():
    def __init__(self, nombre, raza_id, clase_id, lvl, puntos, *args, **kwargs):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.raza_id = raza_id #fk
        self.clase_id = clase_id #fk
        self.lvl = lvl
        self.puntos = puntos

    def __str__(self):
        """
        raza_nombre = clase_nombre = ''
        for raza in RAZAS:
            if raza.id == self.raza_id:
                raza_nombre = raza.nombre
        for clase in CLASES:
            if clase.id == self.clase_id:
                clase_nombre = clase.nombre

        return f'id:*{self.id}* - {self.nombre}, {self.raza_nombre} - {self.clase_nombre} lvl: {self.lvl}\npuntos: {self.puntos}'
        """
        return f'id:*{self.id}* - {self.nombre}, {self.raza_id} - {self.clase_id} lvl: {self.lvl}\npuntos: {self.puntos}'
class Personaje(Criatura):
    def __init__(self, usuario_id, nombre, raza_id, clase_id, lvl, puntos, *args, **kwargs):
        super().__init__(nombre, raza_id, clase_id, lvl, puntos)
        self.usuario_id = usuario_id

    def __str__(self):
        """
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
        """
        return f'id:*{self.id} * u_id*{self.usuario_id}*- {self.nombre}, {self.raza_id} - {self.clase_id} lvl: {self.lvl}\npuntos: {self.puntos}'
    """def save(self):
        #Calculating Point Modifiers
        #Raza Point Modifiers
        race_puntos = RAZAS[self.raza_id - 1].puntos

        for key in race_puntos:
            self.puntos[key] += race_puntos[key]

        PERSONAJES.append(self)
"""

criatura = Criatura('Bulrog',5,0,22,{'fuerza': 15,'destreza': 14,'constitucion': 18,'inteligencia': 12,'sabiduria': 15,'carisma': 2})#nombre, raza_id, clase_id, lvl, puntos, *args, **kwargs):
personaje = Personaje(1,'Garlic',1,1,7,{'fuerza': 10,'destreza': 14,'constitucion': 9,'inteligencia': 11,'sabiduria': 8,'carisma': 14})#user_id, nombre, raza_id, clase_id, lvl, puntos, *args, **kwargs):

input(f'{criatura}\n')
input(f'{personaje}\n')