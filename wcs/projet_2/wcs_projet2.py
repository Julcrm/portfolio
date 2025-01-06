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
        """)

        #Espace
        st.write("")

        with st.expander("Cliquez ici pour afficher le code de la page visualisations"):
            st.code('''# ID du fichier Google Drive
    df_top_pays_id = '13ZGjbFR2_qjOic_hzU4JQvkMvuJ2pfB4'
    df_time_id = '1npUK9DA-EZEbueW8RT-WZIPhlEuxtC7P'
    df_pop_note_id = '1E-jCLT4Ez5X9suxB-AOY597QDpHoR4SP'
    df_real_id = '1qHDuLSY8ZZ-JOTK1jOMgNahVSqjm_JT3'

    # Lien téléchargeable
    url = "https://drive.google.com/uc?id="

    cache = Cache("/data")

    if "df_top_pays" not in cache:
        cache["df_top_pays"] = pd.read_parquet(url + df_top_pays_id)
    df_top_pays = cache["df_top_pays"]
    
    if "df_time" not in cache:
        cache["df_time"] = pd.read_parquet(url + df_time_id)
    df_time = cache["df_time"]

    if "df_pop_note" not in cache:
        cache["df_pop_note"] = pd.read_csv(url + df_pop_note_id)
    df_pop_note = cache["df_pop_note"]

    if "df_real" not in cache:
        cache["df_real"] = pd.read_csv(url + df_real_id)
    df_real = cache["df_real"]


    # Disposition des colonnes pour l'affichage avec Streamlit
    col1, col2 = st.columns([1, 1])

    # Début de la colonne 1
    with col1:
        # Graphique des pays : Top 15 des pays producteurs de films
        pays_chart = px.bar(
            df_top_pays,
            x="pays",
            y="score",
            labels={"pays": "Pays", "score": "Score"}
        )
        pays_chart.update_layout(title_text='Top 15 des pays producteurs de films', title_x=0.4)
        pays_chart.update_traces(marker_color="#9B1B30")
        st.plotly_chart(pays_chart)

        # Explication du graphique des pays
        with st.expander("Explications"):
            st.write("""
                    **(1)**  

                    Ce graphique en barres met en avant le **top 15 des pays producteurs de films**, grâce à un score combinant :  
                    - Le **nombre moyen de films produits par pays**.  
                    - Leur **popularité à l’échelle mondiale**.  
                    """)

        # Graphique Popularité vs Note : Relation entre la note des films et leur popularité
        pop_chart = px.bar(
            df_pop_note,
            x="groupes",
            y="popularity",
            labels={"popularity": "Popularité", "groupes": "Note"}
        )
        pop_chart.update_layout(title_text='Popularité en fonction de la note', title_x=0.4)
        pop_chart.update_traces(marker_color="#9B1B30")
        st.plotly_chart(pop_chart)

        # Explication du graphique Popularité vs Note
        with st.expander("Explications"):
            st.write("""
                    **(3)**  

                    Le graphique en barres montre la relation entre la note des films (sur une échelle de 1 à 10) et leur popularité (sur une échelle de 0 à 5).  

                    On remarque que :  
                    - Les films notés **1/10** sont en réalité plus populaires que ceux notés **10/10**.  
                    - Les films ayant des notes comprises entre **2/10 et 9/10** affichent des scores de popularité similaires.  

                    Par conséquent, j'ai choisi de **ne pas appliquer de filtre** basé sur la note ou la popularité, car ces critères ne semblent pas avoir un impact déterminant sur la popularité d'un film.  
                    """)

        # Graphique des réalisateurs : Nombre de films réalisés par les cinéastes
        nb_films = df_real["Real"].value_counts()
        nb_real = nb_films.value_counts().sort_index()
        x = nb_real.index
        y = nb_real.values  
        real_chart = px.bar(x=x, 
                            y=y, 
                            labels={'x': 'Nombre de films réalisés', 'y': 'Nombre de réalisateurs'}
                            )
        real_chart.update_layout(title_text='Nombre de films réalisés par les cinéastes', title_x=0.3)
        real_chart.update_xaxes(range=[0, 10])
        real_chart.update_traces(marker_color="#9B1B30")
        st.plotly_chart(real_chart)

        # Explication du graphique des réalisateurs
        with st.expander("Explications"):
            st.write("""
                    **(5)**  

                    Le graphique en barres montre la distribution du **nombre de films réalisés par les cinéastes** :  
                    - Environ **25 000 réalisateurs** n’ont réalisé qu’un seul film.  
                    - **6 000 réalisateurs** en ont réalisé deux.  
                    - Moins de **2 500 réalisateurs** en ont réalisé trois ou plus.  

                    Nous n’avons appliqué **aucun filtre concernant les réalisateurs**.  
                    Cependant, malgré le nombre important de réalisateurs avec une filmographie limitée, j'ai choisi d’accorder un **poids significatif à ce critère dans l'algorithme**.  
                    """)

    # Début de la colonne 2
    with col2:
        # Graphique du Bilan annuel CNC : Répartition des entrées par nationalité de film
        labels = 'Français', 'Américains', 'Européens', 'Autres'
        sizes = [70.6, 74.1, 22.9, 8.8]

        cnc_chart = px.pie(
                           values=sizes,
                           names=labels, 
                           color_discrete_sequence=px.colors.sequential.RdBu)
        cnc_chart.update_layout(title_text='Bilan annuel CNC', title_x=0.4)
        st.plotly_chart(cnc_chart)

        # Explication du graphique CNC
        with st.expander("Explications"):
            st.write("""
                    **(2)** 

                    Basé sur le bilan annuel du **CNC de 2023**, ce graphique en secteurs montre la répartition des **entrées en salle** pour chaque nationalité de film.  
                    Un nombre élevé d'entrées reflète généralement l’attractivité d’un film auprès du public français, influencée par sa popularité.  

                    Afin de concevoir un système de recommandation le plus équilibré possible, j'ai choisi :  
                    - **D’intégrer les films produits par les pays du top 15 (1)**.  
                    - Tout en incluant également les **films européens qui n’y figurent pas**.  
                    """)

        # Graphique de l'évolution de la durée des films au fil du temps
        time_chart = px.line(df_time, 
                             x="année", 
                             y="temps_minutes",
                             labels={"année": "Année", "temps_minutes": "Durée en minutes"}
                             )
        time_chart.update_traces(line_color="#922E44",
                                 line=dict(width=4))
        time_chart.update_layout(
        xaxis=dict(range=[1900, 2029]),
        yaxis=dict(range=[0, 125]),
        )
        time_chart.update_layout(title_text='Évolution de la durée des films au cours des années', title_x=0.3)
        st.plotly_chart(time_chart)

        # Explication du graphique de la durée des films
        with st.expander("Explications"):
            st.write("""
                    **(4)**  

                    Ce graphique met en évidence que la **durée des films** n’a pas connu de changements majeurs au fil du temps.  
                    En conséquence, j'ai choisi de **ne pas appliquer de filtre** sur la durée des films dans le système de recommandation.  
                    """)
    # Ajout de style personnalisé à la page via Markdown
    st.markdown("""
        <style>
        /* Ajuste les balises Markdown générées si elles ne sont pas automatiquement dans des balises <p> */
        body div[role="document"] {
            font-size: 18px;
            line-height: 1.5;
        }
        </style>
        """, unsafe_allow_html=True)

    # Disposition des colonnes pour l'affichage de la conclusion et des critères de pondération
    col3, col4, col5 = st.columns([1, 2, 1])

    # Colonne 3 : vide
    with col3:
        st.write("")

    # Colonne 4 : Contenu de la conclusion
    with col4:
        st.markdown("""
        ### <h3 style="text-align:center;">Conclusion</h3>
        J'ai décidé de filtrer les films uniquement en fonction de **leur pays de production**, préférant affiner notre algorithme de recommandation.  
        J'assure ainsi de recommander des films ayant une **forte visibilité** et en lien avec les attentes culturelles des utilisateurs, tout en maintenant de la **diversité** grâce à l’inclusion des films européens qui n’apparaissent pas dans le top 15 mondial.  

        J'ai ajusté soigneusement la **pondération** en fonction de l’importance de chaque critère.
        """, unsafe_allow_html=True)

    # Colonne 5 : vide
    with col5:
        st.write("")

    # Disposition des colonnes pour l'affichage des critères spécifiques
    col6, col7, col8 = st.columns([1, 2, 1])

    # Colonne 6 : Genre et année de parution
    with col6:
        # Affichage du poids du genre
        st.markdown("""
        #### <h4 style="text-align:center;">**Genre**</h4>  
        Le genre a reçu un poids élevé basé sur le rapport du CNC, où j'ai constaté que les Français consommaient beaucoup de comédies, drames, films d’aventure et d’animation.  
        """, unsafe_allow_html=True)
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer

        # Affichage de la pondération de l'année de parution
        st.markdown("""
        #### <h4 style="text-align:center;">**Poids de l’année de parution**</h4>  
        L’année de parution n’a été ni minorée ni majorée.
        """, unsafe_allow_html=True)

    # Colonne 7 : Réalisateur et note
    with col7:
        # Affichage du poids du réalisateur
        st.markdown("""
        #### <h4 style="text-align:center;">**Réalisateur**</h4>  
        Le réalisateur a bénéficié d’un poids élevé, bien que la plupart n’aient réalisé qu’un seul film (5). J'ai équilibré cette pondération en tenant compte d’autres critères (année de parution, genre, popularité…) pour garantir une recommandation diverse et pertinente.  
        Cela met en lumière des réalisateurs ayant une vision artistique particulière tout en offrant une expérience adaptée aux goûts des utilisateurs.  
        """, unsafe_allow_html=True)

        # Affichage du poids de la note
        st.markdown("""
        #### <h4 style="text-align:center;">**Note**</h4>  
        La note a obtenu un poids légèrement inférieur. Bien que la popularité et la note ne soient pas toujours corrélées, j'ai préservé cet indicateur pour inclure des films d’art et d’essai moins populaires tout en maintenant la diversité des propositions (3). 
        """, unsafe_allow_html=True)

    # Colonne 8 : Nombre de votes et durée
    with col8:
        # Affichage du poids du nombre de votes
        st.markdown("""
        #### <h4 style="text-align:center;">**Nombre de votes**</h4>  
        Le nombre de votes a été légèrement minoré, car il peut être influencé par des facteurs externes tels que la visibilité ou des campagnes de promotion, ce qui ne reflète pas toujours la qualité globale.  
        """, unsafe_allow_html=True)
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer

        # Affichage de la pondération de la durée
        st.markdown("""
        #### <h4 style="text-align:center;">**Durée**</h4>  
        La durée a reçu une pondération négative faible, car elle présente peu de variation au fil du temps et semble peu significative sur les préférences des utilisateurs (4).  
        """, unsafe_allow_html=True)
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer
        st.write("")  # Espace vide pour aérer

    # Disposition des colonnes pour le résumé
    col9, col10, col11 = st.columns([1, 2, 1])

    # Colonne 10 : Résumé de la recommandation
    with col10:
        st.markdown("""
        **En résumé** : J'ai pris en compte ces différents critères pour offrir une recommandation équilibrée et diversifiée, répondant aux goûts des utilisateurs tout en valorisant la richesse cinématographique mondiale et européenne.
        """, unsafe_allow_html=True''')
                    
        st.markdown("""
        - Intégration du moteur de recommandation dans une application Streamlit pour une utilisation facile et intuitive.
        - Intégration d'une interface de recommandation avec l'API de l'IA Gemini.
        """)

        #Espace
        st.write("")

        with st.expander("Cliquez ici pour afficher le code de la page recommandation"):
            st.code(''' # ID du fichier Google Drive
    df_poster_id = '1AvzyoeBvwpNQlssF71PG8Ikr6QlpNSYV'
    df_reco_id = '1nHKijrPb-e_r8-5CSXFbiso44lIovARD'
    df_gemini_id = '1eVlcDdtSJen9IEo_MvIvKz3McBQQ1Ns_'

    # Lien téléchargeable
    url = "https://drive.google.com/uc?id="

    cache = Cache("/data")

    if "df_poster" not in cache:
        cache["df_poster"] = pd.read_parquet(url + df_poster_id)
    df_poster = cache["df_poster"]
    
    if "df_reco" not in cache:
        cache["df_reco"] = pd.read_parquet(url + df_reco_id)
    df_reco = cache["df_reco"]

    if "df_gemini" not in cache:
        cache["df_gemini"] = pd.read_csv(url + df_gemini_id)
    df_gemini = cache["df_gemini"]


    st.markdown("""
        <style>
        /* Style pour le texte */
        p {
            text-align: center;
            font-size: 20px;
            color: white;
        }
                
        h3 {
            text-align: center; }
        iframe {
                text-align: center;
                }
        </style>""", unsafe_allow_html=True)


    st.markdown("<p>Soirée entre amis, film en solo, en couple ou en famille ?</p>", unsafe_allow_html=True)

    st.markdown("<h3> Moteur de recommandation </h3>", unsafe_allow_html=True)

    st.text("Tapez le début d’un titre qui vous plaît, choisissez parmi les suggestions, et laissez notre système dénicher 5 films qui pourraient vous divertir!" )

    st.text("Un trou de mémoire pour le titre mais vous êtes certain du nom du réalisateur ? La barre de recherche filtrera les titres pour vous.")
    col1, col2 = st.columns([1, 2])  # Centrer et définir les proportions
    with col1:
        option_real = st.selectbox(
            "filtrer par réalisateur",
            options = df_poster["Real"].unique(),
            format_func=lambda x: x if st.session_state.get("search_query", "").lower() in x.lower() else None, index=None, placeholder="Choisissez un réalisateur",
            label_visibility = "hidden"
        )

        if option_real:
            variable_options = df_poster["id"].loc[df_poster["Real"] == option_real]    
        else:
            variable_options = df_poster["id"]

    with col2:
        option = st.selectbox(
            "selection film",
            options = variable_options,
            format_func=lambda x: x if st.session_state.get("search_query", "").lower() in x.lower() else None, index=None, placeholder="Choisissez un film",
            label_visibility = "hidden"
        )
    image_url = "https://image.tmdb.org/t/p/original"

    if option:
        resultat = df_reco.loc[df_reco["id"] == option] # Source + reco
        if not resultat.empty: #S'il y a quelquechose dans la barre
            # Recherche de l'index de la source
            recherche = resultat["source"].iloc[0] #Récupère l'index du film "option"
            titre_str =  df_poster["titre"].iloc[recherche] #Renvoie l'id du film "option"
            if df_poster['poster_path'].iloc[recherche] is None: # Si pas de poster
                poster_url = "https://i.imghippo.com/files/ZOcN3975ToU.png" #Affiche le logo
            else:
                poster_url = image_url + df_poster['poster_path'].iloc[recherche] #Sinon, l'image du film

            # **Affichage du premier film (au-dessus des recommandations)**
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <h2>Film sélectionné</h2>
                    <p><strong>{titre_str}</strong></p>
                    <img src="{poster_url}" alt="Poster" style="width: 250px;">
                    <p>📅 <strong>Année :</strong> {df_poster['année'].iloc[recherche]}</p>
                    <p>🎥 <strong>Réalisateur :</strong> {df_poster['Real'].iloc[recherche]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Ajouter un séparateur et plusieurs espaces vides
            st.empty()
            st.divider()
            st.empty()
        
            
            # **Affichage des recommandations**
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <h2>Suggestions similaires</h2>
                """,
                unsafe_allow_html=True
            )
            columns = st.columns(5)  # Création des 5 colonnes
            
            # Récupération des recommandations
            recos = list(resultat[["r1", "r2", "r3", "r4", "r5"]].values)[0]
            titres = df_poster["id"].iloc[recos].tolist()
            annee = df_poster["année"].iloc[recos].tolist()
            real = df_poster["Real"].iloc[recos].tolist()
            poster = df_poster["poster_path"].iloc[recos].tolist()

            # Affichage des recommandations dans les colonnes
            for i, (titre, annee, realisateur, poster_path) in enumerate(zip(titres, annee, real, poster)):
                liste_titre_reco = titre.split("-")
                titre_no_date_reco = " ".join(liste_titre_reco[:-1])
                with columns[i % 5]:  # Répartir les films sur 5 colonnes
                    st.markdown(f"{titre_no_date_reco}", unsafe_allow_html=True )
                    if poster_path is None :
                        st.image("wcs/projet_2/logo_sans_fond.png", width=150)
                        st.text(f"📅 Année : {annee}")
                        st.text(f"🎥 Réalisateur : {realisateur}")
                    else:
                        st.image(f"{image_url}{poster_path}", width=150)
                        st.text(f"📅 Année : {annee}")
                        st.text(f"🎥 Réalisateur : {realisateur}")
                    
        else:
            st.warning("Aucun résultat trouvé pour cette sélection.")

    else:
        with col2:
            st.info("Veuillez chercher un film.")


    def dataframe_to_context(df):
        # Transformer chaque ligne en une phrase descriptive
        context = "\n".join(
            df.apply(
                lambda row: (
                    f"{row['id']}"
                ),
                axis=1,
            )
        )
        return f"Voici les films disponibles :\n{context}"

    context = dataframe_to_context(df_gemini)

    # Interface utilisateur
    st.markdown("<h3> Demandez à l'IA 🤖 </h3>", unsafe_allow_html=True)
    st.text("Vous ne savez pas précisément quel film vous inspire ? Demandez à l'IA un genre, un thème, un réalisateur ! Essayez donc avec 'film de sorcier', ou 'Tim Burton' par exemple. Le choix de film avec notre Robot est limité, si vous avez un film en tête, tapez le dans la barre de recherche ⬆️")
    user_query = st.text_input("Input gemini", label_visibility="hidden", placeholder="Quel type de film voulez-vous regarder ?")

    if user_query:  # Assurer que user_query n'est pas vide
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
        api_key = os.getenv('api')

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"""Je cherche des films qui correspondent à la demande suivante : {user_query}.
                        Pour chaque film de cette liste {context}, assure-toi qu'il correspond bien à la demande en termes de genre, d'intrigue, ou d'autres critères.
                        Affiche les ID des 5 films qui correspondent le mieux tel qui sont exactement écris dans {context}, et rien d'autre, sous forme de liste et n'écris rien d'autres."""}
                    ]
                }
            ]
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=payload, params={"key": api_key})
        
        response_json = response.json()
        films_text = response_json['candidates'][0]['content']['parts'][0]['text']

        cleaned_text = re.sub(r'\*', '', films_text)
        film_titles = cleaned_text.strip().splitlines()

        # Créer une liste pour stocker les titres trouvés dans le DataFrame
        titre_gemini = []
        annee_gemini = []
        real_gemini = []
        poster_gemini = []
    
    # Filtrer le DataFrame pour chaque titre extrait et ajouter les résultats
        for el in film_titles:
            el = el.strip()
            filtered_df = df_poster[df_poster['id'] == el]

            if not filtered_df.empty:  # Vérifier si le DataFrame n'est pas vide
                titre_gemini.append(filtered_df['titre'].values[0])
                annee_gemini.append(filtered_df['année'].values[0])
                real_gemini.append(filtered_df['Real'].values[0])
                poster_gemini.append(filtered_df['poster_path'].values[0])

        # Si aucun film n'a été trouvé, afficher un message d'avertissement
        if not titre_gemini:
            st.warning("Aucun film trouvé correspondant à votre recherche.")
        else:
            columns = st.columns(5)

            # Affichage des recommandations dans les colonnes
            for i, (titre_g, annee_g, realisateur_g, poster_path_g) in enumerate(zip(titre_gemini, annee_gemini, real_gemini, poster_gemini)):
                with columns[i % 5]:  # Répartir les films sur 5 colonnes
                    st.markdown(f"{titre_g}", unsafe_allow_html=True)

                    # Vérification si le poster est disponible
                    if not poster_path_g:
                        st.image("wcs/projet_2/logo_sans_fond.png", width=150)  # Afficher une image par défaut si aucun poster n'est trouvé
                    else:
                        st.image(f"{image_url}{poster_path_g}", width=150)  # Afficher l'image du poster

                    # Affichage des autres informations
                    st.text(f"📅 Année : {annee_g}")
                    st.text(f"🎥 Réalisateur : {realisateur_g}")

    else:
        st.warning("Veuillez entrer un type de film pour obtenir des recommandations.")
    ''')

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


