# datetime

from datetime import datetime, timezone, timedelta

# fecha y hora

# leemos la fecha y hora de la computadora donde ejecutamos el programa
# en formato datetime
now = datetime.now()

print("now : ", now)
print("tipo de dato now: ", type(now))

# leemos fecha y hora en utc en formato datetime
now_utc = datetime.now(timezone.utc)
print("now utc : ", now_utc)

# incrementamos un dia a un abjeto datetime
manana = now_utc + timedelta(days=1)
print("mañana: ", manana)

# incrementamos 60 minutos (1 hora) a un objeto del tipo datetime
ahora_1_hora_mas = now_utc + timedelta(minutes=60)            #(hours=1)
print("mas 1 hora: ", ahora_1_hora_mas)

print("fecha y hora: ", now)

# imprimimos las distintas componentes de la fecha y la hora por separdo
print("año: ", now.year)
print("mes: ", now.month)
print("dia: ", now.day)
print("hora: ", now.hour)
print("minutos: ", now.minute)

# leemos fecha y hora en formato datetime
now = datetime.now()
print("now: ", now)
print("tipo now: ", type(now))

# convertimos fecha y hora de formato datetime a str
now_str = datetime.strftime(now, "%d-%m-%Y %H:%M:%S")
print("now str: ", now_str)
print("tipo now str: ", type(now_str))

# convertimos fecha y hora en str a formato datetime
now_dt = datetime.strptime(now_str,"%d-%m-%Y %H:%M:%S")
print("now dt: ",now_dt)
print("tipo now dt: ", type(now_dt))



