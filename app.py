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
    
    <p>Je suis <strong>Julien Castellano</strong>, un <strong>Data Analyst Junior</strong> passionné par l'analyse de données et la résolution de problématiques grâce à l'intelligence des données . Après une carrière de 8 ans dans les télécoms , j'ai décidé de me réorienter vers l'analyse de données, un domaine qui me permet de combiner ma rigueur analytique et mon enthousiasme pour la prise de décision éclairée.</p>
    
    <p>Actuellement en formation à la <strong>Wild Code School</strong> , je développe mes compétences pour obtenir une licence en <strong>Data Analytics</strong>. Mon objectif est d'utiliser les données pour apporter des solutions concrètes et pertinentes aux entreprises.</p>
    
    <p><strong>Mes compétences :</strong></p>
    <ul style='text-align: left; margin-left: 20%;'>
        <li><strong>SQL 🗄️ :</strong> Gestion de bases de données et interrogations pour extraire des insights.</li>
        <li><strong>Python 🐍 :</strong> Programmation pour l'analyse et la manipulation des données.</li>
        <li><strong>Power BI & Tableau 📊 :</strong> Création de visualisations interactives pour des prises de décision éclairées.</li>
        <li><strong>Nettoyage et préparation des données 🧹 :</strong> Transformation des données brutes en informations exploitables.</li>
        <li><strong>Analyse statistique 📈 :</strong> Extraction de tendances et analyses prédictives pour guider la stratégie.</li>
    </ul>

    <p><strong>Ce que vous trouverez sur ce portfolio :</strong></p>
    <ul style='text-align: left; margin-left: 20%;'>
        <li><strong>Projets à la Wild Code School 🎓 :</strong> Divers projets analytiques, dont la création de dashboards interactifs avec Power BI, l'analyse de données à l'aide de Python, et la mise en œuvre de solutions de nettoyage et de préparation des données pour des cas réels.</li>
        <li><strong>Projets personnels 💡 :</strong> Développement de projets pour approfondir mes compétences, tels que la visualisation des données, la manipulation de grands jeux de données, et l'application de modèles prédictifs avec Python pour des problématiques réelles.</li>
    </ul>

    <p>Si vous êtes à la recherche d'un <strong>Data Analyst Junior</strong> déterminé à apporter une réelle valeur ajoutée à votre entreprise, je vous invite à explorer mon portfolio et à me contacter pour échanger sur les opportunités à venir 📩.</p>
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
    # En cours
    afficher_climbing()

