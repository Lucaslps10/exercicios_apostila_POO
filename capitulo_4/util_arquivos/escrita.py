def escrever_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)
