from classes import *

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

