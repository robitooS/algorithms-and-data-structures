import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("1. __O Detetive de Viés___ Crie um dataset manual....xlsx", index_col=0)
# print(df)
fig, ax = plt.subplots()

pronomes_masculinos = [
    "ele", "eles",
    "o", "os",
    "dele", "deles",
    "nele", "neles",
    "meu", "meus",
    "teu", "teus",
    "seu", "seus",
    "nosso", "nossos",
    "este", "estes",
    "esse", "esses",
    "aquele", "aqueles",
    "algum", "alguns",
    "nenhum", "nenhuns",
    "todo", "todos",
    "outro", "outros",
    "muito", "muitos",
    "pouco", "poucos"
]

pronomes_femininos = [
    "ela", "elas",
    "a", "as",
    "dela", "delas",
    "nela", "nelas",
    "minha", "minhas",
    "tua", "tuas",
    "sua", "suas",
    "nossa", "nossas",
    "esta", "estas",
    "essa", "essas",
    "aquela", "aquelas",
    "alguma", "algumas",
    "nenhuma", "nenhumas",
    "toda", "todas",
    "outra", "outras",
    "muita", "muitas",
    "pouca", "poucas"
]

num_masc = 0
num_fem = 0

for frase in df["Frase"]:
    palavras = frase.lower().split(" ")
    
    for palavra in palavras:
        if palavra in pronomes_masculinos:
            num_masc += 1
        elif palavra in pronomes_femininos:
            print(palavra)
            num_fem += 1
    
print(f"Total de termos masculinos encontrados: {num_masc}")
print(f"Total de termos femininos encontrados: {num_fem}") 
print("-" * 30)

total = num_masc + num_fem
if total == 0:
    print("Nenhuma pronome encontrado")
else:
    percent_masculino = (num_masc / total) * 100
    print(f"Viés Masculino: {percent_masculino:.1f}%")
    
    if percent_masculino > 60:
        print("Alto viés masculino")
    elif percent_masculino < 40:
        print("Alto viés feminino")
    else:
        print("Teste equilibrado")    
        
x_axis = ["Masculino", "Feminino"]
counts = [num_masc, num_fem]

ax.bar(x_axis, counts)
ax.set_ylabel("Qtd. de pronomes")
ax.set_title("Quantidade de pronomes para cada categoria")
plt.show()