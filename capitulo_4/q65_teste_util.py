# Arquivo capitulo_4/q65.py

from util_arquivos.escrita import escrever_arquivo
from util_arquivos.leitura import ler_arquivo

# Escreve no arquivo
escrever_arquivo('mensagem.txt', 'Olá, mundo!')

# Lê e imprime o conteúdo
conteudo = ler_arquivo('mensagem.txt')
print(conteudo)
