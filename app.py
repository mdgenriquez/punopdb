import streamlit as st
from chemtools.utils import is_isomorphic

st.title("Compara dos códigos SMILES")
st.write("Ingrese dos SMILES para verificar si corresponden a la misma molécula.")

# Entrada de SMILES
smiles1 = st.text_input("Ingrese el primer SMILES:", "")
smiles2 = st.text_input("Ingrese el segundo SMILES:", "")

if st.button("Comparar moléculas"):
    try:
        # Comprobar equivalencia con ChemTools
        equivalence = is_isomorphic(smiles1, smiles2)

        if equivalence:
            st.success("Las moléculas son equivalentes.")
        else:
            st.error("Las moléculas no son equivalentes.")
    except Exception as e:
        st.error(f"Error al comparar los SMILES: {e}")
