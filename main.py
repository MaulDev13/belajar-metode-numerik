import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

# Title
st.title("⚖️ BMI Calculator")
st.write("Hitung Body Mass Index (BMI) dengan mudah")

# Input user
berat = st.number_input(
    "Masukkan berat badan (kg)",
    min_value=1.0,
    max_value=300.0,
    step=0.1
)

tinggi = st.number_input(
    "Masukkan tinggi badan (cm)",
    min_value=50.0,
    max_value=250.0,
    step=0.1
)

# Tombol hitung
if st.button("Hitung BMI"):

    tinggi_meter = tinggi / 100
    bmi = berat / (tinggi_meter ** 2)

    st.subheader(f"Hasil BMI: {bmi:.2f}")

    # Kategori BMI
    if bmi < 18.5:
        kategori = "Kurus"
        warna = "blue"

    elif bmi < 25:
        kategori = "Normal"
        warna = "green"

    elif bmi < 30:
        kategori = "Kelebihan Berat Badan"
        warna = "orange"

    else:
        kategori = "Obesitas"
        warna = "red"

    st.markdown(
        f"""
        <h3 style='color:{warna};'>
        Kategori: {kategori}
        </h3>
        """,
        unsafe_allow_html=True
    )

    # Progress BMI
    progress = min(int(bmi * 2), 100)
    st.progress(progress)

# Footer
st.markdown("---")
st.caption("Dibuat dengan Python & Streamlit")