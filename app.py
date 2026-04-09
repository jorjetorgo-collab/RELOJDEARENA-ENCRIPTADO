# 6. Sidebar
with st.sidebar:
    st.markdown(f'<h2 style="color:{brd};">Hardware Trayector</h2>', unsafe_allow_html=True)
    if st.button("🌓 Cambiar Modo"):
        st.session_state['nocturno'] = not st.session_state['nocturno']
        st.rerun()
    st.markdown("---")
    ver_ui = st.checkbox("🔽 Opciones", value=True)
    mn_final = 0
    lbl_time = "Esperando Coordenada..."

    if ver_ui:
        metodo = st.radio("Dimensión:", ("Reloj Temporal", "Identificador"))
        if metodo == "Identificador":
            mn_in = st.text_input("ID (Ingresar manualmente):", "")
            if mn_in:
                try: 
                    mn_final = int(mn_in)
                except: 
                    mn_final = 1
            lbl_time = "Selección Manual"
        else:
            # Campos de texto para forzar entrada manual
            f_in = st.text_input("Fecha (YYYY-MM-DD):", placeholder="Ej: 2026-04-16")
            h_in = st.text_input("Hora (HH:MM):", placeholder="Ej: 12:00")
            ms = st.number_input("µs (Microsegundos):", 0, 999999, 0)
            
            if f_in and h_in:
                try:
                    # Intento de conversión de strings a objetos datetime
                    f = datetime.strptime(f_in, '%Y-%m-%d').date()
                    h = datetime.strptime(h_in, '%H:%M').time()
                    dt = datetime.combine(f, h).replace(microsecond=ms, tzinfo=timezone.utc)
                    
                    # Cálculo de Momentum (M_n)
                    diff = dt - reloj.T0
                    u = (Decimal(diff.days)*86400000000) + (Decimal(diff.seconds)*1000000) + Decimal(dt.microsecond)
                    mn_final = int(u * reloj.E * (reloj.P ** 2))
                    lbl_time = dt.strftime('%Y-%m-%d %H:%M:%S') + f":{dt.microsecond:06d}"
                except ValueError:
                    st.error("Formato de fecha u hora incorrecto.")
                except Exception:
                    st.error("Error en el cálculo de trayectoria.")
