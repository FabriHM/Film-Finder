from faker import Faker
import csv

fake = Faker()

Faker.seed(0)
with open("users.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    for _ in range(1500):
        dni = fake.unique.random_number(digits=8)
        nombre_completo = fake.name()
        fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%Y-%m-%d")
        telefono = fake.phone_number()
        email = fake.email()
        nombre_usuario = fake.user_name()
        contrasena = fake.password()

        writer.writerow([dni, nombre_completo, fecha_nacimiento, telefono, email, nombre_usuario, contrasena])
