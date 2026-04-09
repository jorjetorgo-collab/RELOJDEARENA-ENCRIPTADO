# --- SIDEBAR (Hardware) ---
with st.sidebar:
    st.markdown(f'<h2 style="color:{border};">Hardware Trayector</h2>', unsafe_allow_html=True)
    if st.button("🌓 Modo Nocturno"):
        st.session_state['nocturno'] = not st.session_state['nocturno']
        st.rerun()
    
    st.markdown("---")
    ver_ui = st.checkbox("🔽 Mostrar Panel de Control", value=True)
    
    mn_final = 0
    now = datetime.now(timezone.utc)
    lbl_time = now.strftime('%Y, %B, %d, %H:%M:%S')

    if ver_ui:
        st.markdown("---")
        
        # Cuadro de opción para elegir el modo de entrada
        metodo = st.radio(
            "Seleccionar Dimensión de Búsqueda:",
            ("Coordenada Temporal", "Identificador de Poesía"),
            index=0
        )
        
        st.markdown("---")

        if metodo == "Identificador de Poesía":
            st.write("### Búsqueda por ID")
            mn_in = st.text_input("Ingresar # de Poesía:", "0")
            try:
                mn_final = int(mn_in)
            except:
                mn_final = 0
            lbl_time = "Búsqueda Manual: ID Protegido"
        else:
            st.write("### Reloj Temporal")
            f = st.date_input("Fecha", value=date(2026, 4, 16))
            h = st.time_input("Hora")
            ms = st.number_input("Microsegundos", 0, 999999, 0)
            
            dt = datetime.combine(f, h).replace(microsecond=ms, tzinfo=timezone.utc)
            diff = dt - reloj.T0
            
            # Cálculo de momentum
            u = (Decimal(diff.days)*86400000000) + (Decimal(diff.seconds)*1000000) + Decimal(dt.microsecond)
            mn_final = int(u * reloj.E * (reloj.P ** 2))
            
            lbl_time = dt.strftime('%Y, %B, %d, %H:%M:%S') + f":{dt.microsecond:06d}"
