import streamlit as st
from datetime import datetime, timezone, timedelta, date
from decimal import Decimal, getcontext
import random

# Elevamos la precisión para la arquitectura del Teorema de Torres
getcontext().prec = 150

# --- CONFIGURACIÓN DE ACCESO ---
CLAVE_CORRECTA = "Nandino2026"
# EL SECRETO DEL AUTOR (Diferencial de Fase)
DELTA_PHI_REAL = Decimal('3.1415') 

st.set_page_config(page_title="Reloj de Tinta Seca", page_icon="⏳", layout="centered")

# --- ESTÉTICA DEL TRAYECTOR ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .poema-container {
        border: 3px solid #1a5276;
        padding: 35px;
        border-radius: 20px;
        background-color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: 10px 10px 25px rgba(0,0,0,0.15);
        color: #1b2631;
    }
    .footer-data {
        text-align: right; 
        color: #5d6d7e; 
        font-size: 0.85em;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- VALIDACIÓN DE IDENTIDAD ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    st.title("⏳ Acceso al Trayector")
    st.write("Se requiere validación de autor para consultar la entropía de la obra.")
    pw = st.text_input("Introduce la clave de acceso:", type="password")
    if st.button("Validar Trayector"):
        if pw == CLAVE_CORRECTA:
            st.session_state['autenticado'] = True
            st.rerun()
        else:
            st.error("Identidad no validada. Acceso denegado.")
    st.stop()

# --- CLASE CORE: RELOJ DE TINTA SECA ---
class RelojTinta:
    def __init__(self):
        self.M0 = [
            "Con fuerza y bravura, con discreta amargura, porta una armadura que su alma tortura",
            "Con ternura usurpa el espacio que el dolor, sin ella con completa soltura ocupa",
            "Con tinta y sangre el dolor en su piel se tatúa, con aguja en su carne su pasión perpetúa",
            "De mirada gatuna que en sus ojos acuna lagunas de mieles oscuras",
            "Ella es la crisálida y yo la oruga, que en vez de alas prefería su cuna",
            "Ella que en su risa captura lo que los ojos censuran, lo que ante el alma no se oculta",
            "En sus labios se alojan las uvas, de donde el más fino vino obtiene dulzura",
            "Es cura de fatua cordura y cual sangre en mis venas circula, y por ellas la poesía continúa",
            "Es mía la culpa y la condena, no de ella, yo fui El Poeta, ella tan solo la Musa",
            "Es primavera que pulula con frescura, es otoño y hojas de ojos se derraman y mudan",
            "Estrella que guía en la bruma, la brújula que aparta las dudas, la que señala la ruta",
            "La bruja del cuento que embruja a quien incauto su nombre conjura",
            "La estela que veloz se fuga dejando heridas que no suturan",
            "La exquisita tortura de quien naufraga en su mirada y encuentra lujuria",
            "Mancuerna de fosos, centellas gemelas que en el cosmos fulguran",
            "Nada en el mundo está a su altura, ni el pulso de Miguel Ángel, ni la pluma de Neruda",
            "No pregunten si el pecado valió la penuria, yo sería Sócrates si ella fuese cicuta",
            "Por más que huya y se oculta, no hay fuga de lo que con fuego en el alma se incuba",
            "Si es baile es finura y estructura, áurea cuando es pintura, dura si se habla de literatura",
            "Si sus labios mi nombre murmuran, si algún día me conjura, que veloz mi alma a ella acuda",
            "Su rara realeza de heroica figura, divina belleza de humilde postura",
            "Sus pisadas tal vez sean diminutas, pero donde pisa los cielos se inmutan",
            "Un canto para cada desvelo de la luna, un soneto del amor que jamás se consuma",
            "Yo la amaba y no me importaba ser su puta, sin derechos ni disputas"
        ]
        self.T0 = datetime(2026, 4, 16, 0, 0, 0, tzinfo=timezone.utc)
        self.E = Decimal('2.71828182845904523536')
        self.P = Decimal('1.61803398874989484820')

    def desordenar(self, mn, diferencial):
        res = list(self.M0)
        
        # --- LÓGICA DE CAJA NEGRA (Diferencial de Fase) ---
        # Si el diferencial es incorrecto, inyectamos ruido temporal (inestabilidad)
        if diferencial != DELTA_PHI_REAL:
            # El ruido hace que el resultado cambie cada milisegundo aunque el # sea el mismo
            ruido = Decimal(datetime.now().microsecond) 
            ajuste_fase = diferencial * ruido
        else:
            # Si es correcto (3.1415), el ajuste es una constante pura (estabilidad)
            ajuste_fase = diferencial

        for i in range(len(res) - 1, 0, -1):
            # La semilla ahora depende críticamente del ajuste_fase
            seed_val = Decimal(str(mn + i)) * self.E * (self.P ** (i + 5)) * ajuste_fase
            
            # Usamos random con la semilla calculada para el Fisher-Yates
            random.seed(str(seed_val))
            j = random.randint(0, i)
            res[i], res[j] = res[j], res[i]
        return res

reloj = RelojTinta()

# --- PANEL DE CONTROL ---
st.title("⏳ Auditoría: Reloj de Tinta Seca")
st.sidebar.header("Coordenadas Temporales")

# NUEVA CASILLA: Diferencial de Fase (La Caja Negra)
st.sidebar.subheader("Calibración Teórica")
df_input = st.sidebar.number_input("Diferencial de Fase (ΔΦ)", format="%.4f", step=0.0001, help="Parámetro de estabilidad para el Teorema de Torres.")
