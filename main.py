import pandas as pd
import math
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
def main():
    # Base de dados retirada de:
    # https://raw.githubusercontent.com/fivethirtyeight/data/master/bob-ross/elements-by-episode.csv

    dados = pd.read_csv("bobross.csv")
    # Removendo as colunas de episódio e título
    del dados['TITLE']
    del dados['EPISODE']

    print("(linhas, colunas): ", dados.shape)

    print ("dados antes de dropar as linhas com WINTER = 0: ", dados.shape)

    dados = dados.drop(dados.query('WINTER == 0').sample(frac=.7).index)

    print("dados depois de dropar as linhas com WINTER = 0: ", dados.shape)

    # lista de colunas para dropar (colunas de pouco uso)
    colunas_para_dropar =[]
    for col in dados.columns:
        if int(dados[col].sum()) <= 5:
            colunas_para_dropar.append(col)

    dados = dados.drop(axis=1, labels=colunas_para_dropar)

    # separando em matrizes de atributos e repostas
    matriz_x = dados.loc[:, dados.columns != "WINTER"]
    matriz_y = dados.loc[:, "WINTER"]

    # matriz_x = matriz_x.drop(axis=1,labels=["SNOW", "SNOWY_MOUNTAIN"])

    quant_index_treino = math.ceil(matriz_x.shape[0] * 0.75)

    quant_index_teste = matriz_x.shape[0] - quant_index_treino

    # matrizes que serão usadas para treino, os 75% primeiros indices
    treino_x = matriz_x[:quant_index_treino]
    treino_y = matriz_y[:quant_index_treino]

    # matrizes que serão usdas para teste, os 25% ultimos indices
    teste_x = matriz_x[quant_index_treino:]
    teste_y = matriz_y[quant_index_treino:]

    modelo = LinearSVC()

    modelo.fit(treino_x, treino_y)

    previsoes = modelo.predict(teste_x)

    print(accuracy_score(previsoes, teste_y))


if __name__ == "__main__":
    main()