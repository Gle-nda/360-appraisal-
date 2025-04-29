
import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

import json

# STREAMLIT PAGE CONFIG.

st.set_page_config(page_title='360° Appraisal System', page_icon='⚖️⭐', layout="centered",
                   initial_sidebar_state="collapsed")

hide_streamlit_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with open('C://Users//user//PycharmProjects//360 Appraisal System//pages/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

if ("supervision", "attitude", "conflict_res_sub", "interpersonal_rel", "comm_skills_sub", "sub_sum", "sub_score",
    "comments_sub") \
        not in st.session_state:

    st.session_state["supervision"] = 0
    st.session_state["attitude"] = 0
    st.session_state["conflict_res_sub"] = 0
    st.session_state["interpersonal_rel"] = 0
    st.session_state["comm_skills_peer"] = 0
    st.session_state.comments_sub = ""
    st.session_state["sub_sum"] = 0
    st.session_state["sub_score"] = 0


def subs_form():
    uname = st.expander(label="Dear Appraisee's Subordinate, kindly slide the bars below to give input.", expanded=True)
    st.session_state.supervision = uname.slider(label="Supervision Skills", min_value=0, max_value=5, step=1, value=0)
    st.session_state.attitude = uname.slider(label="Attitude to work and colleagues", min_value=0, max_value=5, step=1,
                                          value=0)
    st.session_state.conflict_res_sub = uname.slider(label="Conflict Resolution", min_value=0, max_value=5, step=1,
                                                  value=0)
    st.session_state.interpersonal_rel = uname.slider(label="Interpersonal Relations", min_value=0, max_value=5, step=1,
                                                   value=0)
    st.session_state.comm_skills_peer = uname.slider(label="Communication Skills  ", min_value=0, max_value=5, step=1,
                                                  value=0)

    st.session_state.sub_sum = st.session_state.supervision + st.session_state.attitude + st.session_state.conflict_res_sub + st.session_state.interpersonal_rel + st.session_state.comm_skills_peer

    st.session_state.sub_score = st.session_state.sub_sum / 5

    uname.write("Please score the employee's overall performance for th evaluation period on a scale of 0-4.")
    overall0 = uname.checkbox("Poor(0)")
    overall1 = uname.checkbox("Fair(1)")
    overall2 = uname.checkbox("Good(2)")
    overall3 = uname.checkbox("V. Good(3)")
    overall4 = uname.checkbox("Excellent(4)")

    st.session_state.comments_sub = uname.text_input(label="Any other comment(s):")

    data = {st.session_state.username: []}

    # Load existing data (if any)
    try:
        with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "r") as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}

    # Update existing data with new data
    existing_data.update(data)
    existing_data[st.session_state.username].append({st.session_state.username: [st.session_state.supervision,
                                                                                  st.session_state.attitude,
                                                                                  st.session_state.conflict_res_sub,
                                                                                  st.session_state.interpersonal_rel,
                                                                                  st.session_state.comm_skills_peer,
                                                                                  st.session_state.sub_sum,
                                                                                  st.session_state.sub_score,
                                                                                  st.session_state.comments_sub]})

    # Write updated data back to the file
    with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=2)

authenticator.login(location="main")

if st.session_state["authentication_status"]:

    st.write(f'Welcome *{st.session_state["name"]}*')

    profiles = st.expander(label="User Profile", expanded=False)
    profiles.write(config["credentials"]["usernames"][st.session_state.username])

    if st.session_state["username"] == "sub1" or "sub2" or "sub3":

        subs_form()

    authenticator.logout()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')