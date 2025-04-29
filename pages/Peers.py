import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

import json

with open('C://Users//user//PycharmProjects//360 Appraisal System//pages/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

if ("coop", "comm_skills_peer", "interpersonal", "ideas", "punctuality",
    "team_player", "flexibility", "conflict_res", "integrity_peer", "prof_peer", "creativity_and_innovativeness",
    "lead_peer", "peer_sum", "peer_score") not in st.session_state:

    st.session_state["coop"] = 0
    st.session_state["comm_skills_peer"] = 0
    st.session_state["interpersonal"] = 0
    st.session_state["ideas"] = 0
    st.session_state["punctuality"] = 0
    st.session_state["team_player"] = 0
    st.session_state["conflict_res"] = 0
    st.session_state["flexibility"] = 0
    st.session_state["integrity_peer"] = 0
    st.session_state["prof_peer"] = 0
    st.session_state["creativity_and_innovativeness"] = 0
    st.session_state["lead_peer"] = 0
    st.session_state["peer_score"] = 0
    st.session_state["supervision"] = 0
    st.session_state["attitude"] = 0
    st.session_state["conflict_res_sub"] = 0
    st.session_state["interpersonal_rel"] = 0
    st.session_state["comm_skills_peer"] = 0
    st.session_state["peer_sum"] = 0
    st.session_state["peer_score"] = 0

def peers_form():
    uname = st.expander(label="Dear Appraisee's Peer, kindly slide the bars below to give input.", expanded=True)
    st.session_state.coop = uname.slider(label="Cooperative", min_value=0, max_value=5, step=1, value=0)
    st.session_state.comm_skills_peer = uname.slider(label="Communication Skills.", min_value=0, max_value=5, step=1,
                                                  value=0)
    st.session_state.interpersonal = uname.slider(label="Interpersonal SKills", min_value=0, max_value=5, step=1, value=0)
    st.session_state.ideas = uname.slider(label="Open to new ideas", min_value=0, max_value=5, step=1, value=0)
    st.session_state.punctuality = uname.slider(label="Punctuality", min_value=0, max_value=5, step=1, value=0)
    st.session_state.team_player = uname.slider(label="Team Player", min_value=0, max_value=5, step=1, value=0)
    st.session_state.conflict_res = uname.slider(label="Conflict Resolution Skills", min_value=0, max_value=5, step=1,
                                              value=0)
    st.session_state.flexibility = uname.slider(label="Flexibility to changes in the working environment", min_value=0,
                                             max_value=5, step=1, value=0)
    st.session_state.integrity_peer = uname.slider(label="Integrity", min_value=0, max_value=5, step=1, value=0)
    st.session_state.prof_peer = uname.slider(label="Professionalism ", min_value=0, max_value=5, step=1, value=0)
    st.session_state.creativity_and_innovativeness = uname.slider(label="Creativity and Innovativeness", min_value=0,
                                                               max_value=5, step=1, value=0)
    st.session_state.lead_peer = uname.slider(label="Leadership Skill", min_value=0, max_value=5, step=1, value=0)

    st.session_state.peer_sum = (
                                          st.session_state.coop + st.session_state.comm_skills_peer
                                          + st.session_state.interpersonal + st.session_state.ideas
                                          + st.session_state.punctuality + st.session_state.team_player
                                          + st.session_state.conflict_res + st.session_state.flexibility
                                          + st.session_state.integrity_peer + st.session_state.prof_peer
                                          + st.session_state.creativity_and_innovativeness
                                          + st.session_state.lead_peer + st.session_state.peer_score)

    st.session_state.peer_score = st.session_state.peer_sum / 12

    uname.write("Please score the employee's overall performance for th evaluation period on a scale of 0-4.")
    overall0 = uname.checkbox("Poor(0)")
    overall1 = uname.checkbox("Fair(1)")
    overall2 = uname.checkbox("Good(2)")
    overall3 = uname.checkbox("V. Good(3)")
    overall4 = uname.checkbox("Excellent(4)")

    comments_peer = uname.text_input(label="Any other comment(s)")

    data = {st.session_state.username: []}

    # Load existing data (if any)
    try:
        with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "r") as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}

    # Update existing data with new data
    existing_data.update(data)
    existing_data[st.session_state.username].append({st.session_state.username: [st.session_state.coop,
                                                                                 st.session_state.comm_skills_peer,
                                          st.session_state.interpersonal, st.session_state.ideas,
                                          st.session_state.punctuality, st.session_state.team_player,
                                          st.session_state.conflict_res, st.session_state.flexibility,
                                          st.session_state.integrity_peer, st.session_state.prof_peer,
                                          st.session_state.creativity_and_innovativeness,
                                          st.session_state.lead_peer, st.session_state.peer_score,
                                          st.session_state.peer_sum, comments_peer]})

    # Write updated data back to the file
    with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=2)

authenticator.login(location="main")

if st.session_state["authentication_status"]:

    st.write(f'Welcome *{st.session_state["name"]}*')

    profiles = st.expander(label="User Profile", expanded=False)
    profiles.write(config["credentials"]["usernames"][st.session_state.username])

    if st.session_state['username'] == 'peer1' or "peer2" or "peer3":

        peers_form()

    authenticator.logout()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')