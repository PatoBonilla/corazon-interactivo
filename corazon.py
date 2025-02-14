import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configurar la página
st.set_page_config(page_title="Tu Corazón Interactivo", page_icon="❤️")

st.title("💖 Un corazón solo para ti 💖")
st.write("Usa los botones para cambiar la forma del corazón ajustando el valor de k.")

# Inicializar k en session_state
if "k" not in st.session_state:
    st.session_state.k = 1.0  # Valor inicial

# Botones para modificar k
col1, col2, col3 = st.columns([1, 2, 1])  # Distribución del layout

with col1:
    if st.button("⬅ Disminuir k"):
        st.session_state.k = max(0.0, st.session_state.k - 0.1)

with col3:
    if st.button("Aumentar k ➡"):
        st.session_state.k = min(5.0, st.session_state.k + 0.1)

# Obtener valor actual de k
k = st.session_state.k

# Generar coordenadas del corazón
x = np.linspace(-2, 2, 400)
y = (x**2)**(1/3) + 0.7 * np.sin(k * x) * np.sqrt(3 - x**2)

# Graficar el corazón
fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(x, y, 'r', linewidth=2)
ax.plot(x, -y, 'r', linewidth=2)  # Reflejo para completar el corazón
ax.set_xticks([])
ax.set_yticks([])
ax.axis("equal")
ax.set_title(f"💖 k = {k:.1f}")

# Mostrar gráfico
st.pyplot(fig)

st.write(f"Valor actual de k: **{k:.1f}**")
st.write("Espero que te guste 💕")




