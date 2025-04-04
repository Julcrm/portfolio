import streamlit as st
from wcs.projet_1.wcs_projet1 import afficher_wcs_projet1
from wcs.projet_2.wcs_projet2 import afficher_wcs_projet2
from wcs.projet_3.wcs_projet3 import afficher_wcs_projet3
from perso.climbing.climbing import afficher_climbing



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

# Modification de la taille de la sidebar et réduction de l'espace entre les colonnes
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            display: inline-block;
            width: 360px !important; # Set the width to your desired value
        }
        .stColumn {
            gap: 1px;  /* Réduit l'espace entre les colonnes */
        }
        .stButton>button {
            margin-right: 1px;  /* Réduit l'espace entre les boutons */
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# Menu de navigation dans la sidebar
with st.sidebar:
    # Créer des colonnes pour "Accueil" et "Popover"
    col1, col2 = st.columns([1, 1])  # Deux colonnes avec une taille égale

    with col1:
        if st.button("Accueil 🏠"):
            set_page("Accueil")

    with col2:
        with st.popover("Contact 📩", use_container_width = True):
            st.link_button("Linkedin 🔗", "https://www.linkedin.com/in/julien-castellano")
            st.link_button("Mail 📬", "mailto:julien.crm@gmail.com")

    # Les autres éléments (boutons et textes) restent en affichage vertical
    st.markdown("""
    ### Projets réalisés à la Wild Code School <img src='https://help.wildcodeschool.com/hubfs/markentive/favicons/global/android-chrome-256x256.png' width='25' height='25'>""", 
    unsafe_allow_html=True)
    if st.button("Toys & Models 📊"):
        set_page("wcs_projet1")
    if st.button("Recommandation Films 🍿"):
        set_page("wcs_projet2")
    if st.button("Projet 3 - En cours 🚧"):
        set_page("wcs_projet3")
    st.markdown("""
    ### Projets personnels  <img src='https://cdn-icons-png.flaticon.com/512/6140/6140802.png' width='25' height='25'>""", 
    unsafe_allow_html=True)
    if st.button("Climbing - En cours 🧗"):
        set_page("climbing")



# Affichage page d'accueil
if st.session_state.page == "Accueil":
    # Page d'accueil
    st.markdown("<h1 style='text-align: center; color: white;'>Bienvenue sur mon portfolio ! 🗂️</h1>", unsafe_allow_html=True)

    st.markdown("""
            <div style='text-align: center; color: white; font-size: 20px;'>

            <p>Je suis <strong>Julien Castellano</strong>, un <strong>Data Analyst Junior</strong> passionné par la donnée et son potentiel. Après une carrière de 8 ans dans les télécoms, j’ai fait le choix de me reconvertir dans la <strong>Data</strong> et l’<strong>Intelligence Artificielle</strong>.</p>

            <p>Récemment diplômé d’une <strong>licence en Data Analytics</strong> à la <strong>Wild Code School</strong>, je poursuis désormais mon évolution en me spécialisant en <strong>Data Engineering</strong>, avec l’ambition d’intégrer un <strong>Master en Data & IA</strong>. Mon objectif est de concevoir et optimiser des architectures de données afin de rendre les infrastructures plus performantes et scalables.</p>

            <p><strong>Mes compétences :</strong></p>
            <ul style='text-align: left; margin-left: 20%;'>
                <li><strong>SQL 🗄️ :</strong> Optimisation et gestion de bases de données relationnelles.</li>
                <li><strong>Python 🐍 :</strong> Manipulation de données, automatisation et développement d’algorithmes.</li>
                <li><strong>Power BI & Tableau 📊 :</strong> Création de dashboards interactifs pour des analyses stratégiques.</li>
                <li><strong>ETL & Data Pipelines 🔄 :</strong> Conception et automatisation des flux de données.</li>
            </ul>

            <p><strong>Ce que vous trouverez sur ce portfolio :</strong></p>
            <ul style='text-align: left; margin-left: 20%;'>
                <li><strong>Projets réalisés 🚀 :</strong> Analyses de données, création de dashboards interactifs, développement d’automatisations et mise en place de workflows d’ingestion et transformation de données.</li>
                <li><strong>Projets personnels 💡 :</strong> Développement de projets pour approfondir mes compétences, tels que la visualisation des données, la manipulation de grands jeux de données, et l'application de modèles prédictifs avec Python pour des problématiques réelles.</li>
            </ul>

            <p>Si vous recherchez un profil passionné et motivé dans l’univers de la <strong>Data & IA</strong>, je vous invite à explorer mon portfolio et à me contacter pour échanger sur de futures opportunités 📩.</p>

            </div>
            """, unsafe_allow_html=True)


elif st.session_state.page == "wcs_projet1":
    # Toys & Models
    afficher_wcs_projet1()

elif st.session_state.page == "wcs_projet2":
    # Recommandation de films
    afficher_wcs_projet2()

elif st.session_state.page == "wcs_projet3":
    # En cours
    afficher_wcs_projet3()

elif st.session_state.page == "climbing":
    # Climlbing
    afficher_climbing()


