def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero.")
    return peso / (altura ** 2)
