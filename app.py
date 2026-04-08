import streamlit as st
from datetime import datetime, timezone, timedelta, date
from decimal import Decimal, getcontext
import random

# Elevamos la precisión para la arquitectura del Teorema de Torres
getcontext().prec = 150

# --- CONFIGURACIÓN DE ACCESO ---
# Nota: En producción real, estos valores pueden ir en st.secrets
CLAVE_CORRECTA = "Nandino2026"
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
        line-height: 1.6;
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
            st.error("Identidad no validada. Acceso al Reloj de Tinta Seca denegado.")
    st.stop()

# --- CLASE CORE: RELOJ DE TINTA SECA ---
class RelojTinta:
    def __init__(self):
        # El cuerpo poético (M0)
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
            "M
