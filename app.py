import streamlit as st
from datetime import datetime, timezone, timedelta, date
from decimal import Decimal, getcontext
import random

# 1. CONFIGURACIÓN DE PRECISIÓN
getcontext().prec = 150

# 2. CONFIGURACIÓN DE PÁGINA (Debe ir al inicio)
st.set_page_config(page_title="Reloj de Tinta Seca", page_icon="⏳", layout="centered")

# 3. VARIABLES DE ACCESO
CLAVE_CORRECTA = "Nandino2026"

# Extracción de la llave invisible de los Secretos
try:
    if "ELI_KEY" in st.secrets:
        ELI_NUMBER_MASTER = Decimal(st.secrets["ELI_KEY"])
    else:
        ELI_NUMBER_MASTER = None
except Exception:
    ELI_NUMBER_MASTER = None

# 4. VERIFICACIÓN DE SEGURIDAD
if ELI_NUMBER_MASTER is None:
    st.error("❌ ERROR CRÍTICO: Constante de Fase no detectada.")
    st.info("Configura 'ELI_KEY' en los secretos del servidor.")
    st.stop()

# 5. CLASE CORE
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

# 6. INTERFAZ DE AUTENTICACIÓN
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

# 7. PANEL DE CONTROL (SIDEBAR)
st.sidebar.title("🛠️ Auditoría")
fase_input = st.sidebar.number_input("Clave de Fase (Eli #)", format="%.8f", step=0.00000001, value=0.00000000)
metodo =
