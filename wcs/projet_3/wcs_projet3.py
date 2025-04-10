import streamlit as st
import json
from wcs.projet_3.func.SQL_user import SQL_user
from wcs.projet_3.chat import chatbot
from wcs.projet_3.dash_admin import dash_admin
from dotenv import load_dotenv

load_dotenv()

def afficher_wcs_projet3():
    # Initialisation de la variable pour suivre la page active
    if "page_projet3" not in st.session_state:
        st.session_state.page_projet3 = "login"  # Par défaut, la page d'accueil du projet 2 est affichée

    # Définition d'une fonction pour changer la page active
    def set_page(page_name):
        st.session_state.page_projet2 = page_name  # Modification de la variable pour changer de page


    sql_user = SQL_user()

    def main():
        # Initialiser les variables de session
        if "authenticated" not in st.session_state:
            st.session_state["authenticated"] = False
            st.session_state["current_user"] = None
            st.session_state["current_page"] = "Landing"  # Page par défaut au démarrage
        if "user_id" not in st.session_state:
            st.session_state["user_id"] = None

        # Afficher la page actuelle
        if st.session_state["authenticated"]:
            if st.session_state["current_page"] == "chat":
                chatbot()
            elif st.session_state["current_page"] == "Compte":
                show_account_page()
            elif st.session_state["current_page"] == "Admin":
                dash_admin()
        else:
            if st.session_state["current_page"] == "Landing":
                show_landing_page()
            elif st.session_state["current_page"] == "Signup":
                show_signup_form()
            elif st.session_state["current_page"] == "Login":
                show_login_form()

    def show_landing_page():
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image("wcs/projet_3/img/logo_home_search_and_go.png")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Créer un compte", use_container_width=True):
                st.session_state["current_page"] = "Signup"
                st.rerun()
        with col2:
            if st.button("Se connecter", use_container_width=True):
                st.session_state["current_page"] = "Login"
                st.rerun()

    def show_signup_form():
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image("wcs/projet_3/img/logo_home_search_and_go.png")
        st.title("Créer un compte")
        # Formulaire de création de compte
        with st.form("signup_form"):
            name = st.text_input("Nom")
            lastname = st.text_input("Prénom")
            email = st.text_input("Email")
            password = st.text_input("Mot de passe", type="password",
                                     help="Mot de passe de 8 caractères alphanumérique avec majuscule et symbole",
                                     label_visibility='visible')
            submit = st.form_submit_button("Valider")

        if submit:
            if sql_user.is_email_known(email):
                st.warning("Un compte avec cet email existe déjà !")
            else:
                if sql_user.validate_user(email, password, name, lastname):
                    sql_user.add_user(email, password, name, lastname)
                    st.success("Compte créé avec succès ! Vous pouvez maintenant vous connecter.")
                    st.session_state["current_page"] = "Login"
                    st.rerun()

    def show_login_form():
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image("wcs/projet_3/img/logo_home_search_and_go.png")
        st.subheader("Se connecter")
        # Formulaire de connexion
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Mot de passe", type="password")
            submit = st.form_submit_button("Valider")

            if submit:
                st.session_state["user_id"] = sql_user.is_authentificate(email, password)
                # Vérifier les informations d'identification
                if st.session_state["user_id"][2] == "Big Boss Robot":
                    st.session_state["authenticated"] = True
                    st.session_state["current_user"] = email
                    st.session_state["current_page"] = "Admin"
                    st.rerun()
                elif st.session_state["user_id"][0]:
                    st.session_state["authenticated"] = True
                    st.session_state["current_user"] = email
                    st.session_state["current_page"] = "chat"
                    st.rerun()
                else:
                    st.error("Email ou mot de passe incorrect !")

    def show_account_page():
        email = st.session_state["current_user"]
        user_data = email
        st.title("Mon compte")
        st.write(f"**Nom**: {user_data['nom']}")
        st.write(f"**Prénom**: {user_data['prenom']}")
        st.write(f"**Email**: {email}")

        if st.button("Retour à l'accueil"):
            st.session_state["current_page"] = "chat"

    main()

