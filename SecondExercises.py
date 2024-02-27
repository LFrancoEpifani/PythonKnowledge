# Exercise 1 - Create using different lists with names, places and problems to create a rondom story. Use the random.choice() function to select one item from each list.

import random

lista_nombres = ['Lucas', 'Emiliano', 'Sara', 'Alexa', 'Luciano', 'Susana']
lista_lugares = ['Castillo', 'Palacio', 'Cuadrilátero', 'Espacio', 'Volcán']
lista_problemas = ['Neo', 'UmpaLumpa', 'Rex', 'Topuria', 'Ezreal', 'Cosmo']

# Función con selección aleatoria dentro
def random_selection(nombres, lugares, problemas):
    lugar_random = random.choice(lugares)
    nombre_random = random.choice(nombres)
    problema_random = random.choice(problemas)
    print(f'Una vez {nombre_random}, se encontró en un {lugar_random} y tuvo que pelear contra {problema_random}.')

# Llamada a la función pasando las listas como argumentos
random_selection(lista_nombres, lista_lugares, lista_problemas)



# Exercise 2 - Implements a phonebook using a dictionary where the keys are the names of the contacts and the values are their phone numbers. Adds functions to insert a new contact, delete a contact, search for a contact's number and update an existing contact's number.



contacts = {'Lucas': 123, 'Lucia': 546, 'Tomas': 789, 'Lautaro': 124, 'Ezequiel': 573, 'Daniel': 989}

def insert_contact(contacts, clave, valor):
    contacts[clave] = valor

insert_contact(contacts, 'Jorge', 882)
print(contacts)

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
    else:
        print(f"{name} no encontrado.")

delete_contact(contacts, 'Pepe')
print(contacts)

def update_contact(contacts, name, num):
    if name in contacts:
        contacts[name] = num
        print(f"Contacto actualizado: {name} -> {num}")
    else:
        print(f"{name} no encontrado.")

update_contact(contacts, 'Tomas', 111)
update_contact(contacts, 'Daniel', 990)

print(contacts)


# Exercise 3 - Create a game where the user has to guess the random number that the program will generate. The user has a limited number of tries and the program has to give some help if the number is higher or lower.

print("Welcome to guess number!")
print("You have 5 tries to guess the number!")


random_number = random.radint(0, 100)
counter = 0

while counter <= 4:
    user_number = int(input("Write a number: "))
    counter += 1;
else:
    print('Adiós')