import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation(corr):
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.show()
