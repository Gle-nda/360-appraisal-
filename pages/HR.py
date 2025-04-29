import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

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

    profiles = st.expander(label="User Profile", expanded=False)
    profiles.write(config["credentials"]["usernames"][st.session_state.username])

    if st.session_state['username'] == 'hr':

        with open("C://Users//user//PycharmProjects//360 Appraisal System//pages//data.json", "r") as json_file:
            report = json.load(json_file)

        admin_report = report["admin"]
        for key in admin_report[0]:
            admin_report = admin_report[0][key][0]

        appraisee_report = report["appraisee"]
        for key in appraisee_report[0]:
            appraisee_report = appraisee_report[0][key][-4]

        customers_report = report["customer1"]
        for key in customers_report[0]:
            customers_report = customers_report[0][key][-3]

        hods_report = report["hod1"]
        for key in hods_report[0]:
            hods_report = hods_report[0][key][-3]

        peers_report = report["peer1"]
        for key in peers_report[0]:
            peers_report = peers_report[0][key][-3]

        subs_report = report["sub1"]
        for key in subs_report[0]:
            subs_report = subs_report[0][key][-2]

        overall_grade = appraisee_report + hods_report + subs_report + peers_report + customers_report
        overall_grade_pct = (overall_grade / 270) * 100

        if 85 < overall_grade_pct < 100:
            grade = "Excellent."

        elif 70 < overall_grade_pct < 84:
            grade = "Very Good"

        elif 50 < overall_grade_pct < 69:
            grade = "Good"

        elif 40 < overall_grade_pct < 49:
            grade = "Fair"

        elif 0 < overall_grade_pct < 39:
            grade = "Poor"

        else:
            pass

        recommendation = st.text_area("Recommendations on Appraisal.")

        report = "APPRAISEE'S PERFORMANCE SUMMARY." + "\n" + "Self Assessment: " + str(
            appraisee_report) + "\n" + "Customer Evaluation: " \
                 + str(customers_report) + "\n" + "Evaluation on Values and Staff Competency: " + str(
            hods_report) + "\n" + "Peer Evaluation: " + str(
            peers_report) + "\n" + "Evaluation by employees below rank: " \
                 + str(subs_report) + "\n" + "Your Overall Score is: " + str(overall_grade) + "\n" +"Your Overall Grade is: "\
        + str(grade) + "\n" + "Recommendation on Appraisal: " + recommendation





        st.download_button(label="Generate REPORT", data=report, file_name="report.txt", mime="text/plain")

    authenticator.logout()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
