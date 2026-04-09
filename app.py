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

# 4. CSS Maestro
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
