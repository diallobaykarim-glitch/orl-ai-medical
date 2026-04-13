import streamlit as st
import pandas as pd
import joblib

# 🧠 charger modèle (SHELL 2)
model = joblib.load("models/orl_rf_model.pkl")

st.title("🏥 Dashboard ORL IA Médicale")

# 📦 charger data (SHELL 1)
df = pd.read_csv("data/patients_1111.csv")

st.subheader("📊 Aperçu des patients")
st.dataframe(df.head(20))

st.subheader("🔮 Test IA ORL")

age = st.number_input("Age", 0, 100, 50)
cancer = st.selectbox("Cancer", [0, 1])
larynx = st.selectbox("Larynx", [0, 1])
parotide = st.selectbox("Parotide", [0, 1])
ethmoide = st.selectbox("Ethmoide", [0, 1])

if st.button("Prédire"):
    data = pd.DataFrame([{
        "age": age,
        "cancer": cancer,
        "larynx": larynx,
        "parotide": parotide,
        "ethmoide": ethmoide
    }])

    prediction = model.predict(data)[0]

    if prediction == "Malin":
        st.error("🚨 CAS MALIN")
    elif prediction == "Suspect":
        st.warning("⚠️ CAS SUSPECT")
    else:
        st.success("✅ CAS BÉNIN")