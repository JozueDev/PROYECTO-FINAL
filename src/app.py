from pickle import load
import streamlit as st

model = load(open("../data/raw/model_LGBMClassifier_Heart_Atack.sav", "rb"))
class_dict = {
    "0": "No Atack",
    "1": "Atack",
    }

st.title("Heart Atack - Model prediction")

val1 = st.slider("Edad", min_value = 20, max_value = 100, step = 1)
val2 = st.slider("Genero", min_value = 0, max_value = 1, step = 1)
val3 = st.slider("Region", min_value = 0, max_value = 1, step = 1)
val4 = st.slider("Nivel de Ingresos", min_value = 0, max_value = 2, step = 1)
val5 = st.slider("Hipertension", min_value = 0, max_value = 1, step = 1)
val6 = st.slider("Diabetes", min_value = 0, max_value = 1, step = 1)
val7 = st.slider("Nivel de Colesterol", min_value = 50, max_value = 300, step = 10)
val8 = st.slider("Obesidad", min_value = 0, max_value = 1, step = 1)
val9 = st.slider("Circunferencia Abdominal", min_value = 50, max_value = 300, step = 5)
val10 = st.slider("Historia Familiar", min_value = 0, max_value = 1, step = 1)
val11= st.slider("Consumo de tabaco", min_value = 0, max_value = 2, step = 1)
val12= st.slider("Consumo de alcohol", min_value = -1, max_value = 1, step = 1)
val13= st.slider("Actividad Fisica", min_value = 0, max_value = 2, step = 1)
val14= st.slider("Habitos alimentarios", min_value = 0, max_value = 1, step = 1)
val15= st.slider("Exposicion_polusion_aire", min_value = 0, max_value = 2, step = 1)
val16= st.slider("Nivel de estres", min_value = 0, max_value = 1, step = 1)
val17= st.slider("Horas de sueño", min_value = 4, max_value = 12, step = 1)
val18= st.slider("Presión arterial sistólica", min_value = 120, max_value = 180, step = 10)
val19= st.slider("Presión arterial diastólica", min_value = 60, max_value = 100, step = 10)
val20= st.slider("Glucosa en sangre", min_value = 50, max_value = 180, step = 1)
val21= st.slider("Colesterol_hdl", min_value = 30, max_value = 90, step = 1)
val22= st.slider("Colesterol_ldl", min_value = 60, max_value = 180, step = 1)
val23= st.slider("Triglyceridos", min_value = 100, max_value = 300, step = 1)
val24= st.slider("Resultados_ EKG", min_value = 0, max_value = 1, step = 1)
val25= st.slider("enfermedad cardíaca previa", min_value = 0, max_value = 1, step = 1)
val26= st.slider("Medicacion usada", min_value = 0, max_value = 1, step = 1)
val27= st.slider("Participo_campaña_deteccion", min_value = 0, max_value = 1, step = 1)

if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4,val5, val6, val7, val8,val9, val10, val11, val12,val13, val14, val15, val16,val17, val18, val19, val20,val21, val22, val23, val24,val25, val26, val27]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)

    