import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
        .stApp {
            background:#F7F9FB !important;
        }
        </style>
    """, unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@300..700&family=Inter:wght@400;500;600&display=swap');

        #MainMenu, header, footer {
            visibility: hidden;
        }
        .block-container {
            padding-top: 1.5rem !important;
            max-width: 900px !important;
        }
        h2, h3, h4, p {
            font-family: "Roboto Slab", serif;
        }
        h2 {
            color:#0B2540;
            font-weight:700;
            letter-spacing:0.2px;
        }

        div[data-testid="column"] {
            padding: 0 0.5rem;
        }

        /* Portal cards */
        .portal-card {
            background:#FFFFFF;
            border:1px solid #E1E7ED;
            padding:2rem 1.5rem;
            text-align:center;
            box-shadow:0 2px 6px rgba(11,37,64,0.05);
        }
        .portal-card h3 {
            color:#0B2540;
            font-weight:600;
            margin-bottom:0.4rem;
        }
        .portal-card p {
            color:#5A6B7B;
            font-size:0.9rem;
            margin-bottom:1.2rem;
        }

        /* Divider */
        hr {
            border-color:#E1E7ED !important;
            margin:1.5rem 0 !important;
        }


        /* Buttons — single merged rule, nothing overridden away */
        div.stButton > button {
            width:100%;
            padding:0.7rem 1rem !important;
            border-radius:10px;
            background:#0B2540;
            color:#FFFFFF;
            border:none;
            font-family:"Inter", sans-serif !important;
            font-weight:500;
            font-size:0.92rem;
            letter-spacing:0.2px;
            transition: background 0.2s ease, transform 0.15s ease, border-color 0.2s ease;
        }
        div.stButton > button p {
            font-family:"Inter", sans-serif !important;
            font-weight:500 !important;
        }
        div.stButton > button:hover {
            background:#1B6FA8;
            color:#FFFFFF;
        }

        /* secondary type = outlined, overrides the base fill above */
        div.stButton > button[kind="secondary"] {
            background:#1B6FA8;
            color:white;
            border:2px solid #D8DFE6;
        }
        div.stButton > button[kind="secondary"]:hover {
            border-color:#1B6FA8;
            color:#1B6FA8;
            background:#F7FAFC;
        }

        /* primary type = filled navy, explicit for clarity */
        div.stButton > button[kind="primary"] {
            background:#0B2540;
            color:#FFFFFF;
            border:none;
        }
        div.stButton > button[kind="primary"]:hover {
            background:#1B6FA8;
            transform: translateY(-1px);
        }

        /* Toast / alerts */
        div[data-testid="stAlert"] {
            border-radius:10px;
            font-family:"Inter", sans-serif;
        }

        /* Footer note */
        .footer-note {
            text-align:center;
            color:#9AA7B2;
            font-size:0.78rem;
            margin-top:2.5rem;
            margin-bottom:3rem;
        }
        </style>
    """, unsafe_allow_html=True)