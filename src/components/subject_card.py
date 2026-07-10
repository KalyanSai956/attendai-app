import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:white; border-left: 8px solid #1B6FA8; padding:25px; border-radius: 20px; border: 1px solid #E1E7ED; margin-bottom:20px;">
        <h3 style="margin:0; color: #0B2540; font-size: 1.5rem ">{name}</h3>
        <p style="color:#5A6B7B; margin:10px 0;">Code : <span style="background:#EAF1F7; color:#1B6FA8; padding:2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #1B6FA810; padding:5px 12px; border-radius:12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()