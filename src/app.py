from pickle import load
import streamlit as st
import base64
from PIL import Image

# Configuración de página
st.set_page_config(
    page_title="CardioPredict",
    page_icon="❤️",
    layout="wide"
)

# Cargar el modelo
model = load(open("./models/model_LGBMClassifier_Heart_Atack.sav", "rb"))
class_dict = {
    "0": "Bajo Riesgo ❤️",
    "1": "Alto Riesgo ⚠️"
}

# Función para imagen de fondo
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: rgba(255, 255, 255, 0.9);
        background-blend-mode: lighten;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Establecer fondo (reemplaza 'heart_bg.png' con tu imagen)
# set_background('heart_bg.png')  # Descomenta si tienes una imagen local

# Estilos CSS personalizados
st.markdown("""
<style>
    :root {
        --primary: #e63946;
        --secondary: #457b9d;
        --light: #f1faee;
        --dark: #1d3557;
    }
    
    .header {
        color: white;
        background-color: var(--primary);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .section {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        border-left: 5px solid var(--secondary);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .prediction-box {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 2rem;
        border: 3px solid var(--primary);
    }
    
    .stButton>button {
        background-color: var(--primary);
        color: white !important;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 25px;
        border: none;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton>button:hover {
        background-color: var(--dark) !important;
        transform: scale(1.02);
    }
    
    .css-18e3th9 {
        padding: 2rem 5rem;
    }
    
    @media (max-width: 768px) {
        .css-18e3th9 {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Encabezado con logo
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://img.icons8.com/color/96/000000/heart-health.png", width=80)
with col2:
    st.markdown("<div class='header'><h1>CardioPredict</h1><p>Sistema de evaluación de riesgo cardiovascular</p></div>", unsafe_allow_html=True)

# Descripción
with st.container():
    st.markdown("""
    <div class="section">
    <h4 style="color: #1d3557;">🔍 ¿Qué es CardioPredict?</h4>
    <p>Esta herramienta utiliza inteligencia artificial para evaluar tu riesgo de desarrollar problemas cardiovasculares 
    basándose en múltiples factores de salud y estilo de vida. Completa tu información a continuación y obtén tu evaluación personalizada.</p>
    </div>
    """, unsafe_allow_html=True)

# Organización en columnas
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown("<div class='section'><h4>📊 Datos Personales</h4></div>", unsafe_allow_html=True)
        val1 = st.slider("**Edad**", min_value=20, max_value=100, step=1, value=40, help="Edad en años")
        val2 = st.selectbox("**Género**", ["Femenino", "Masculino"], format_func=lambda x: x, index=0)
        val2 = 0 if val2 == "Femenino" else 1
        val3 = st.selectbox("**Región**", ["Urbana", "Rural"], index=0)
        val3 = 0 if val3 == "Urbana" else 1
        val4 = st.selectbox("**Nivel de ingresos**", ["Bajo", "Medio", "Alto"], index=1)
        val4 = ["Bajo", "Medio", "Alto"].index(val4)
        
        st.markdown("<div class='section'><h4>🏥 Historial Médico</h4></div>", unsafe_allow_html=True)
        val5 = st.checkbox("Hipertensión", value=False)
        val5 = 1 if val5 else 0
        val6 = st.checkbox("Diabetes", value=False)
        val6 = 1 if val6 else 0
        val8 = st.checkbox("Obesidad", value=False)
        val8 = 1 if val8 else 0
        val25 = st.checkbox("Enfermedad cardíaca previa", value=False)
        val25 = 1 if val25 else 0
        val26 = st.checkbox("Medicación cardiovascular", value=False)
        val26 = 1 if val26 else 0
        val27 = st.checkbox("Participó en campaña de detección", value=False)
        val27 = 1 if val27 else 0

with col2:
    with st.container():
        st.markdown("<div class='section'><h4>❤️ Indicadores Clínicos</h4></div>", unsafe_allow_html=True)
        val7 = st.slider("**Colesterol total (mg/dL)**", min_value=50, max_value=300, step=1, value=180)
        val18 = st.slider("**Presión arterial sistólica (mmHg)**", min_value=100, max_value=180, step=5, value=120)
        val19 = st.slider("**Presión arterial diastólica (mmHg)**", min_value=60, max_value=100, step=5, value=80)
        val20 = st.slider("**Glucosa en sangre (mg/dL)**", min_value=70, max_value=180, step=1, value=90)
        val21 = st.slider("**Colesterol HDL (mg/dL)**", min_value=30, max_value=90, step=1, value=50)
        val22 = st.slider("**Colesterol LDL (mg/dL)**", min_value=60, max_value=180, step=1, value=100)
        val23 = st.slider("**Triglicéridos (mg/dL)**", min_value=100, max_value=300, step=1, value=150)
        val24 = st.selectbox("**Resultados EKG**", ["Normal", "Anormal"], index=0)
        val24 = 0 if val24 == "Normal" else 1
        
        st.markdown("<div class='section'><h4>🚬 Estilo de Vida</h4></div>", unsafe_allow_html=True)
        val11 = st.radio("**Consumo de tabaco**", ["Nunca", "Ex-fumador", "Actualmente"], horizontal=True)
        val11 = ["Nunca", "Ex-fumador", "Actualmente"].index(val11)
        val12 = st.radio("**Consumo de alcohol**", ["Nunca", "Moderado", "Alto"], horizontal=True)
        val12 = [-1, 0, 1][["Nunca", "Moderado", "Alto"].index(val12)]
        val13 = st.radio("**Actividad física**", ["Sedentario", "Moderado", "Activo"], horizontal=True)
        val13 = ["Sedentario", "Moderado", "Activo"].index(val13)
        val14 = st.radio("**Hábitos alimentarios**", ["Poco saludables", "Saludables"], horizontal=True)
        val14 = 0 if val14 == "Poco saludables" else 1
        val9 = st.slider("**Circunferencia abdominal (cm)**", min_value=50, max_value=150, step=1, value=80)
        val10 = st.checkbox("Historia familiar de enfermedades cardíacas", value=False)
        val10 = 1 if val10 else 0
        val16 = st.select_slider("**Nivel de estrés**", options=["Bajo", "Moderado", "Alto"])
        val16 = ["Bajo", "Moderado", "Alto"].index(val16)
        val17 = st.slider("**Horas de sueño diarias**", min_value=4, max_value=10, step=1, value=7)
        val15 = st.select_slider("**Exposición a contaminación del aire**", options=["Baja", "Moderada", "Alta"])
        val15 = ["Baja", "Moderada", "Alta"].index(val15)

# Botón de predicción centrado
c1, c2, c3 = st.columns([1,2,1])
with c2:
    predict_btn = st.button("🔍 Evaluar mi riesgo cardiovascular")

# Resultados - Esto aparecerá solo después de hacer clic
if predict_btn:
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13, val14, val15, val16, val17, val18, val19, val20, val21, val22, val23, val24, val25, val26, val27]])[0])
    
    with st.container():
        st.markdown("<div class='prediction-box'>", unsafe_allow_html=True)
        
        if prediction == "1":
            st.error("""
            ## ⚠️ Alto Riesgo Cardiovascular
            
            Nuestra evaluación indica que tienes un perfil de riesgo elevado.
            Te recomendamos consultar con un especialista lo antes posible.
            
            💡 Consejos:
            - Programa una cita médica
            - Revisa tus hábitos alimenticios
            - Realiza actividad física regular
            - Controla tus niveles de estrés
            """)
        else:
            st.success("""
            ## ❤️ Riesgo Cardiovascular Bajo
            
            Tus indicadores actuales sugieren un perfil cardiovascular saludable.
            Continúa con tus buenos hábitos y realiza chequeos anuales preventivos.
            
            👍 Buenas prácticas:
            - Mantén una dieta equilibrada
            - Realiza ejercicio regular
            - Duerme 7-8 horas diarias
            - Evita el tabaco y alcohol en exceso
            """)
            
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Nota legal
        st.markdown("""
        <div style="text-align: center; margin-top: 1rem; font-size: 0.8rem; color: #666;">
        <i>Esta herramienta no sustituye una evaluación médica profesional. Los resultados son meramente indicativos.</i>
        </div>
        """, unsafe_allow_html=True)

# Nota al pie
st.markdown("""
<div style="text-align: center; margin-top: 3rem; color: #666;">
<p>© 2023 CardioPredict - Sistema de Inteligencia Artificial para Salud Cardiovascular</p>
</div>
""", unsafe_allow_html=True)
