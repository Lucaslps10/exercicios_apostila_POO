# Arquivo capitulo_5/q66.py
from imc.calculo import calcular_imc

def mostrar_imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")

mostrar_imc()



    


