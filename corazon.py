streamlit
numpy
matplotlib
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configurar la página
st.set_page_config(page_title="Tu Corazón Interactivo", page_icon="❤️")

st.title("💖 Feliz día de San Valentín 💖")
st.write("Usa el control deslizante para cambiar el valor de k, que representa cómo los altos y bajos momentos nos unen para dar un resultado final.")

# Slider para modificar k con aumento de 1 en 1
k = st.slider("Ajusta el valor de k", min_value=0, max_value=260, value=0, step=1)

# Generar coordenadas del corazón
x = np.linspace(-2, 2, 400)
y = (x**2)**(1/3) + 0.7 * np.sin(k * x) * np.sqrt(3 - x**2)

# Graficar solo la parte superior del corazón
fig, ax = plt.subplots(figsize=(7, 7))  # Ajustar el tamaño de la figura

ax.plot(x, y, 'r', linewidth=2)
ax.set_xticks(np.arange(-6, 6.1, 0.5))  # Ajustar escala de los ejes X a 0.5
ax.set_yticks(np.arange(-5, 5.1, 0.5))  # Ajustar escala de los ejes Y a 0.5
ax.grid(True)  # Activar la cuadrícula

# Ajustar límites de los ejes para mejor visibilidad
ax.set_xlim([-6, 6])  # Establecer límites del eje X
ax.set_ylim([-5, 5])  # Establecer límites del eje Y

ax.axis("equal")
ax.set_title(f"💖 k = {k}")

# Mostrar la ecuación con el título "Ecuación del Amor"
equation_title = "Ecuación del Amor:"
equation = r"$y = (x^2)^{1/3} + 0.7 \cdot \sin(k \cdot x) \cdot \sqrt{3 - x^2}$"
ax.text(0, -1.8, equation_title, fontsize=14, color='black', ha='center')  # Subir título
ax.text(0, -2.0, equation, fontsize=12, color='black', ha='center')  # Subir ecuación

# Mostrar gráfico
st.pyplot(fig)

st.write(f"Valor actual de k: **{k}**")
st.write("Deja tu ego y seamos felices hoy 💖")


