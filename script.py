import pandas as pd
import random

dataFrame1MonJeuDeDonneeDentrainement = pd.read_csv("donnesTestIa.csv")
dataFrame1MonJeuDeDonneeDentrainement["danger"] = dataFrame1MonJeuDeDonneeDentrainement["danger"].map({0: "safe", 1: "danger"})

w = random.randint(-10, 10)
b = random.randint(-10, 10)
print(w, b)

X = dataFrame1MonJeuDeDonneeDentrainement["vitesse"]
Y = dataFrame1MonJeuDeDonneeDentrainement["danger"]
print(X[:5], Y[:5])