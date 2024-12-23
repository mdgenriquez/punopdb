import streamlit as st
import requests

st.title("Compara dos códigos SMILES")
st.write("Ingrese dos SMILES para verificar si corresponden a la misma molécula.")

# Entradas de SMILES
smiles1 = st.text_input("Ingrese el primer SMILES:")
smiles2 = st.text_input("Ingrese el segundo SMILES:")

def fetch_canonical_smiles(smiles):
    """Usar una API para obtener el SMILES canónico."""
    api_url = f"https://cactus.nci.nih.gov/chemical/structure/{smiles}/smiles"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text.strip()
        return None
    except Exception as e:
        return None

if st.button("Comparar moléculas"):
    canonical1 = fetch_canonical_smiles(smiles1)
    canonical2 = fetch_canonical_smiles(smiles2)

    if canonical1 and canonical2:
        if canonical1 == canonical2:
            st.success("Las moléculas son equivalentes.")
        else:
            st.error("Las moléculas no son equivalentes.")
    else:
        st.error("No se pudo validar uno o ambos SMILES.")
