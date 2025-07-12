import os
config = [
    ('capitulo_1', 10),
    ('capitulo_2', 55),
    ('capitulo_3', 61),
    ('capitulo_4', 65),
    ('capitulo_5', 75),
    ('capitulo_6', 80),
    ('capitulo_7', 90)
]
numero_anterior = 0
for pasta, ultimo in config:
    os.makedirs(pasta, exist_ok=True)
    inicio = numero_anterior + 1
    fim = ultimo + 1
    for n in range(inicio, fim):
        caminho = os.path.join(pasta, f'q{n}.py')
        if not os.path.exists(caminho):
            with open(caminho, 'w') as arquivo:
                arquivo.write(f'# Arquivo {caminho}\n')
    numero_anterior = ultimo # Atualiza para próxima pasta
print("Estrutura criada com sucesso!")