import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = pd.read_csv('PBEA7347/data/b3_data_14012021.csv',
                     float_precision='high', sep=";")
    fig, axs = plt.subplots(2, 5, sharey=True)
    for i, col in enumerate(df.columns[3:]):
        data = df.loc[:, col]
        axs[int(i >= 5)][i % 5].hist(data, edgecolor='black', alpha=0.7)
        axs[int(i >= 5)][i % 5].set_title(col, fontsize=15)
    plt.show()
