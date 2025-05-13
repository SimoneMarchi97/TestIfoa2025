import streamlit as st

def main ():
    st.title("La bottega del gusto")

    st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #FFFFFF;                       /* Opzionale: imposta il colore del testo per contrasto */
    }
    .stApp {
        background-color: #000000;            /* Assicura che anche l'area principale sia nera */
    }
    </style>
    """,
    unsafe_allow_html=True,) 

    st.title("La mia app con sfondo nero")
    st.write("Questo testo dovrebbe essere bianco su sfondo nero.")





    st.balloons()
    st.snow()

if __name__ == "__main__":
    main()
