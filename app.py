import streamlit as st
from datetime import datetime, timezone, timedelta, date
from decimal import Decimal, getcontext
import random

# Elevamos la precisión para la arquitectura del Teorema de Torres
getcontext().prec = 150

# --- CONFIGURACIÓN DE ACCESO ---
CLAVE_CORRECTA = "Nandino2026"

# EL NÚMERO ELI (La única constante de fase)
ELI_NUMBER_MASTER = Decimal('0.31052094')

st.set_page_config(page_title="Reloj de Tinta Seca", page_icon="⏳", layout="centered")

# --- ESTÉTICA DEL TRAYECTOR ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .poema-container {
        border: 4px solid #1a5276;
        padding: 40px;
        border-radius: 25px;
        background-color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: 15px 15px 35px rgba(0,0,0,0.2);
        color: #1b2631;
        line-height: 1.7;
    }
    .footer-data {
        text-align: right; 
        color: #5d6d7e; 
        font-size: 0.9em;
        margin-top: 25px;
        border-top: 1px solid #eee;
        padding-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- VALIDACIÓN DE IDENTIDAD ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    st.title("⏳ Acceso al Trayector")
    st.write("Se requiere validación de autor para estabilizar la entropía.")
    pw = st.text_input("Introduce la clave de acceso:", type="password")
    if st.button("Validar Identidad"):
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

# --- PANEL DE CONTROL ---
st.sidebar.title("🛠️ Auditoría Teórica")
st.sidebar.markdown("---")

fase_input = st.sidebar.number_input("Clave de Fase (Eli #)", format="%.8f", step=0.00000001, value=0.00000000)

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

st.markdown(f"""
    <div class="poema-container">
        {"<br>".join(versos_finales)}
        <div class="footer-data">
            <b>Identidad Temporal:</b> {label_tiempo}<br>
            <b>Fase Eli:</b> {fase_input:.8f}<br>
            <span style="color: #1a5276;"><b>TRAYECTOR: #{mn}</b></span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Indicadores de Auditoría
if Decimal(str(fase_input)) == ELI_NUMBER_MASTER:
    st.sidebar.success("✔️ FASE ELIZABETH ESTABLE")
else:
    st.sidebar.warning("⚠️ SISTEMA EN DERIVA ENTRÓPICA")

st.sidebar.markdown("---")
st.sidebar.caption("Propiedad Intelectual de Jorge Torres. Teorema de la Identidad Informativa.")
