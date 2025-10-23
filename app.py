import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Métodos Iterativos – Boyyer & Jasson", layout="wide", page_icon="👷‍♂️")

# --- BROMITA #1: CARGA CON GLOBITOS Y MENSAJE DIVERTIDO ---
with st.spinner("🧮 Cargando inteligencia numérica avanzada..."):
    time.sleep(1.5)
st.success("✅ Carga completada con éxito (¡más rápido que Gauss–Seidel!)")
st.balloons()

st.markdown("""
> 💡 *Advertencia:* Este programa puede generar **convergencia extrema** en matemáticos desprevenidos.  
> 👷‍♂️ ¡Boyyer y Jasson, preparados para el impacto numérico! 💥
""")

# --- ESTILOS ---
st.markdown("""
<style>
.main {
    background: linear-gradient(90deg, #0a2647, #133b5c);
    color: #f1f5f9;
    font-family: 'Segoe UI';
}
h1, h2, h3 {
    color: #facc15;
    text-shadow: 1px 1px 3px black;
}
section[data-testid="stSidebar"] {
    background-color: #12273a;
    color: #f1f5f9;
}
button[kind="primary"] {
    background-color: #facc15 !important;
    color: #0a2647 !important;
    border-radius: 8px !important;
    border: none !important;
}
button[kind="primary"]:hover {
    background-color: #eab308 !important;
}
textarea, input {
    background-color: #0f1f33 !important;
    color: #e5e7eb !important;
    border: 1px solid #facc15 !important;
    border-radius: 8px !important;
}
.temario-box {
    background: linear-gradient(90deg, #0a2647 60%, #133b5c);
    border-radius: 12px;
    padding: 30px;
    color: #ffffff;
    font-family: 'Segoe UI';
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    display: flex;
    align-items: center;
    margin-bottom: 25px;
}
.temario-img {
    flex: 1;
    text-align: center;
}
.temario-img img {
    width: 100%;
    max-width: 300px;
    border-radius: 10px;
}
.temario-text {
    flex: 2;
    padding-left: 40px;
}
.temario-title {
    color: #facc15;
    font-size: 1.8rem;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 15px;
}
.temario-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
.temario-num {
    background-color: #facc15;
    color: #0a2647;
    font-weight: bold;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- CONTROL DE PÁGINAS ---
if "pagina" not in st.session_state:
    st.session_state.pagina = "temario"

def volver():
    st.session_state.pagina = "temario"

# --- PORTADA / TEMARIO ---
if st.session_state.pagina == "temario":
    st.markdown("""
    <div class="temario-box">
        <div class="temario-img">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Hard_hats_in_a_row.jpg/640px-Hard_hats_in_a_row.jpg" alt="Cascos de ingeniería">
        </div>
        <div class="temario-text">
            <div class="temario-title">Temario – Boyyer & Jasson 👷‍♂️</div>
            <div class="temario-item"><div class="temario-num">1</div><span>Norma Matricial</span></div>
            <div class="temario-item"><div class="temario-num">2</div><span>Condicionamiento</span></div>
            <div class="temario-item"><div class="temario-num">3</div><span>Convergencia y Error</span></div>
            <div class="temario-item"><div class="temario-num">4</div><span>Método de Jacobi</span></div>
            <div class="temario-item"><div class="temario-num">5</div><span>Método de Gauss–Seidel</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.title("👷‍♂️ Métodos Iterativos – Boyyer & Jasson")
    st.subheader("Aplicación Interactiva de Métodos Numéricos Iterativos")
    st.markdown("Selecciona un tema del temario para comenzar 👇")

    metodo = st.radio(
        "📘 Elige el método que deseas explorar:",
        [
            "Norma Matricial",
            "Condicionamiento",
            "Convergencia y Error",
            "Método de Jacobi",
            "Método de Gauss–Seidel"
        ]
    )

    if st.button("Ir al método seleccionado"):
        st.session_state.pagina = metodo

# --- NORMA MATRICIAL ---
elif st.session_state.pagina == "Norma Matricial":
    st.header("1️⃣ Norma Matricial")
    st.write("La norma mide el tamaño o magnitud de una matriz, útil para analizar estabilidad numérica.")
    if st.button("🏠 Volver al Temario"):
        volver()

    A_text = st.text_area("🔢 Matriz A", "1,2,3; 4,5,6; 7,8,9")
    if st.button("Calcular Normas"):
        try:
            A = np.array([[float(x) for x in row.split(',')] for row in A_text.split(';')])
            n1, ninf, nf = np.linalg.norm(A, 1), np.linalg.norm(A, np.inf), np.linalg.norm(A, 'fro')
            st.success(f"Norma 1 = {n1:.4f}")
            st.success(f"Norma ∞ = {ninf:.4f}")
            st.success(f"Norma Frobenius = {nf:.4f}")
            fig, ax = plt.subplots()
            ax.bar(['Norma 1', 'Norma ∞', 'Frobenius'], [n1, ninf, nf], color=['#facc15','#fde047','#fef9c3'])
            ax.set_title("Comparación de Normas")
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error: {e}")

# --- CONDICIONAMIENTO ---
elif st.session_state.pagina == "Condicionamiento":
    st.header("2️⃣ Condicionamiento")
    st.write("Evalúa la sensibilidad del sistema Ax = b ante perturbaciones.")
    if st.button("🏠 Volver al Temario"):
        volver()

    A_text = st.text_area("🔢 Matriz A", "2,1; 1,3")
    if st.button("Calcular Condicionamiento"):
        try:
            A = np.array([[float(x) for x in row.split(',')] for row in A_text.split(';')])
            cond = np.linalg.cond(A)
            st.success(f"Número de condición: {cond:.4f}")
            if cond < 10:
                st.info("✅ Bien condicionado")
            elif cond < 1000:
                st.warning("⚠️ Medianamente condicionado")
            else:
                st.error("❌ Muy mal condicionado")
        except Exception as e:
            st.error(f"Error: {e}")

# --- CONVERGENCIA Y ERROR ---
elif st.session_state.pagina == "Convergencia y Error":
    st.header("3️⃣ Convergencia y Error")
    st.latex(r"e_{rel} = \frac{|x_{k+1} - x_k|}{|x_{k+1}|}")
    if st.button("🏠 Volver al Temario"):
        volver()

    xk = st.number_input("xₖ (anterior)", value=2.0)
    xk1 = st.number_input("xₖ₊₁ (nuevo)", value=2.2)
    if st.button("Calcular Error Relativo"):
        e = abs(xk1 - xk) / abs(xk1)
        st.success(f"Error relativo = {e:.5f}")
        fig, ax = plt.subplots()
        ax.bar(["Error"], [e], color="#facc15")
        ax.set_ylim(0, 1)
        ax.set_ylabel("Magnitud del Error")
        st.pyplot(fig)

# --- JACOBI ---
elif st.session_state.pagina == "Método de Jacobi":
    st.header("4️⃣ Método de Jacobi")
    st.latex(r"x_i^{(k+1)} = \frac{1}{a_{ii}}(b_i - \sum_{j \neq i} a_{ij}x_j^{(k)})")
    if st.button("🏠 Volver al Temario"):
        volver()

    A_text = st.text_area("🔢 Matriz A", "10,-1,2,0; -1,11,-1,3; 2,-1,10,-1; 0,3,-1,8")
    b_text = st.text_input("🎯 Vector b", "6,25,-11,15")
    x0_text = st.text_input("🔰 x inicial", "0,0,0,0")
    it = st.number_input("Iteraciones", 1, 50, 5)
    if st.button("Ejecutar Jacobi"):
        try:
            A = np.array([[float(x) for x in row.split(',')] for row in A_text.split(';')])
            b = np.array([float(x) for x in b_text.split(',')])
            x = np.array([float(x) for x in x0_text.split(',')])
            D = np.diag(np.diag(A))
            R = A - D
            hist = []
            for _ in range(it):
                x = np.linalg.inv(D) @ (b - R @ x)
                hist.append(x.copy())
            st.success(f"Solución aproximada: x = {x.round(4)}")
            hist = np.array(hist)
            fig, ax = plt.subplots()
            for i in range(hist.shape[1]):
                ax.plot(hist[:, i], label=f"x{i+1}")
            ax.set_title("Convergencia de Jacobi")
            ax.legend()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error: {e}")

# --- GAUSS-SEIDEL ---
elif st.session_state.pagina == "Método de Gauss–Seidel":
    st.header("5️⃣ Método de Gauss–Seidel")
    st.latex(r"x_i^{(k+1)} = \frac{1}{a_{ii}}(b_i - \sum_{j<i} a_{ij}x_j^{(k+1)} - \sum_{j>i} a_{ij}x_j^{(k)})")
    if st.button("🏠 Volver al Temario"):
        volver()

    A_text = st.text_area("🔢 Matriz A", "10,-1,2,0; -1,11,-1,3; 2,-1,10,-1; 0,3,-1,8")
    b_text = st.text_input("🎯 Vector b", "6,25,-11,15")
    x0_text = st.text_input("🔰 x inicial", "0,0,0,0")
    it = st.number_input("Iteraciones", 1, 50, 5)
    if st.button("Ejecutar Gauss–Seidel"):
        try:
            A = np.array([[float(x) for x in row.split(',')] for row in A_text.split(';')])
            b = np.array([float(x) for x in b_text.split(',')])
            x = np.array([float(x) for x in x0_text.split(',')])
            n = len(b)
            hist = []
            for _ in range(it):
                for i in range(n):
                    x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
                hist.append(x.copy())
            st.success(f"Solución aproximada: x = {x.round(4)}")
            hist = np.array(hist)
            fig, ax = plt.subplots()
            for i in range(hist.shape[1]):
                ax.plot(hist[:, i], label=f"x{i+1}")
            ax.set_title("Convergencia de Gauss–Seidel")
            ax.legend()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error: {e}")

# --- PIE DE PÁGINA + BROMITA #3 ---
st.markdown("""
---
### 👨‍🏫 Proyecto desarrollado por:
**Boyyer & Jasson**  
_Curso: Métodos Numéricos – Ingeniería de Sistemas_  
💛 Universidad Peruana Unión – 2025  

> 🤖 *Inteligencia Numérica cortesía de: ChatGPT + Boyyer & Jasson Neural Systems™ 2025* 🚀
""")
