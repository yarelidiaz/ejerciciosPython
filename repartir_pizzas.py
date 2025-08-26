pizzas_grandes = 3
porciones_por_pizza = 8
numero_de_amigos = 18

total_porciones = pizzas_grandes * porciones_por_pizza

porciones_por_amigo = total_porciones / numero_de_amigos

print("Marco preparó", pizzas_grandes, "pizzas grandes.")
print("Cada pizza tiene", porciones_por_pizza, "porciones.")
print("Tiene", numero_de_amigos, "amigos.")
print("Cada amigo recibirá", (porciones_por_amigo, 2), "porciones de pizza.")
