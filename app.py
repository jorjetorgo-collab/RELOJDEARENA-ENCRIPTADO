import streamlit as st
from datetime import datetime, timezone, timedelta, date
from decimal import Decimal, getcontext
import random

# Configuración de resolución infinitesimal (Axioma Operativo I)
getcontext().prec = 150
st.set_page_config(page_title="Reloj de Tinta Seca", layout="centered")

CLAVE_CORRECTA = "Nandino2026"

# Carga de la Fase Eli desde Secretos
try:
    if "ELI_KEY" in st.secrets:
        ELI_NUMBER_MASTER = Decimal(st.secrets["ELI_KEY"])
    else:
        ELI_NUMBER_MASTER = Decimal("0")
except:
    ELI_NUMBER_MASTER = Decimal("0")

class RelojTinta:
    def __init__(self):
        # M0 con gramática de continuidad (...)
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

# Gestión de Modo Nocturno
if 'nocturno' not in st.session_state: st.session_state['nocturno'] = False
st.sidebar.title("🛠️ Configuración")
if st.sidebar.button("Modo Nocturno / Diurno"):
    st.session_state['nocturno'] = not st.session_state['nocturno']

# Paleta de Colores
if st.session_state['nocturno']:
    bg, txt, border = "#000000", "#FFFFFF", "#FF0000"  # Negro, Blanco, Rojo
else:
    bg, txt, border = "#FDFEFE", "#1B2631", "#1A5276"  # Blanco, Negro, Azul

# Estilos Globales
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime&display=swap');
    html, body, [class*="st-"] {{
        font-family: 'Courier Prime', monospace;
        background-color: {bg};
        color: {txt};
    }}
    .main-title {{
        font-family: 'Courier Prime', monospace;
        text-align: center;
        font-size: 2.5em;
        padding-bottom: 20px;
        color: {txt};
    }}
    </style>
""", unsafe_allow_html=True)

# Autenticación
if 'auth' not in st.session_state: st.session_state['auth'] = False
if not st.session_state['auth']:
    st.markdown('<h1 class="main-title">Sincronización de Identidad</h1>', unsafe_allow_html=True)
    pw = st.text_input("Clave de Acceso:", type="password")
    if st.button("Entrar"):
        if pw == CLAVE_CORRECTA:
            st.session_state['auth'] = True
            st.rerun()
        else: st.error("Incertidumbre estructural.")
    st.stop()

# Navegación
metodo = st.sidebar.radio("Trayector:", ["Poesía Continua #", "Reloj Temporal"])
mn_final = 0
lbl_time = ""

if metodo == "Reloj Temporal":
    f = st.sidebar.date_input("Fecha", value=date(2026, 4, 16))
    h = st.sidebar.time_input("Hora")
    ms = st.sidebar.number_input("Microsegundos", min_value=0, max_value=999999, value=0)
    dt = datetime.combine(f, h).replace(microsecond=ms, tzinfo=timezone.utc)
    diff = dt - reloj.T0
    u = (Decimal(diff.days)*86400000000) + (Decimal(diff.seconds)*1000000) + Decimal(dt.microsecond)
    mn_final = int(u * reloj.E * (reloj.P ** 2))
    lbl_time = dt.strftime('%Y, %B, %d, %H:%M:%S') + f":{dt.microsecond:06d}"
else:
    try:
        mn_input = st.sidebar.text_input("Poesía Continua #:", "0")
        mn_final = int(mn_input)
    except: mn_final = 0
    lbl_time = "Sincronización Manual"

# Despliegue Principal
st.markdown('<h1 class="main-title">Reloj de Tinta Seca</h1>', unsafe_allow_html=True)

versos = reloj.M0 if mn_final == 0 else reloj.desordenar(mn_final)

st.markdown(f"""
<div style="border:2px solid {border}; padding:35px; border-radius:10px; background-color:{bg}; color:{txt}; font-family:'Courier Prime', monospace;">
    <div style="font-size:1.05em; line-height:1.7;">
        {'<br>'.join(versos)}
    </div>
    <hr style="border:0.5px solid {border}; margin-top:30px;">
    <div style="text-align:right; font-size:0.85em; opacity:0.8;">
        {lbl_time}<br>
        Reloj de Tinta Seca: Poesía Continua #{mn_final}
    </div>
</div>
""", unsafe_allow_html=True)
