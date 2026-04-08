import streamlit as st
from datetime import datetime, timezone, timedelta, date
from decimal import Decimal, getcontext
import random

getcontext().prec = 150

# --- CONFIGURACIÓN DE ACCESO ---
CLAVE_CORRECTA = "Nandino2026"

# Extracción de la llave invisible de los Secretos de Streamlit
try:
    if "ELI_KEY" in st.secrets:
        ELI_NUMBER_MASTER = Decimal(st.secrets["ELI_KEY"])
    else:
        ELI_NUMBER_MASTER = None
except Exception:
    ELI_NUMBER_MASTER = None

st.set_page_config(page_title="Reloj de Tinta Seca", page_icon="⏳", layout="centered")

# Verificación de la presencia de la constante en el servidor
if ELI_NUMBER_MASTER is None:
    st.error("❌ ERROR CRÍTICO: Constante de Fase no detectada.")
    st.info("El sistema requiere la configuración de 'ELI_KEY' en los secretos del servidor para operar.")
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

    def desordenar(self, mn, clave_fase_input):
        res = list(self.M0)
        clave_fase = Decimal(str(clave_fase_input))
        if clave_fase != ELI_NUMBER_MASTER:
            ruido = Decimal(datetime.now().microsecond + 1)
            ajuste_fase = clave_fase * ruido
        else:
            ajuste_fase = clave_fase
        for i in range(len(res) - 1, 0, -1):
            seed_val = Decimal(str(mn + i)) * self.E * (self.P ** (i + 5)) * ajuste_fase
            random.seed(str(seed_val))
            j = random.randint(0, i)
            res[i], res[j] = res[j], res[i]
        return res

reloj = RelojTinta()

# --- INTERFAZ DE AUTENTICACIÓN ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    st.title("⏳ Validación de Identidad")
    pw = st.text_input("Clave de Acceso:", type="password")
    if st.button("Acceder"):
        if pw == CLAVE_CORRECTA:
            st.session_state['autenticado'] = True
            st.rerun()
        else:
            st.error("Acceso denegado.")
    st.stop()

# --- PANEL DE CONTROL ---
st.sidebar.title("🛠️ Auditoría")
fase_input = st.sidebar.number_input("Clave de Fase (Eli #)", format="%.8f", step=0.00000001)
metodo = st.sidebar.radio("Input de Reloj:", ["Número de Reloj (#)", "Coordenada Temporal"])

mn = 0
label_tiempo = ""

if metodo == "Coordenada Temporal":
    f = st.sidebar.date_input("Fecha", value=date(2026, 4, 16))
    h = st.sidebar.time_input("Hora (UTC)", step=60)
    ms = st.sidebar.number_input("μs", 0, 999999, 0)
    dt_obj = datetime.combine(f, h).replace(tzinfo=timezone.utc, microsecond=ms)
    diff = dt_obj - reloj.T0
    u_total = (Decimal(diff.days) * Decimal('86400000000')) + \
              (Decimal(diff.seconds) * Decimal('1000000')) + \
              Decimal(diff.microseconds)
    mn = int(u_total * reloj.E * (reloj.P ** 2)) if u_total >= 0 else 0
    label_tiempo = dt_obj.strftime('%d/%m/%Y | %H:%M:%S.%f')
else:
    mn_in = st.sidebar.text_input("Reloj (#):", value="0")
    try:
        mn = int(mn_in.replace('#','').replace(',','').strip())
    except:
        mn = 0
    u_calc = Decimal(mn) / (reloj.E * (reloj.P ** 2))
    try:
        dt_final = reloj.T0 + timedelta(microseconds=float(u_calc))
        label_tiempo = dt_final.strftime('%d/%m/%Y | %H:%M:%S.%f')
    except:
        label_tiempo = "TRAYECTORIA INDEFINIDA"

# --- RENDERIZADO ---
st.title("⏳ El Reloj de Tinta Seca")

if mn == 0 and metodo == "Número de Reloj (#)":
    versos_finales = reloj.M0
else:
    versos_finales = reloj.desordenar(mn, fase_input)

st
