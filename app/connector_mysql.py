import mysql.connector

# Configurações da conexão
config = {
    'user': 'root',       # seu usuário do MySQL
    'password': 0000,     # sua senha do MySQL
    'host': 'localhost',         # endereço do servidor MySQL (localhost se for local)
    'database': 'bd_base_arq'  # nome do banco de dados que deseja acessar
}
try:
    # Criar a conexão
    conexao = mysql.connector.connect(**config)
    if conexao.is_connected():
        print("Conexão estabelecida com sucesso!")
except mysql.connector.Error as erro:
    print(f"Erro ao conectar: {erro}")
finally:
    if conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")
