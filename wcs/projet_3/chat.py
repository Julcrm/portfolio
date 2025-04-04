import json
import requests
import pandas as pd
from wcs.projet_3.func.gepetto import Robot_bistro
from PIL import Image
from io import BytesIO
import folium
from wcs.projet_3.func.mage_local import Mage_local
#from streamlit_js_eval import get_geolocation  # Décommentez si nécessaire
from streamlit_float import *
import streamlit.components.v1 as components
import time
from streamlit_option_menu import option_menu
from wcs.projet_3.dash_user import dash_user
from wcs.projet_3.func.SQL_user import SQL_user
import streamlit as st
import os

def chatbot():
    mage_local = Mage_local()
    sql_user = SQL_user()

    # Dès que l'utilisateur est authentifié, forcer l'affichage du chatbot et mettre à jour les clés héritées
    if st.session_state.get("authenticated"):
        st.session_state["current_page"] = "chat"
        st.session_state["page_projet3"] = "chat"
        if st.session_state.get("page") == "wcs_projet3":
            st.session_state["page"] = "chat"

    API_KEY = os.getenv('api_google')

    if st.session_state.get("current_page") == "chat":
        # Initialisation de l'étape du chatbot
        if "current_step" not in st.session_state:
            st.session_state["current_step"] = "🤖 Discute avec Robot bistro"

        # Initialisation des variables nécessaires
        st.session_state.setdefault('dico', dict())
        st.session_state.setdefault("has_moved_to_step_2", False)

        # Fonction d'ajout de message et génération de réponse
        def addtext():
            user_input = st.session_state.get("prompt", "")
            if user_input:
                st.session_state.setdefault("messages", []).append({"role": "user", "text": user_input})
                st.session_state["history"] = [msg["text"] for msg in st.session_state["messages"] if msg["role"] == "user"]
            context = "\n".join([msg["text"] for msg in st.session_state.get("messages", [])])
            response_bot = st.session_state["robot"].talk(context)
            st.session_state["messages"].append({"role": "assistant", "text": response_bot})

        # Affichage de la première étape du chatbot
        if st.session_state["current_step"] == "🤖 Discute avec Robot bistro":
            options_1 = ["🤖 Discute avec Robot bistro"]
            selection_1 = st.pills("Les étapes :", options_1, selection_mode="single", default=st.session_state["current_step"])
            st.divider()
            if selection_1 != st.session_state["current_step"]:
                st.session_state["current_step"] = selection_1
                st.rerun()

            chat_col, empty_col, img_col = st.columns([1.5, 0.1, 1])
            with img_col:
                st.image("wcs/projet_3/img/Leonardo_Phoenix_09_a_whimsical_cartoon_illustration_of_a_robo_1.jpg", width=500)
            with chat_col:
                if "user_location" not in st.session_state:
                    st.session_state["user_location"] = ()
                # Pour tester, on commente temporairement l'appel à get_geolocation()
                # location_data = get_geolocation()
                # if location_data:
                #     user_lat = location_data.get("coords", {}).get("latitude")
                #     user_lon = location_data.get("coords", {}).get("longitude")
                #     if user_lat and user_lon:
                #         st.session_state["user_location"] = (user_lat, user_lon)
                #     else:
                #         st.warning("Impossible d'obtenir votre localisation. Activez la géolocalisation.")
                if "robot" not in st.session_state:
                    st.session_state["robot"] = Robot_bistro()
                    st.session_state["robot"].preprompt("wcs/projet_3/prompt/robot_chat.txt")
                if "messages" not in st.session_state:
                    st.session_state["messages"] = []
                avatar_bot = "wcs/projet_3/img/icons8-robot-100.png"
                avatar_user = "wcs/projet_3/img/user.png"
                st.chat_message("assistant", avatar=avatar_bot).write(st.session_state["robot"].get_welcome())
                for message in st.session_state["messages"]:
                    avatar = avatar_user if message["role"] == "user" else avatar_bot
                    st.chat_message(message["role"], avatar=avatar).write(message["text"])

                action_buttons_container = st.container(key="testcont")
                cols_dimensions = [20, 29, 40, 9]
                col1, col2, col3, col4 = action_buttons_container.columns(cols_dimensions)
                with col2:
                    if st.button("Réinitialiser le Chat 🧹"):
                        st.session_state["messages"] = []
                        st.rerun()
                with col3:
                    icon = "😩 J'ai FAIMMMM !!! 😩"
                    if st.button(icon):
                        st.session_state.setdefault("history", [])
                        df_resto = sql_user.listing_resto(st.session_state['user_id'][1])
                        category_counts = df_resto['Catégorie'].value_counts()
                        df_favorite = pd.DataFrame(category_counts).reset_index()
                        adresse = mage_local.gps_to_address_google(
                            st.session_state["user_location"][0],
                            st.session_state["user_location"][1]
                        )
                        phrase = f"Je veux manger {df_favorite['Catégorie'].iloc[0]}, à cette adresse {adresse}, sans budget ni régime particulier"
                        st.toast(f'Vous avez faim et vous aimez la {df_favorite["Catégorie"].iloc[0]}')
                        time.sleep(0.5)
                        st.toast("Allez Go !! je m'occupe de vous trouver ça", icon='🎉')
                        time.sleep(0.5)
                        st.session_state["history"].append(phrase)
                        query = st.session_state["robot"].talk(phrase)
                        st.session_state["history"].append(query)
                        st.session_state["robot_hist"] = Robot_bistro()
                        st.session_state["robot_hist"].preprompt("wcs/projet_3/prompt/robot_hist.txt")
                        history = st.session_state["robot_hist"].talk(st.session_state["history"])
                        st.session_state["extracted_info"] = history
                        st.session_state["has_moved_to_step_2"] = True
                        st.session_state["current_step"] = "🍽️ Trouve ton resto idéal"
                        st.rerun()

                st.chat_input("Faites une demande", key="prompt", on_submit=addtext)

            if any("Très bien. Tout est bon, je lance la recherche !" in msg["text"] for msg in st.session_state.get("messages", [])) and not st.session_state["has_moved_to_step_2"]:
                st.session_state["robot_hist"] = Robot_bistro()
                st.session_state["robot_hist"].preprompt("wcs/projet_3/prompt/robot_hist.txt")
                history = [f'{dico["role"]}:{dico["text"]}' for dico in st.session_state["messages"]]
                st.session_state["extracted_info"] = st.session_state["robot_hist"].talk(history)
                st.session_state["has_moved_to_step_2"] = True
                st.session_state["current_step"] = "🍽️ Trouve ton resto idéal"
                st.rerun()

            def get_resized_image(photo_reference, size=(200, 200)):
                default_img = Image.open("wcs/projet_3/img/icons8-robot-100.png").resize((200, 200))
                image_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference="
                if not photo_reference:
                    return default_img
                try:
                    img_url = f"{image_url}{photo_reference}&key={API_KEY}"
                    response = requests.get(img_url)
                    if response.status_code == 200:
                        img = Image.open(BytesIO(response.content)).resize(size)
                        return img
                except Exception:
                    pass
                return default_img

if __name__ == '__main__':
    chatbot()
