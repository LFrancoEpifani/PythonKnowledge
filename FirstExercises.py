#Exercise 1 - Create variables to store your name, age, height in meters and if you have pets (boolean). Then, print these variables.


nombre = 'Luciano'
edad = 24
altura = 1.86
mascota = True

print(f"My name is {nombre}. I am {edad} years old. My height is {altura} meters. Pets: {mascota}")

print("My name is {}. I am {} years old. My height is {} meters. Pets: {}".format(nombre, edad, altura, mascota))

#Exercise 2 - Calculate the area of a circle whose radius is 5. Use the formula area = π * radius^2. (You can use 3.1416 as an approximation of π).Given two numbers, try all the comparison operators (==, !=, <, >, <=, >=) and print the results.


import math 

def area(radio):
	return math.pi * radio**2


radius_circle = 5

form_area = area(radius_circle)

print("El área del círculo con radio {} es {}".format(radius_circle, form_area))

# Define dos números
numero1 = 10
numero2 = 20

# Realiza comparaciones e imprime los resultados
print(f"{numero1} == {numero2}: {numero1 == numero2}")
print(f"{numero1} != {numero2}: {numero1 != numero2}")
print(f"{numero1} < {numero2}: {numero1 < numero2}")
print(f"{numero1} > {numero2}: {numero1 > numero2}")
print(f"{numero1} <= {numero2}: {numero1 <= numero2}")
print(f"{numero1} >= {numero2}: {numero1 >= numero2}")


#Exercise 3 - Write a program that ask a user a number and print if the number it's positive, negative or cero. Use bucle for to iterate on a list of numbers and print only even numbers. Create while that starts in x=0 and increase 1 each iteration. Condition has to be <= 5


user_number = int(input('Write a number: '))

if user_number > 0:
	print ("Número Positivo.")
elif user_number < 0:
	print ("Número Negativo.")	
else:
	print("El número es 0");



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)


contador = 0;

while contador <= 5:
	print(f'Contador: {contador}')
	contador +=1

else:
	print('Contador terminado.')



# Exercise 4 - Write a program that convert Fahrenheit temperature to Celsius.

fahrenheit = float(input('Enter temperature in Fahrenheit: '))
celsius = (fahrenheit - 32) * 5.0/9.0

print (f"The temperature in Celsius is: {celsius}")