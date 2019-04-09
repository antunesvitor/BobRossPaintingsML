import pandas as pd

# uri = "https://raw.githubusercontent.com/fivethirtyeight/data/master/bob-ross/elements-by-episode.csv"

def main():
    dados = pd.read_csv("bobross.csv")

    print(dados.shape)

    count = 0
    for column in dados:
        count += 1

    print(count)

    # Removendo as colunas de episódio e título
    del dados['TITLE']
    del dados['EPISODE']
    count = 0
    for column in dados:
        count += 1
    print(count)

    print(dados.shape)
    print(dados.head())

if __name__ == "__main__":
    main()