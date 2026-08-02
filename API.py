import requests
import mysql.connector
import banco

conexao = banco.conectar()
resposta = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=400")

dicionario = resposta.json()

try:
    if conexao.is_connected():
        print("Conectou com sucesso!")
        cursor = conexao.cursor()
        
        for pokemon in dicionario["results"]:

            detalhes = requests.get(pokemon["url"]).json()

            cursor.execute("""INSERT INTO pokemon (id,nome,base_de_exp,habilidade,peso) VALUES 
                        (default,%s,%s,%s,%s)
                        """,
                        (
                            detalhes["forms"][0]["name"],
                            detalhes["base_experience"],
                            detalhes["abilities"][0]["ability"]["name"],
                            detalhes["weight"]
                        )
                        )
        conexao.commit()


except Exception as error:
    print(f"Houve um erro: {error}")

finally:
    conexao.close()
    cursor.close()