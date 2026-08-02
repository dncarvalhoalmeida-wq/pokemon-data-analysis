import matplotlib.pyplot as plt

def grafico_xp(df):

    peso = df["peso"]
    exp = df["base_de_exp"]

    plt.figure(figsize=(10,10)) 
    plt.grid(True)
    plt.scatter(peso,exp,label = "Relação peso e experiência",color="orange",marker="o")
    plt.xlabel("Peso pokemon")
    plt.ylabel("Experiência pokemon")

    plt.title("Peso x Experiência")
    plt.savefig("graficopokemon.png",dpi=75)
