aparelho = input("Nome do aparelho: ")
potencia = float(input("Potência (W): "))
horas = float(input("Horas por dia: "))

consumo = (potencia * horas * 30) / 1000

print("Aparelho:", aparelho)
print("Consumo mensal:", consumo, "kWh")