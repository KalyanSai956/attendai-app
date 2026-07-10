import streamlit as st

def header_home():
    st.markdown("""
        <div style="text-align:center;">
            <p style="
                font-family:'Roboto Slab', serif;
                font-size:0.85rem;
                letter-spacing:3px;
                color:#5A6B7B;
                text-transform:uppercase;
            ">Enterprise Attendance Platform</p>
            <h1 style="
                font-family:'Roboto Slab', serif;
                font-weight:700;
                font-size:3rem;
                color:#0B2540;
                margin:0;
                letter-spacing:1px;
            ">ATTEND <span style="color:#1B6FA8;">AI</span></h1>
            <div style="
                width:80px;
                height:3px;
                background:#1B6FA8;
                margin:1rem auto 0 auto;
            "></div>
        </div>
    """, unsafe_allow_html=True)

def header_dashboard():
    st.markdown("""
        <div style="text-align:center;">
            <h1 style="
                font-family:'Roboto Slab', serif;
                font-weight:700;
                font-size:3rem;
                color:#0B2540;
                margin:0;
                letter-spacing:1px;
            ">ATTEND <span style="color:#1B6FA8;">AI</span></h1>
            <div style="
                width:80px;
                height:3px;
                background:#1B6FA8;
                margin:1rem auto 0 auto;
            "></div>
        </div>
    """, unsafe_allow_html=True)