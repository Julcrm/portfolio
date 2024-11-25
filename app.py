import streamlit as st
from wcs.projet_1.projet1 import afficher_wcs_projet1
from wcs.projet_2.projet2 import afficher_wcs_projet2

# Configuration de la page
st.set_page_config(
    page_title="Portfolio - Julien Castellano",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialisation de la variable pour suivre la page active
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

# Définir une fonction pour changer la page active
def set_page(page_name):
    st.session_state.page = page_name

# Modification de la taille de la sidebar
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 360px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Menu de navigation dans la sidebar
with st.sidebar:
    if st.button("Accueil 🏠"):
        set_page("Accueil")
    st.markdown("""
    ### Projets réalisés à la Wild Code School <img src='https://help.wildcodeschool.com/hubfs/markentive/favicons/global/android-chrome-256x256.png' width='25' height='25'>""", 
    unsafe_allow_html=True)
    if st.button("Projet 1 - SQL/Power BI 📊"):
        set_page("wcs_projet1")
    if st.button("Projet 2 - Python/Pandas/Seaborn 🐍"):
        set_page("wcs_projet2")
    st.markdown("""
    ### Projets personnels  <img src='https://cdn-icons-png.flaticon.com/512/6140/6140802.png' width='25' height='25'>""", 
    unsafe_allow_html=True)

# Affichage page d'accueil
if st.session_state.page == "Accueil":
    # Page d'accueil
    st.markdown("<h1 style='text-align: center; color: white;'>Bienvenue sur mon portfolio ! 🗂️</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; color: white; font-size: 20px;'>
    Passionné par l'analyse de données 📊, je suis un Data Analyst en reconversion, avec une formation solide et une réelle envie de résoudre des problématiques complexes grâce à la donnée.

Au cours de mon parcours à la Wild Code School 🎓, j'ai acquis des compétences techniques en gestion, nettoyage, analyse et visualisation des données. J'ai eu l'occasion de travailler avec des outils comme Python 🐍, SQL et Power BI pour transformer des données brutes en informations utiles, et créer des rapports interactifs pour aider à la prise de décision stratégique 📈.

Dans ce portfolio, vous trouverez une sélection de projets qui montrent ma capacité à analyser des datasets complexes, en extraire des insights pertinents 💡, et créer des visualisations claires pour mieux comprendre les tendances et les performances. Chaque projet reflète mon aptitude à utiliser des outils modernes et à appliquer des méthodologies solides pour résoudre des problèmes réels 🔧.

Je suis actuellement à la recherche de nouvelles opportunités dans la Data Analytics 🌟 et serais ravi d’échanger sur des projets intéressants.

N’hésitez pas à explorer mes projets et à me contacter si vous avez des questions ou souhaitez collaborer 🤝.

    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "wcs_projet1":
    # SQL/Power BI
    afficher_wcs_projet1()

elif st.session_state.page == "wcs_projet2":
    # Python/Pandas/Seaborn
    afficher_wcs_projet2()
