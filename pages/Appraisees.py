import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

import pandas as pd

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


if ("training", "comm", "personal_dev", "prod", "prof", "drive", "creativity", "integrity", "decision", "depend",
    "punctual", "deliver", "lead", "score", "sum", "SUB_nomination_form", "SUB_nominaters", "PEER_nomination_form",
    "PEER_nominaters", "CUS_nomination_form", "CUS_nominaters", "support_appraisee_yes", "support_appraisee_no") \
    not in st.session_state:
    st.session_state.training = ""
    st.session_state["comm"] = 0
    st.session_state["prod"] = 0
    st.session_state["prof"] = 0
    st.session_state["drive"] = 0
    st.session_state["creativity"] = 0
    st.session_state["integrity"] = 0
    st.session_state["decision"] = 0
    st.session_state["depend"] = 0
    st.session_state["punctual"] = 0
    st.session_state["deliver"] = 0
    st.session_state["lead"] = 0
    st.session_state["sum"] = 0
    st.session_state["score"] = 0
    st.session_state["SUB_nominaion_form"] = pd.DataFrame()
    st.session_state["SUB_nominaters"] = ""
    st.session_state["PEER_nomination_form"] = pd.DataFrame()
    st.session_state["PEER_nominaters"] = ""
    st.session_state["CUS_nomination_form"] = pd.DataFrame()
    st.session_state["CUS_nominaters"] = ""
    st.session_state["pdev"] = 0
    st.session_state["support_appraisee_yes"] = ""
    st.session_state["support_appraisee_no"] = ""

def appraisee_form():

    uname = st.expander(label="Dear Appraisee, kindly slide the bars below to give input.", expanded=True)
    uname.write("Are there any areas of your work which you have difficulties and would like to have further training or support?")
    st.session_state.support_appraisee_yes = uname.checkbox("Yes")
    st.session_state.support_appraisee_no = uname.checkbox("No")
    st.session_state.training = uname.text_input(label="If yes, please explain ")
    st.session_state.comm = uname.slider(label="Communication", min_value=0, max_value=5, step=1, value=0)
    st.session_state.personal_dev = uname.slider(label="Personal Development/Skills Enhancements", min_value=0, max_value=5,
                                      step=1, value=0)
    st.session_state.prod = uname.slider(label="Productivity", min_value=0, max_value=5, step=1, value=0)
    st.session_state.prof = uname.slider(label="Professionalism", min_value=0, max_value=5, step=1, value=0)
    st.session_state.drive = uname.slider(label="Initiative and Self Drive", min_value=0, max_value=5, step=1,
                                            value=0)
    st.session_state.creativity = uname.slider(label="Creativity", min_value=0, max_value=5, step=1, value=0)
    st.session_state.integrity = uname.slider(label="Integrity and Honesty", min_value=0, max_value=5, step=1, value=0)
    st.session_state.decision = uname.slider(label="Decision-making", min_value=0, max_value=5, step=1, value=0)
    st.session_state.depend = uname.slider(label="Dependability and Resourcefulness", min_value=0, max_value=5, step=1,
                                          value=0)
    st.session_state.deliver = uname.slider(label="Delivery and Promptness", min_value=0, max_value=5, step=1, value=0)
    st.session_state.lead = uname.slider(label="Leadership Skills", min_value=0, max_value=5, step=1, value=0)

    st.session_state.sum = (st.session_state.comm + st.session_state.prod + st.session_state.prof
                            + st.session_state.personal_dev + st.session_state.drive + st.session_state.creativity
                            + st.session_state.integrity
                            + st.session_state.decision + st.session_state.depend + st.session_state.punctual
                            + st.session_state.deliver + st.session_state.lead)

    st.session_state.score = st.session_state.sum / 12
    st.write("Please list names of three(3) employees below your rank who you think are best suited to appraise you on your leadership skills.")
    st.session_state.SUB_nomination_form = pd.DataFrame({"Name":"", "PF":"", "Designation":"", "Department":""},
                                               [1, 2, 3])

    st.session_state.SUB_nominaters = st.data_editor(st.session_state.SUB_nomination_form).to_json(orient="records")

    st.write("Please list names of three (3) peers who are best suited to appraise you on your teamwork abilities.")
    st.session_state.PEER_nomination_form = pd.DataFrame({"Name":"", "PF":"", "Designation":"", "Department":""},
                                               ["I", "II", "III"])

    st.session_state.PEER_nominaters = st.data_editor(st.session_state.PEER_nomination_form).to_json(orient="records")

    st.write("Please list names of three(3) of your internal customers who are best suited to appraise you on your customer service abilities.")
    st.session_state.CUS_nomination_form = pd.DataFrame({"Name":"", "PF":"", "Designation":"", "Department":""},
                                               ["i","ii" , "iii"])

    st.session_state.CUS_nominaters = st.data_editor(st.session_state.CUS_nomination_form).to_json(orient="records")
    data = {st.session_state.username: []}

    # Load existing data (if any)
    try:
        with open("C://Users//user//PycharmProjects//360 Appraisal System//pages//data.json", "r") as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}

    # Update existing data with new data
    existing_data.update(data)
    existing_data[st.session_state.username].append({st.session_state.username: [st.session_state.training,
                                                                                 st.session_state.support_appraisee_yes,
                                                                                 st.session_state.support_appraisee_no,
                                                                                 st.session_state.comm,
                                                                                 st.session_state.personal_dev,
                                                                                 st.session_state.prod,
                                                                                 st.session_state.prof,
                                                                                 st.session_state.drive,
                                                                                 st.session_state.creativity,
                                                                                 st.session_state.integrity,
                                                                                 st.session_state.decision,
                                                                                 st.session_state.depend,
                                                                                 st.session_state.punctual,
                                                                                 st.session_state.deliver,
                                                                                 st.session_state.lead,
                                                                                 st.session_state.sum,
                                                                                 st.session_state.score,
                                                                                 st.session_state.SUB_nominaters,
                                                                                 st.session_state.PEER_nominaters,
                                                                                 st.session_state.CUS_nominaters]})

    # Write updated data back to the file
    with open("C://Users//user//PycharmProjects//360 Appraisal System//pages//data.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=2)

authenticator.login(location="main")

if st.session_state["authentication_status"]:

    st.write(f'Welcome *{st.session_state["name"]}*')

    profiles = st.expander(label="User Profile", expanded=False)
    profiles.write(config["credentials"]["usernames"][st.session_state.username])

    if st.session_state['username'] == 'appraisee':

        appraisee_form()

    authenticator.logout()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')