
def process_line(data: list):
    print("linea:")
    data[-1] = data[-1].strip()
    alumno = f"{data[0]}, {data[1]}"
    presentes = data.count("P")
    ausentes = data.count("A")
    cantidad_clases = len(data)-2
    if (presentes + ausentes) != cantidad_clases:
        print("error")
    porcentaje = (presentes *100/cantidad_clases)    
    print(f"Alumno: {alumno}, asistencia: {porcentaje}")

with open("datos.csv", "r") as file:
    datos = file.readlines()

for linea in datos:
    process_line(linea.split(","))