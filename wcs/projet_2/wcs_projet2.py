import streamlit as st
from wcs.projet_2.reco import afficher_reco
from wcs.projet_2.viz import afficher_viz

def afficher_wcs_projet2():
    # Initialisation de la variable pour suivre la page active
    if "page_projet2" not in st.session_state:
        st.session_state.page_projet2 = "accueil"  # Par défaut, la page d'accueil du projet 2 est affichée

    # Définition d'une fonction pour changer la page active
    def set_page(page_name):
        st.session_state.page_projet2 = page_name  # Modification de la variable pour changer de page

    # Configuration de la barre de navigation avec plusieurs colonnes
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])  # Distribution des colonnes
    with col2:
        if st.button("Accueil", use_container_width=True):  # Bouton Accueil
            set_page("accueil")  # Change la page en 'accueil' lorsque ce bouton est pressé
    with col3:
        if st.button("Visualisations", use_container_width=True):  # Bouton Visualisations
            set_page("viz")  # Change la page en 'viz' lorsque ce bouton est pressé
    with col4:
        if st.button("Recommandation", use_container_width=True):  # Bouton Recommandation
            set_page("reco")  # Change la page en 'reco' lorsque ce bouton est pressé

    # Ajout d'un espacement entre la navigation et le contenu de la page
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    # Affichage de la page correspondant à la variable `st.session_state.page_projet2`
    if st.session_state.page_projet2 == "accueil":

        # Titre + explication du projet
        st.markdown("<h1 style='text-align: center; color: white;'>Projet 2 : Analyse de données et Machine Learning dans le Cinéma</h1>", unsafe_allow_html=True)

        #Espace
        st.write("")
        st.write("")


        # Disposition de l'image du logo (centrée sur la page)
        col1, col2, col3 = st.columns([3, 2, 3])  # Création de trois colonnes de largeur relative (col2 sera au centre)
        with col2:  # Affichage de l'image dans la colonne du centre
            st.image("wcs/projet_2/logo_sans_fond.png", width=150)  # L'image est redimensionnée à 10% de sa largeur d'origine

        #Espace
        st.write("")
        st.write("")


        st.markdown("""
        <div style='text-align: center; color: white; font-size: 20px;'>
        Dans ce projet, j'ai travaillé sur l'analyse du marché du cinéma et le développement d'un moteur de recommandation basé sur le Machine Learning.  
        L'objectif était d'aider un cinéma local à mieux comprendre son public et à proposer des films adaptés à ses préférences.<br><br>
        Vous pouvez naviguer dans avec les onglets visualisation et recommandation,<br>
        (un petit temps de chargement est nécessaire pour charger les données hébergées sur mon drive).
        </div>
        """, unsafe_allow_html=True)

        #Espace
        st.write("")
        st.write("")


        # Étapes du projet
        st.markdown("""
        ## 🔍 Étapes réalisées :
        """)

        #Espace
        st.write("")
        st.write("")

        st.markdown("""
        ### 1️⃣ Analyse des données avec Pandas 📊 :
        - Récupération des données depuis TMDB et IMDB.
        - Exploration et traitement des données relatives aux films, genres, réalisateurs et audiences.
        - Identification des tendances clés du marché du cinéma (genres populaires, réalisateurs appréciés, etc.).
        """)

        # URL vers le notebook traitement hébergé
        traitement = "https://nbviewer.org/github/Julcrm/Recommandation_films/blob/9ee7c720c705630ecd7b3f5b8579a500a9909682/traitements.ipynb"

        #Espace
        st.write("")

        # Affichage avec iframe
        with st.expander("Cliquez ici pour afficher le notebook traitement et nettoyage des données"):
            st.markdown(f'<iframe src="{traitement}" width="100%" height="800px"></iframe>', unsafe_allow_html=True)

        #Espace
        st.write("")
        st.write("")

        st.markdown("""
        ### 2️⃣ Création d’un moteur de recommandation avec Scikit-Learn 🧠 :
        - Mise en place d'un pipeline pour gérer les données numériques et catégorielles.
        - Mise en place d’un algorithme de recommandation basé sur le modèle NearestNeighbors.
        - Attribution de poids aux différentes catégories.
        - Optimisation et validation des performances du modèle.
        """)
        
        # URL vers le notebook machine learning hébergé
        machine_learning= "https://nbviewer.org/github/Julcrm/Recommandation_films/blob/9ee7c720c705630ecd7b3f5b8579a500a9909682/reco.ipynb"

        #Espace
        st.write("")

        # Affichage avec iframe
        with st.expander("Cliquez ici pour afficher le notebook machine learning"):
            st.markdown(f'<iframe src="{machine_learning}" width="100%" height="800px"></iframe>', unsafe_allow_html=True)

        #Espace
        st.write("")
        st.write("")

        st.markdown("""
        ### 3️⃣ Développement d’un outil interactif avec Streamlit 🌐 :
        - Présentation des résultats de l’analyse du marché sous forme de graphiques.
        - Intégration du moteur de recommandation dans une application Streamlit pour une utilisation facile et intuitive.
        - Intégration d'une interface de recommandation avec l'API de l'IA Gemini.
        
        """)

        #Espace
        st.write("")
        st.write("")

        # Résultat
        st.markdown("""
        ## 💡 Résultat :
        Un outil puissant et intuitif, offrant :
        - Un tableau de bord pour explorer les tendances du marché du cinéma.
        - Un moteur de recommandation selon le film choisi ou une interface de recommandation selon la demande. 
        """)

        #Espace
        st.write("")

        st.markdown("""
        Ce projet a permis de démontrer la puissance des données et du Machine Learning dans un domaine créatif comme le cinéma.
        """)


    elif st.session_state.page_projet2 == "viz":
        # Page de visualisation : Appel de la fonction pour afficher les visualisations
        afficher_viz()

    elif st.session_state.page_projet2 == "reco":
        # Page de recommandations : Appel de la fonction pour afficher les recommandations
        afficher_reco()


