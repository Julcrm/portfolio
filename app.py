import streamlit as st
from wcs_projet1 import afficher_wcs_projet1
from wcs_projet2 import afficher_wcs_projet2

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
    Passionné par l'analyse de données 📊, je suis un Data Analyst en reconversion professionnelle 🚀, avec une formation solide et une véritable envie de résoudre des problématiques complexes à l'aide de la donnée.

Au fil de mon parcours à la Wild Code School 🎓, j'ai acquis des compétences techniques en gestion, nettoyage, analyse et visualisation des données 🔍. Grâce à des outils comme Python, SQL et Power BI, j'ai appris à transformer des données brutes en informations exploitables 💡 et à créer des rapports interactifs pour prendre des décisions stratégiques 📈.

Dans ce portfolio, vous trouverez une sélection de projets qui démontrent ma capacité à analyser des datasets complexes 📉, à en extraire des insights pertinents 💬 et à créer des visualisations qui facilitent la compréhension des tendances et des performances 📊. Chaque projet reflète ma capacité à utiliser des outils modernes et à appliquer des méthodologies robustes pour résoudre des problèmes réels 🔧.

Je suis actuellement à la recherche de nouvelles opportunités dans le domaine de la Data Analytics 🌟, où je pourrai continuer à développer mes compétences et contribuer à des projets stimulants ⚡.

N'hésitez pas à explorer mes projets et à me contacter pour toute question ou collaboration 🤝! 
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "wcs_projet1":
    # SQL/Power BI
    afficher_wcs_projet1()

elif st.session_state.page == "wcs_projet2":
    # Python/Pandas/Seaborn
    afficher_wcs_projet2()
