# Arquivo capitulo_4/q64.py

# Para usar SQL:
from banco_dados_sql import Conexao

# Para usar NoSQL: from banco_dados_nosql import Conexao

# Usanso SQL

def main():
    conexao = Conexao()
    print(conexao.conectar())

if __name__ == "__main__":
    main()
