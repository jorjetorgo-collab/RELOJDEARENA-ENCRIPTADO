# ... (Todo el código anterior de autenticación y lógica permanece igual) ...

# --- RENDERIZADO FINAL ---
st.title("⏳ El Reloj de Tinta Seca")

if mn == 0 and metodo == "Número de Reloj (#)":
    versos_finales = reloj.M0
else:
    versos_finales = reloj.desordenar(mn, fase_input)

st.markdown(f"""
    <div style="border:4px solid #1a5276; padding:40px; border-radius:25px; background-color:white; font-family:monospace;">
        {"<br>".join(versos_finales)}
        <div style="text-align:right; margin-top:20px; font-size:0.9em; color:gray;">
            <b>Identidad:</b> {label_tiempo}<br>
            <b>Fase:</b> {fase_input:.8f}<br>
            <b># TRAYECTOR: {mn}</b>
        </div>
    </div>
""", unsafe_allow_html=True)

if Decimal(str(fase_input)) == ELI_NUMBER_MASTER:
    st.sidebar.success("✔️ FASE ELIZABETH ESTABLE")
else:
    st.sidebar.warning("⚠️ SISTEMA EN DERIVA ENTRÓPICA")

# EL ARCHIVO DEBE TERMINAR AQUÍ. NO ESCRIBAS NADA MÁS ABAJO.
