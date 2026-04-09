# 4. CSS Maestro (Asegúrate de que termine con """)
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
div[data-baseweb="radio"] div, div[data-baseweb="checkbox"] div {{ border-color: {brd} !important; }}
input[type="radio"]:checked + div {{ background-color: {brd} !important; }}
hr {{ border-top: 1px solid {brd} !important; opacity: 0.5; }}
</style>
""", unsafe_allow_html=True) # <--- Revisa que existan las tres comillas aquí
