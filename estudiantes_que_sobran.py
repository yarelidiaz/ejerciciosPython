estudiantes_totales = 85
capacidad_autobus = 12


estudiantes_sobrantes = estudiantes_totales % capacidad_autobus


print("Número total de estudiantes:", estudiantes_totales)
print("Capacidad de cada autobús:", capacidad_autobus)
print("Estudiantes que no alcanzan lugar en los autobuses completos:", estudiantes_sobrantes)

if estudiantes_sobrantes > 0:
    print("Se necesita un autobús adicional para los estudiantes que sobran.")
else:
    print(" No se necesita un autobús adicional. Todos los estudiantes tienen lugar.")