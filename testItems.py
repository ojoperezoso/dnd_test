class Item():
    def __init__(self, nombre, descripcion, puntos, visible, valor, *args, **kwargs):
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

    def save(self):
        super().save(self)


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

    def save(self):
        super().save(self)


gorro = Vestimenta(1,2,1,'Gorro de Goblin', 'Gorro de goblin comun, con manchas de nagre seca', {'fuerza':0,'destreza':0,'constitucion':0,'inteligencia':0,'sabiduria':0,'carisma':0}, True, 100)

pechera = Vestimenta(2,2,4,'Pechera de cazador', 'Pechera de cazador comun, curtida del uso', {'fuerza':0,'destreza':1,'constitucion':0,'inteligencia':0,'sabiduria':0,'carisma':0}, True, 250)

daga = Arma(1,1,1,5,'Daga abisal', 'Daga encontraad en los avismos de la oscuridad', {'fuerza':0,'destreza':1,'constitucion':0,'inteligencia':0,'sabiduria':0,'carisma':0}, True, 2000)

espada = Arma(2,1,1,12,'espada del rey helado','poco a poco su poder consumira tus miembros',{'fuerza':0,'destreza':0,'constitucion':-1,'inteligencia':0,'sabiduria':0,'carisma':0},True,800)

print()
print(f'{gorro}\n')
print(f'{pechera}\n')
print(f'{espada}\n')
print(f'{daga}\n')