import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

df=pd.read_excel("AdventureWorks.xlsx")

print(df.head)

#verificando tipos dados 
print(df.dtypes)

#receita total
print(round (df["Valor Venda"].sum(),2))

#criando coluna custo e valor custo total 
df["Custo"]=df["Custo Unitário"]*df["Quantidade"]
print(df["Custo"].sum())

#descobrir lucro 
df["Lucro"]=df["Valor Venda"]-df["Custo"]
print(round (df["Lucro"].sum(),2))

#tempo envio 
df["Tempo_envio"]=df["Data Envio"]-df["Data Venda"]
#extrair somente dias sem days
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
#print(df.head(1))
print(df["Tempo_envio"].dtype)

#media tempo envio por marca 
print(df.groupby("Marca")["Tempo_envio"].mean())

#verificar valores vazios
print(df.isnull().sum())

print(df.groupby([df["Data Venda"].dt.year,("Marca")])["Lucro"].sum())
print(df.groupby([df["Data Venda"].dt.year,("Marca")])["Lucro"].sum())

pd.options.display.float_format = '{:20,.2f}'.format

print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False))

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("ToTal")
plt.xlabel("Produto")
plt.show()

df.groupby(df["Data Venda"].dt.year) ["Lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.xlabel("Receita")
plt.show()

print(df.groupby(df["Data Venda"].dt.year) ["Lucro"].sum())
df_2009= df[df["Data Venda"].dt.year ==2009]
print(df_2009)

df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mes")
plt.xlabel("Lucro")
plt.show()

df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.xlabel("Lucro")
plt.xticks(rotation='horizontal')
plt.show()

df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.xlabel("Lucro")
plt.xticks(rotation='horizontal')
plt.show()

print(df["Tempo_envio"].describe())

plt.boxplot(df["Tempo_envio"])
plt.show()

plt.hist(df["Tempo_envio"])
plt.show()

print(df["Tempo_envio"].min())
print(df["Tempo_envio"].max())
