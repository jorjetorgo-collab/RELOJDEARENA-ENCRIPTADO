import streamlit as st
from datetime import datetime, timezone, date
from decimal import Decimal, getcontext
import random

# 1. Configuración de Precisión y Página
getcontext().prec = 150
st.set_page_config(page_title="Reloj de Tinta Seca", layout="wide")

CLAVE_CORRECTA = "Nandino2026"

# 2. Carga de la Fase Eli
try:
    if "ELI_KEY" in st.secrets:
        ELI_NUMBER_MASTER = Decimal(st.secrets["ELI_KEY"])
    else:
        ELI_NUMBER_MASTER = Decimal("0")
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

# 3. Gestión de Estado
if 'nocturno' not in st.session_state:
    st.session_state['nocturno'] = False
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

# 4. Paleta de Colores
if st.session_state['nocturno']:
    bg, txt, border, accent = "#000000", "#FFFFFF", "#FF0000", "#FF0000"
else:
    bg, txt, border, accent = "#FDFEFE", "#1B2631", "#1A5276", "#FF4B4B"

# 5. CSS
css_code = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime&display=swap');
html, body, [class*="st-"] {{
    font-family: 'Courier Prime', monospace !important;
    background-color: {0} !important;
    color: {1} !important;
}}
.poema-box {{
    border: 2px solid {2};
    padding: 40px;
    border-radius: 10px;
    background-color: {0};
    width: 92%;
    margin: auto;
    white-space: nowrap;
    overflow: hidden;
}}
input[type="checkbox"], input[type="radio"] {{
    accent-color: {3} !important;
}}
</style>
""".format(bg, txt, border, accent)
st.markdown(css_code, unsafe_allow_html=True)

# 6. Autenticación
if not st.session_state['auth']:
    st.markdown('<h1 style="text-align:center;">Sincronización de Identidad</h1>', unsafe_allow_html=True)
    pw = st.text_input("Clave de Acceso:", type="password")
    if st.button("Validar Trayectoria"):
        if pw == CLAVE_CORRECTA:
            st.session_state['auth'] = True
            st.rerun()
        else:
            st.error("Identidad no reconocida.")
    st.stop()

# 7. SIDEBAR
with st.sidebar:
    st.markdown(f'<h2 style="color:{border};">Hardware Trayector</h2>', unsafe_allow_html=True)
    
    if st.button("🌓 Cambiar Modo"):
        st.session_state['nocturno'] = not st.session_state['nocturno']
        st.rerun()
    
    st.markdown("---")
    ver_ui = st.checkbox("🔽 Mostrar Opciones", value=True)
    
    mn_final = 0
    now = datetime.now(timezone.utc)
    lbl_time = now.strftime('%Y, %B, %d, %H:%M:%S')

    if ver_ui:
        st.markdown("---")
        # Selector de Modo (Marcadores)
        metodo = st.radio(
            "Dimensión de Búsqueda:",
            ("Reloj Temporal", "Identificador de Poesía")
        )
        
        st.markdown("---")

        if metodo == "Identificador de Poesía":
            mn_in = st.text_input("Ingresar ID de Poesía:", "1")
            try:
                mn_final = int(mn_in)
            except:
                mn_final = 1
            lbl_time = "Búsqueda por Identificador"
        else:
            f = st.date_input("Fecha", value=date(2026, 4, 16))
            h = st.time_input("Hora")
            ms = st.number_input("Microsegundos", 0, 999999, 0)
            
            dt = datetime.combine(f, h).replace(microsecond=ms, tzinfo=timezone.utc)
            diff = dt - reloj.T0
            u = (Decimal(diff.days)*86400000000) + (Decimal(diff.seconds)*1000000) + Decimal(dt.microsecond)
            mn_final = int(u * reloj.E * (reloj.P ** 2))
            lbl_time = dt.strftime('%Y, %B, %d, %H:%M:%S') + f":{dt.microsecond:06d}"

# 8. CUERPO
st.markdown('<h1 style="text-align:center;">Reloj de Tinta Seca</h1>', unsafe_allow_html=True)

# Lógica de versos
versos = reloj.desordenar(mn_final) if mn_final != 0 else reloj.M0
poema_html = '<br>'.join(versos)

st.markdown(f"""
<div class="poema-box">
    <div style="font-size: 0.95vw; line-height: 2.1;">
        {poema_html}
    </div>
    <hr style="border: 0.5px solid {border}; margin-top: 40px;">
    <div style="text-align: right; font-size: 0.85em; opacity: 0.8;">
        {lbl_time}<br>
        Reloj de Tinta Seca: Poesía Continua #{mn_final}
    </div>
</div>
""", unsafe_allow_html=True)
