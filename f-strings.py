# f strings da formato a las cadenas de texto
name= "Ana"
text = f"Hola {name}"
print(text)

mayusculas = f"HOLA {name.upper()}"
print(mayusculas)

#condicionales

edad = 15
mensaje = f"hola {name} Entrada: {"Permitida" if edad >= 18 else "Denegada"}"
print(mensaje)

num_participantes = 2
mensaje2 = f"total= {num_participantes} {"Participantes" if num_participantes > 1 else "Participante"}"
print(mensaje2)

print("--------------------------------------------------")

# Modificadores de formato avanzados en f-strings para números y fechas

bank_bakance = 13000000.384
text = f"Tu saldo es {bank_bakance:,.2f} USD" 
# El formato :,.2f formatea el número con comas como separadores de miles y dos decimales
print(text)
print("--------------------------------------------------")
user_id = 1
text2 = f"Tu id es {user_id:04d}"
# El formato :04d formatea el número entero con ceros a la izquierda para que tenga al menos 4 dígitos
print(text2)
print("--------------------------------------------------")
user_id = 158
text3 = f"Tu id es {user_id:04d}"
# El formato :04d formatea el número entero con ceros a la izquierda para que tenga al menos 4 dígitos
print(text3)
print("--------------------------------------------------")

from datetime import datetime
date = datetime(2016, 6, 11)
text4 = f"La fecha de su nacimiento es: {date:%d-%m-%Y}"
# El formato :%d-%m-%Y formatea la fecha en el formato día-mes-año  
print(text4)

