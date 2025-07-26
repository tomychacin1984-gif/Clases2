alumnos = {
    "Juan": {"Matemáticas", "Historia", "Biología"},
    "maria": {"Matemáticas", "Física", "Química"},
    "Ruben": {"Historia", "Arte", "Biología"},
}

materias_unicas = set.union(*alumnos.values())
print("Materias únicas:",materias_unicas)

materias_comunes = alumnos["Juan"].intersection(alumnos["maria"])
print("Materias comunes entre Juan y maria:",materias_comunes)

alumnos["Ruben"].add("Física")

alumnos["Ruben"].discard("Arte")

for alumno, materias in alumnos.items():
    print(f"{alumno} cursa {len(materias)} materias.")