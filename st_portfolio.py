import streamlit as st

st.title("Bienvenue sur mon portfolio")

st.markdown(
    """
    <h1 style='text-align: center; color: #5C6BC0;'>
       <iframe title="Projet final" width="960" height="540" src="https://app.powerbi.com/reportEmbed?reportId=b75cffeb-b1b8-4f0b-ab42-b0a5a3404c5c&autoAuth=true&ctid=986299fe-66a9-4d37-9a47-cdce9bc9721f" frameborder="0" allowFullScreen="true"></iframe>
    </h1>
    """,
    unsafe_allow_html=True
)
