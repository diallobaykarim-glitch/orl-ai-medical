import pandas as pd
import joblib

# 🧠 SHELL 2 - charger modèle IA
model = joblib.load("models/orl_rf_model.pkl")

# 🧪 SHELL 1 - exemple patient (nouveau cas)
new_patient = pd.DataFrame([{
    "age": 55,
    "cancer": 1,
    "larynx": 1,
    "parotide": 0,
    "ethmoide": 1
}])

# 🔮 prédiction
prediction = model.predict(new_patient)

# 📊 affichage résultat
print("🧠 DIAGNOSTIC ORL :", prediction[0])

# ⚠️ vérification automatique simple
if prediction[0] == "Malin":
    print("🚨 ALERTE : cas potentiellement grave")
elif prediction[0] == "Suspect":
    print("⚠️ surveillance recommandée")
else:
    print("✅ cas bénin")