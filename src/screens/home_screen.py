import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_background_home, style_base_layout
from src.components.footer import footer

def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown("""
            <div class="portal-card">
                <h3>Teacher Portal</h3>
                <p>Manage classes, mark attendance, and view reports.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Teacher Portal", key="teacher_btn"):
            st.session_state['login_type'] = "teacher"
            st.rerun()

    with col2:
        st.markdown("""
            <div class="portal-card">
                <h3>Student Portal</h3>
                <p>Check your attendance history and schedule.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Student Portal", key="student_btn"):
            st.session_state['login_type'] = "student"
            st.rerun()
    footer()