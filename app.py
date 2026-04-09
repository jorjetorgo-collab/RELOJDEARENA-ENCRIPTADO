import streamlit as st
from datetime import datetime, timezone, timedelta, date
from decimal import Decimal, getcontext
import random

# Configuración de resolución infinitesimal
getcontext().prec = 150
st.set_page_config(page_title="Reloj de Tinta Seca", layout="centered")

CLAVE_CORRECTA = "Nandino2026"

# Carga de la Fase Eli desde Secretos
try:
    ELI_NUMBER_MASTER = Decimal(st.secrets["ELI_KEY"]) if "ELI_KEY" in st.secrets else Decimal("0")
except:
    ELI_NUMBER_MASTER = Decimal("0")

class RelojTinta:
    def __init__(self):
        self.M0 = [
            "Con fuerza y bravura, con discreta amargura, porta una armadura que su alma tortura...",
            "Con ternura usurpa el espacio que el dolor, sin ella con completa soltura ocupa...",
            "Con tinta y sangre el dolor en su piel se tatúa, con aguja en su carne su pasión perpetúa...",
            "De mirada gatuna que en sus ojos acuna lagunas de mieles oscuras...",
            "Ella es la crisálida y yo la oruga, que en vez de alas prefería su cuna...",
            "Ella que en su risa captura lo que los ojos censuran, lo que ante el alma no se oculta...",
            "En sus labios se alojan las uvas, de donde el más fino vino obtiene dulzura...",
            "Es cura de fatua cordura y cual sangre en mis venas circula, y por ellas la poesía continúa...",
            "Es mía la culpa y la condena, no de ella, yo fui El Poeta, ella tan solo la Musa...",
            "Es primavera que pulula con frescura, es otoño y hojas de ojos se derraman y mudan...",
            "Estrella que guía en la bruma, la brújula que aparta las dudas, la que señala la ruta...",
            "La bruja del cuento que embruja a quien incauto su nombre conjura...",
            "La estela que veloz se fuga dejando heridas que no suturan...",
            "La exquisita tortura de quien naufraga en su mirada y encuentra lujuria...",
            "Mancuerna de fosos, centellas gemelas que en el cosmos fulguran...",
            "Nada en el mundo está a su altura, ni el pulso de Miguel Ángel, ni la pluma de Neruda...",
            "No pregunten si el pecado valió la penuria, yo sería Sócrates si ella fuese cicuta...",
            "Por más que huya y se oculta, no hay fuga de lo que con fuego en el alma se incuba...",
            "Si es baile es finura y estructura, áurea cuando es pintura, dura si se habla de literatura...",
            "Si sus labios mi nombre murmuran, si algún día me conjura, que veloz mi alma a ella acuda...",
            "Su rara realeza de heroica figura, divina belleza de humilde postura...",
            "Sus pisadas tal vez sean diminutas, pero donde pisa los cielos se inmutan...",
            "Un canto para cada desvelo de la luna, un soneto del amor que jamás se consuma...",
            "Yo la amaba y no me importaba ser su puta, sin derechos ni disputas..."
        ]
        self.T0 = datetime(2026, 4, 16, 0, 0, 0, tzinfo=timezone.utc)
        self.E, self.P = Decimal('2.7182818284'), Decimal('1.6180339887')

    def desordenar(self, mn):
        res = list(self.M0)
        for i in range(len(res) - 1, 0, -1):
            random.seed(str(Decimal(str(mn + i)) * self.E * (self.P ** (i + 5)) * ELI_NUMBER_MASTER))
            j = random.randint(0, i)
            res[i], res[j] = res[j], res[i]
        return res

reloj = RelojTinta()

# Gestión de Colores y Modo Nocturno
if 'nocturno' not in st.session_state: st.session_state['nocturno'] = False

# Paleta
if st.session_state['nocturno']:
    bg, txt, border, accent = "#000000", "#FFFFFF", "#FF0000", "#FF0000"
else:
    bg, txt, border, accent = "#FDFEFE", "#1B2631", "#1A5276", "#1A5276"

# Inyección de CSS para forzar la tipografía en toda la app
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime&display=swap');
    
    html, body, [class*="st-"] {{
        font-family: 'Courier Prime', monospace !important;
        background-color: {bg} !important;
        color: {txt} !important;
    }}
    .stTextInput>div>div>input {{ color: {txt} !important; font-family: 'Courier Prime' !important; }}
    .stButton>button {{ border-color: {accent} !important; font-family: 'Courier Prime' !important; color: {txt} !important; }}
    </style>
""", unsafe_allow_html=True)

# Autenticación
if 'auth' not in st.session_state: st.session_state['auth'] = False
if not st.session_state['auth']:
    st.markdown(f'<h1 style="text-align:center; font-family:\'Courier Prime\'">Sincronización de Identidad</h1>', unsafe_allow_html=True)
    pw = st.text_input("Clave de Acceso:", type="password")
    if st.button("Sincronizar"):
        if pw == CLAVE_CORRECTA:
            st.session_state['auth'] = True
            st.rerun()
        else: st.error("Incertidumbre detectada.")
    st.stop()

# --- BARRA LATERAL (Panel de Control) ---
with st.sidebar:
    st.markdown(f'<h3 style="color:{accent}">Panel del Trayector</h3>', unsafe_allow_html=True)
    if st.button("🌓 Cambiar Modo"):
        st.session_state['nocturno'] = not st.session_state['nocturno']
        st.rerun()
    
    st.markdown("---")
    metodo = st.radio("Modo de Búsqueda:", ["Poesía Continua #", "Reloj Temporal"])
    
    mn_final = 0
    lbl_time = ""

    if metodo == "Reloj Temporal":
        f = st.date_input("Fecha", value=date(2026, 4, 16))
        h = st.time_input("Hora")
        ms = st.number_input("Microsegundos", 0, 999999, 0)
        dt = datetime.combine(f, h).replace(microsecond=ms, tzinfo=timezone.utc)
        diff = dt - reloj.T0
        u = (Decimal(diff.days)*86400000000) + (Decimal(diff.seconds)*1000000) + Decimal(dt.microsecond)
        mn_final = int(u * reloj.E * (reloj.P ** 2))
        lbl_time = dt.strftime('%Y, %B, %d, %H:%M:%S') + f":{dt.microsecond:06d}"
    else:
        mn_input = st.text_input("Poesía Continua #:", "0")
        try: mn_final = int(mn_input)
        except: mn_final = 0
        lbl_time = "Sincronización Manual"

# --- CUERPO PRINCIPAL ---
st.markdown(f'<h1 style="text-align:center; font-family:\'Courier Prime\'; color:{txt}">Reloj de Tinta Seca</h1>', unsafe_allow_html=True)

versos = reloj.M0 if mn_final == 0 else reloj.desordenar(mn_final)

# Caja del Poema
st.markdown(f"""
<div style="border:2px solid {border}; padding:40px; border-radius:10px; background-color:{bg}; color:{txt}; font-family:'Courier Prime', monospace; margin-top:20px;">
    <div style="font-size:1.1em; line-height:1.8; margin-bottom: 40px;">
        {'<br>'.join(versos)}
    </div>
    <hr style="border:0.5px solid {border};">
    <div style="text-align:right; font-size:0.9em; line-height:1.5; opacity:0.9;">
        {lbl_time}<br>
        Reloj de Tinta Seca: Poesía Continua #{mn_final}
    </div>
</div>
""", unsafe_allow_html=True)
