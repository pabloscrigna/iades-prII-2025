from datetime import datetime

hora_actual = datetime.now()

# convertimos fecha y hora de formato datetime a str
now_str = datetime.strftime(hora_actual, "%d-%m-%Y %H:%M:%S")
print("hora actual: ", now_str)


now_str = datetime.strftime(hora_actual, "%H:%M:%S")
print("hora actual: ", now_str)


now_str = datetime.strftime(hora_actual, "%d/%m/%Y")
print("hora actual: ", now_str)

now_str = datetime.strftime(hora_actual, "%d/%m/%y")
print("hora actual: ", now_str)