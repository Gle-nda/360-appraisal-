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

if ("comm_skills_hod","prof_hod", "initiative_hod", "creativity_hod", "integrity_hod", "decision_hod", "depend_hod",
    "punctual_hod", "delivery_hod", "lead_hod", "score_hod", "sum_hod") not in st.session_state:

    st.session_state["comm_skills_hod"] = 0
    st.session_state["prof_hod"] = 0
    st.session_state["initiative_hod"] = 0
    st.session_state["creativity_hod"] = 0
    st.session_state["integrity_hod"] = 0
    st.session_state["decision_hod"] = 0
    st.session_state["depend_hod"] = 0
    st.session_state["punctual_hod"] = 0
    st.session_state["delivery_hod"] = 0
    st.session_state["lead_hod"] = 0
    st.session_state["score_hod"] = 0
    st.session_state["sum_hod"] = 0

def hods_form():

    uname = st.expander(label="Dear HoD, kindly slide the bars below to give input.", expanded=True)
    st.session_state.comm_skills_hod = uname.slider(label="Communication ", min_value=0, max_value=5, step=1, value=0)
    st.session_state.prof_hod = uname.slider(label="Professionalism.", min_value=0, max_value=5, step=1, value=0)
    st.session_state.initiative_hod = uname.slider(label="Initiative and self drive", min_value=0, max_value=5, step=1,
                                                value=0)
    st.session_state.creativity_hod = uname.slider(label="Creativity  ", min_value=0, max_value=5, step=1, value=0)
    st.session_state.integrity_hod = uname.slider(label="Integrity and Honesty  ", min_value=0, max_value=5, step=1,
                                               value=0)
    st.session_state.decision_hod = uname.slider(label="Decision Making", min_value=0, max_value=5, step=1, value=0)
    st.session_state.depend_hod = uname.slider(label="Dependability and Resourcefulness ", min_value=0, max_value=5,
                                            step=1, value=0)
    st.session_state.punctual_hod = uname.slider(label="Punctuality and Attendance", min_value=0, max_value=5, step=1,
                                              value=0)
    st.session_state.delivery_hod = uname.slider(label="Delivery and Promptness ", min_value=0, max_value=5, step=1,
                                              value=0)
    st.session_state.lead_hod = uname.slider(label="Leadership Skills  ", min_value=0, max_value=5, step=1, value=0)

    st.session_state.sum_hod = (
                                         st.session_state.comm_skills_hod + st.session_state.prof_hod
                                         + st.session_state.initiative_hod + st.session_state.creativity_hod
                                         + st.session_state.decision_hod + st.session_state.depend_hod
                                         + st.session_state.punctual_hod + st.session_state.delivery_hod
                                         + st.session_state.lead_hod)

    st.session_state.score_hod = st.session_state.sum_hod / 10

    uname.write("Please score the employee's overall performance for th evaluation period on a scale of 0-4.")
    overall0 = uname.checkbox("Poor(0)")
    overall1 = uname.checkbox("Fair(1)")
    overall2 = uname.checkbox("Good(2)")
    overall3 = uname.checkbox("V. Good(3)")
    overall4 = uname.checkbox("Excellent(4)")

    strengths_hod = uname.text_input(label="List below the employee's main strengths: ")
    support_hod = uname.text_input(
        label=
        " List below the employee's work in which they have difficulties and may need further training or support:")

    data = {st.session_state.username: []}

    # Load existing data (if any)
    try:
        with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "r") as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}

    # Update existing data with new data
    existing_data.update(data)
    existing_data[st.session_state.username].append({st.session_state.username: [
                                         st.session_state.comm_skills_hod, st.session_state.prof_hod,
                                         st.session_state.initiative_hod, st.session_state.creativity_hod,
                                         st.session_state.decision_hod, st.session_state.depend_hod,
                                         st.session_state.punctual_hod, st.session_state.delivery_hod,
                                         st.session_state.lead_hod, st.session_state.sum_hod, st.session_state.score_hod,
                                         strengths_hod, support_hod ]})

    # Write updated data back to the file
    with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=2)


authenticator.login(location="main")

if st.session_state["authentication_status"]:

    st.write(f'Welcome *{st.session_state["name"]}*')

    profiles = st.expander(label="User Profile", expanded=False)
    profiles.write(config["credentials"]["usernames"][st.session_state.username])

    if st.session_state['username'] == 'hod1' or "hod2" or "hod3":

        hods_form()

    authenticator.logout()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
