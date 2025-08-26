dinero = 500
extra = 50
dinero_total = dinero + extra

pastel = 180
globos = 6 * 25
refrescos = 4 * 30
dulces = 3 * 40

costo_total = pastel + globos + refrescos + dulces

if dinero_total >= costo_total:
    print("si le alcanza.Le sobra:" , dinero_total - costo_total, "pesos")
else:
    print("no le alacanza.Le falta:" , costo_total - dinero_total, "pesos")
