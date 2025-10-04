from faker import Faker
import random

def crear_usuarios(num=15):
    fake = Faker()
    usuarios={}

    for i in range(1,num+1):
        usuarios[i]={
            "nome": fake.name(),
            "direccion": fake.address(),
            "correo": fake.email(),
            "telefono": fake.phone_number()
        }

    return usuarios

def mostrar_usuarios(usuarios):
    print("Usuarios:\n")
    for clave, valor in usuarios.items():
        print(f"Usuario {clave}:")
        print(f"Nome: {valor['nome']}")
        print(f"Dirección: {valor['direccion']}")
        print(f"Correo: {valor['correo']}")
        print(f"Teléfono: {valor['telefono']}")
        print("-" * 60)

def aleatorio(usuarios):
    usuario_seleccionado=random.choice(list(usuarios.keys()))
    nome=usuarios[usuario_seleccionado]["nome"]
    print(f"O usuario chamado {nome} foi o afortunado!")



usuarios = crear_usuarios(15)
mostrar_usuarios(usuarios)
aleatorio(usuarios)