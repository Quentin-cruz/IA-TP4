import pandas as pd
import random

dataFrame1MonJeuDeDonneeDentrainement = pd.read_csv("donnesTestIa.csv")
dataFrame1MonJeuDeDonneeDentrainement["danger"] = dataFrame1MonJeuDeDonneeDentrainement["danger"].map({"safe": 0, "dangerous": 1})

w = random.randint(-10, 10)
b = random.randint(-10, 10)
print(w, b)

X = dataFrame1MonJeuDeDonneeDentrainement["vitesse"].tolist()
Y = dataFrame1MonJeuDeDonneeDentrainement["danger"].tolist()
print(X[:5], Y[:5])

""""def test(a, b):
    calcul = a * b
    return calcul"""

def Zpredict(x):
    Z = w * x + b
    if Z > 0:
        return 1
    else:
        return 0

for (x, y) in zip(X, Y):
    prediction = Zpredict(x)
    if prediction 
    print(f"Vitesse: {x}, Danger: {y}, Prediction: {prediction}")