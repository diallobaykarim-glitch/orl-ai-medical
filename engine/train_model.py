import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# 1. Charger dataset
df = pd.read_csv("data/patients_1111.csv")

# 2. Features / target
X = df[["age", "cancer", "larynx", "parotide", "ethmoide"]]
y = df["classe"]

# 3. Modèle IA
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=6,
    random_state=42
)

# 4. Entraînement
model.fit(X, y)

# 5. Sauvegarde modèle
joblib.dump(model, "models/orl_rf_model.pkl")

print("✅ MODÈLE ORL ENTRAÎNÉ ET SAUVEGARDÉ")