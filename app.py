import streamlit as st
from datetime import datetime, timezone, date, time, timedelta
from decimal import Decimal, getcontext
import random

# 1. Configuración de Precisión y Página
getcontext().prec = 150
st.set_page_config(page_title="Reloj de Tinta Seca", layout="wide")
CLAVE_CORRECTA = "Nandino2026"

# 2. Carga de la Fase Eli
try:
    ELI_NUMBER_MASTER = Decimal(st.secrets.get("ELI_KEY", "0"))
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

# 3. Gestión de Estado y Colores
if 'nocturno' not in st.session_state: st.session_state['nocturno'] = False
if 'auth' not in st.session_state: st.session_state['auth'] = False

bg, txt, brd = ("#000000", "#FFFFFF", "#FF0000") if st.session_state['nocturno'] else ("#FDFEFE", "#1B2631", "#1A5276")

# 4. CSS Maestro (Garantiza visibilidad total)
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime&display=swap');
[data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"], .stApp {{
    background-color: {bg} !important;
}}
html, body, [class*="st-"], h1, h2, h3, p, label, span, div, input, button {{
    font-family: 'Courier Prime', monospace !important;
    color: {txt} !important;
}}
input {{
    background-color: {bg} !important;
    border: 1px solid {brd} !important;
    color: {txt} !important;
}}
.poema-box {{
    border: 2px solid {brd}; 
    padding: 35px; 
    border-radius: 10px;
    background-color: {bg}; 
    width: 95%; 
    margin: auto; 
    overflow-x: auto;
    white-space: nowrap;
}}
hr {{ border-top: 1px solid {brd} !important; opacity: 0.5; }}
</style>
""", unsafe_allow_html=True)

# 5. Autenticación
if not st.session_state['auth']:
    st.markdown('<h1 style="text-align:center;">Sincronización de Identidad</h1>', unsafe_allow_html=True)
    pw = st.text_input("Clave de Acceso:", type="password")
    if st.button("Validar Trayectoria"):
        if pw == CLAVE_CORRECTA:
            st.session_state['auth'] = True
            st.rerun()
        else: st.error("Identidad no reconocida.")
    st.stop()

# 6. Sidebar y Lógica de Sincronización
with st.sidebar:
    st.markdown(f'<h2 style="color:{brd};">Hardware Trayector</h2>', unsafe_allow_html=True)
    if st.button("🌓 Cambiar Modo"):
        st.session_state['nocturno'] = not st.session_state['nocturno']
        st.rerun()
    st.markdown("---")
    ver_ui = st.checkbox("🔽 Opciones", value=True)
    
    mn_final = 0
    lbl_time = reloj.T0.strftime('%Y-%m-%d %H:%M:%S') + ".000000"

    if ver_ui:
        metodo = st.radio("Dimensión:", ("Reloj Temporal", "Identificador"))
        if metodo == "Identificador":
            mn_in = st.text_input("ID (Escribir número):", "")
            if mn_in:
                try: 
                    mn_final = int(mn_in)
                    u_rec = Decimal(mn_final) / (reloj.E * (reloj.P ** 2))
                    seg_rec = float(u_rec / 1000000)
                    dt_rec = reloj.T0 + timedelta(seconds=seg_rec)
                    lbl_time = dt_rec.strftime('%Y-%m-%d %H:%M:%S') + f":{dt_rec.microsecond:06d}"
                except: mn_final = 0
        else:
            f_in = st.text_input("Fecha (AAAA-MM-DD):", placeholder="Ej: 2026-04-16")
            h_in = st.text_input("Hora (HH:MM:SS):", placeholder="Ej: 14:30:05")
            ms = st.number_input("µs (Microsegundos):", 0, 999999, 0)
            
            if f_in and h_in:
                try:
                    f = datetime.strptime(f_in, "%Y-%m-%d").date()
                    h = datetime.strptime(h_in, "%H:%M:%S").time()
                    dt = datetime.combine(f, h).replace(microsecond=ms, tzinfo=timezone.utc)
                    
                    diff = dt - reloj.T0
                    u = (Decimal(diff.days)*86400000000) + (Decimal(diff.seconds)*1000000) + Decimal(dt.microsecond)
                    mn_final = int(u * reloj.E * (reloj.P ** 2))
                    lbl_time = dt.strftime('%Y-%m-%d %H:%M:%S') + f":{dt.microsecond:06d}"
                except ValueError:
                    st.sidebar.warning("Use formatos AAAA-MM-DD y HH:MM:SS")

# 7. Main UI
st.markdown('<h1 style="text-align:center;">Reloj de Tinta Seca</h1>', unsafe_allow_html=True)
versos = reloj.M0 if mn_final == 0 else reloj.desordenar(mn_final)
poema_html = '<br>'.join(versos)

st.markdown(f"""
<div class="poema-box">
    <div style="font-size: 0.88vw; line-height: 2.1;">{poema_html}</div>
    <hr>
    <div style="text-align: right; font-size: 0.85em; opacity: 0.8;">
        Reloj de Tinta Seca: {lbl_time}<br>Poesía Continua #{mn_final}
    </div>
</div>
""", unsafe_allow_html=True)
