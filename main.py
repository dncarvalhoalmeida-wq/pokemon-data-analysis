import grafico
import banco
import pandas 

conexao = banco.conectar()

try:
    if conexao.is_connected():
        
        df = pandas.read_sql("SELECT peso,base_de_exp FROM pokemon",conexao)

        grafico.grafico_xp(df)

except Exception as erro:
    print(f"Houve um erro: {erro}")
    
finally:
    conexao.close()