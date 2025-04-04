import streamlit as st
import time
import os


# Importe uniquement ce qui est nécessaire pour la version de débogage.
# Vous pourrez réintroduire petit à petit vos fonctionnalités.

def chatbot():
    # Pour le débogage, afficher le contenu du session_state
    st.write("DEBUG - Session state:", st.session_state)

    # Assurez-vous d'être sur la page "chat"
    if st.session_state.get("current_page") != "chat":
        st.session_state["current_page"] = "chat"
        st.rerun()  # Redémarrer pour prendre en compte la nouvelle valeur

    st.write("Chatbot page loaded!")

    # Initialisation minimale de l'historique
    if "messages" not in st.session_state:
        st.session_state["messages"] = ["Bienvenue sur le chatbot !"]

    # Affichage des messages du chat
    st.write("Historique des messages :")
    for message in st.session_state["messages"]:
        st.write("- " + str(message))

    # Zone de saisie pour ajouter un message
    user_input = st.text_input("Votre message :", key="user_msg")
    if st.button("Envoyer"):
        if user_input:
            st.session_state["messages"].append(user_input)
            st.experimental_rerun()

    # Bouton de débogage pour simuler la fin d'une opération bloquante
    if st.button("Simuler fin de chargement"):
        st.session_state["simulated_loaded"] = True
        st.experimental_rerun()


# Appel de la fonction chatbot pour afficher la page
chatbot()
