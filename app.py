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
        # Origen del Trayector (T0): 16 de Abril 2026
        self.T0 = datetime(2026, 4, 16, 0, 0, 0, tzinfo=timezone.utc)
        # Constantes del Teorema de Torres
        self.E = Decimal('2.71828182845904523536')
        self.P = Decimal('1.61803398874989484820')

    def desordenar(self, mn, diferencial_input):
        res = list(self.M0)
        diferencial = Decimal(str(diferencial_input))
        
        # --- LÓGICA DE CAJA NEGRA (Diferencial de Fase) ---
        if diferencial != DELTA_PHI_REAL:
            # Si el diferencial es incorrecto o 0, se inyecta entropía temporal
            # Esto hace que el resultado cambie cada microsegundo (Inestabilidad)
            ruido = Decimal(datetime.now().microsecond + 1)
            ajuste_fase = diferencial * ruido
        else:
            # Si es exacto (3.1415), la fase se estabiliza (Determinismo)
            ajuste_fase = diferencial

        for i in range(len(res) - 1, 0, -1):
            # Semilla condicionada por el diferencial de fase
            seed_val = Decimal(str(mn + i)) * self.E * (self.P ** (i + 5)) * ajuste_fase
            random.seed(str(seed_val))
            j = random.randint(0, i)
            res[i], res[j] = res[j], res[i]
        return res

reloj = RelojTinta()

# --- PANEL DE CONTROL ---
st.title("⏳ Auditoría: Reloj de Tinta Seca")
st.sidebar.header("Coordenadas Temporales")

# Casilla de Diferencial de Fase (La llave de la Caja Negra)
st.sidebar.subheader("Calibración Teórica")
df_input = st.sidebar.number_input("Diferencial de Fase (ΔΦ)", format="%.4f", step=0.0001, value=0.0000, help="Parámetro de estabilidad para el Teorema de Torres.")

opcion = st.sidebar.radio("Método de búsqueda:", ["Calendario (Límite 9999)", "Número Eterno (#)"])

mn = 0
label_tiempo = ""

if opcion == "Calendario (Límite 9999)":
    f = st.sidebar.date_input("Fecha del Trayector", value=date(2026, 4, 16))
    h = st.sidebar.time_input("Hora Exacta (UTC)", step=60)
    ms = st.sidebar.number_input("Microsegundos", 0, 999999, 0)
    
    dt_obj = datetime.combine(f, h).replace(tzinfo=timezone.utc, microsecond=ms)
    diff = dt_obj - reloj.T0
    
    # Conversión a microsegundos con precisión absoluta
    u_total = (Decimal(diff.days) * Decimal('86400000000')) + \
              (Decimal(diff.seconds) * Decimal('1000000')) + \
              Decimal(diff.microseconds)
    
    mn = int(u_total * reloj.E * (reloj.P ** 2)) if u_total >= 0 else 0
    label_tiempo = dt_obj.strftime('%d/%m/%Y | %H:%M:%S.%f')

else:
    mn_in = st.sidebar.text_input("Número de Reloj (#):", value="0")
    try:
        mn = int(mn_in.replace('#','').replace(',','').strip())
    except:
        mn = 0
    
    u_calc = Decimal(mn) / (reloj.E * (reloj.P ** 2))
    try:
        dt_final = reloj.T0 + timedelta(microseconds=float(u_calc))
        label_tiempo = dt_final.strftime('%d/%m/%Y | %H:%M:%S.%f')
    except:
        label_tiempo = "FUERA DEL RANGO HUMANO"

# --- EJECUCIÓN DEL TRAYECTOR ---
if mn == 0 and opcion == "Número Eterno (#)":
    versos_finales = reloj.M0
else:
    versos_finales = reloj.desordenar(mn, df_input)

# --- RENDERIZADO ---
st.markdown(f"""
    <div class="poema-container">
        {"<br>".join(versos_finales)}
        <hr style="border: 0.5px dashed #1a5276; margin-top: 30px;">
        <div class="footer-data">
            Identidad Temporal: {label_tiempo}<br>
            ΔΦ Aplicado: {df_input:.4f}<br>
            <b style="color: #1a5276;">reloj de tinta seca: #{mn}</b>
        </div>
    </div>
""", unsafe_allow_html=True)

# Indicadores de Estado
if Decimal(str(df_input)) == DELTA_PHI_REAL:
    st.sidebar.success("✔️ FASE ESTABILIZADA: Determinismo activo.")
else:
    st.sidebar.warning("⚠️ FASE INESTABLE: Deriva informativa activa.")

st.sidebar.info("Teorema de la Identidad Informativa: Cada microsegundo es una configuración única del ser.")
