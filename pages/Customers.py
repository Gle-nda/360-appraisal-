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

if ("comm_skills", "prompt_response", "pr", "dependability",
    "commitment_service", "customer_score", "customer_sum") not in st.session_state:

    st.session_state["comm_skills"] = 0
    st.session_state["prompt_response"] = 0
    st.session_state["pr"] = 0
    st.session_state["dependability"] = 0
    st.session_state["commitment_service"] = 0
    st.session_state["customer_sum"] = 0
    st.session_state["customer_score"] = 0

def customers_form():
    uname = st.expander(label="Dear Customer, kindly slide the bars below to give input.", expanded=True)
    st.session_state.comm_skills = uname.slider(label="Communication Skills   ", min_value=0, max_value=5, step=1, value=0,
                                             key="customer_commSkills")
    st.session_state.prompt_response = uname.slider(label="Promptness to response", min_value=0, max_value=5, step=1,
                                                 value=0)
    st.session_state.pr = uname.slider(label="Public Relations", min_value=0, max_value=5, step=1, value=0)
    st.session_state.dependability = uname.slider(label="Dependability", min_value=0, max_value=5, step=1, value=0)
    st.session_state.commitment_service = uname.slider(label="Commitment to service", min_value=0, max_value=5, step=1,
                                                    value=0)

    st.session_state.customer_sum = (
                                              st.session_state.comm_skills + st.session_state.prompt_response +
                                              st.session_state.pr + st.session_state.commitment_service +
                                              st.session_state.dependability)

    st.session_state.customer_score = st.session_state.customer_sum / 5
    uname.write("Please score the employee's overall performance for th evaluation period on a scale of 0-4.")
    overall0 = uname.checkbox("Poor(0)")
    overall1 = uname.checkbox("Fair(1)")
    overall2 = uname.checkbox("Good(2)")
    overall3 = uname.checkbox("V. Good(3)")
    overall4 = uname.checkbox("Excellent(4)")
    strengths = uname.text_input(label="List below the employee's main strengths:")
    support = uname.text_input(
        label="List below the employee's work in which they have difficulties and may need further training or support:")

    data = {st.session_state.username: []}

    # Load existing data (if any)
    try:
        with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "r") as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}

    # Update existing data with new data
    existing_data.update(data)
    existing_data[st.session_state.username].append({st.session_state.username: [st.session_state.comm_skills,
                                                                                 st.session_state.prompt_response,
                                                                                 st.session_state.pr,
                                                                                 st.session_state.dependability,
                                                                                 st.session_state.commitment_service,
                                                                                 st.session_state.customer_sum,
                                                                                 st.session_state.customer_score,
                                                                                 support,
                                                                                 strengths
                                                                                 ]})

    # Write updated data back to the file
    with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "w") as json_file:
        json.dump(existing_data, json_file, indent=2)


authenticator.login(location="main")

if st.session_state["authentication_status"]:

    st.write(f'Welcome *{st.session_state["name"]}*')

    profiles = st.expander(label="User Profile", expanded=False)
    profiles.write(config["credentials"]["usernames"][st.session_state.username])

    if st.session_state['username'] == 'customer1' or "customer2" or "customer3":

        customers_form()

    authenticator.logout()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

