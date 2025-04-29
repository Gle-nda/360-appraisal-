import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

import pandas as pd

import json

with open('C://Users//user//PycharmProjects//360 Appraisal System//pages//config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

authenticator.login(location="main")

if st.session_state["authentication_status"]:

    st.write(f'Welcome *{st.session_state["name"]}*')

    if st.session_state['username'] == 'admin':

        try:
            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(
                pre_authorization=False)
            if email_of_registered_user:
                st.success('User registered successfully')

                with open('C://Users//user//PycharmProjects//360 Appraisal System//pages/config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)

        except Exception as e:
            st.error(e)

        st.subheader("Nominate Appraisers.")

        try:
            with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "r") as json_file:
                existing_data = json.load(json_file)

        except:

            pass

        for key in existing_data["appraisee"][0]:

            nominated_subs = pd.read_json(existing_data["appraisee"][0][key][-3:][-3])
            nominated_peers = pd.read_json(existing_data["appraisee"][0][key][-3:][-2])
            nominated_customers = pd.read_json(existing_data["appraisee"][0][key][-3:][-1])

            break
        st.write("Nominators below Appraisee's rank.")
        st.write(nominated_subs)
        st.write("Nominators who are Appraisee's peers")
        st.write(nominated_peers)
        st.write("Nominators who are served by the Appraisee i.e. customers")
        st.write(nominated_customers)

        appraisers = st.text_area(label="List below 1 nominee from each form.")
        nominated_subs = nominated_subs.to_json()
        nominated_peers = nominated_peers.to_json()
        nominated_customers = nominated_customers.to_json()


        data = {st.session_state.username: []}

        # Load existing data (if any)
        try:
            with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "r") as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = {}

        # Update existing data with new data
        existing_data.update(data)
        existing_data[st.session_state.username].append({"appraisers":[appraisers]})

        # Write updated data back to the file
        with open("C://Users//user//PycharmProjects//360 Appraisal System//pages/data.json", "w") as json_file:
            json.dump(existing_data, json_file, indent=2)

        profiles = st.expander(label="See User Profiles", expanded=False)
        profiles.write(config["credentials"]["usernames"])


    authenticator.logout()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')