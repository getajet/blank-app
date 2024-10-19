import streamlit as st
import subprocess
import threading
import queue
import time

def run_command(command, output_queue):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    for line in process.stdout:
        output_queue.put(line)
    for line in process.stderr:
        output_queue.put(line)
    process.wait()

def stream_console_output(command):
    st.title('Console Output in Streamlit')

    output_queue = queue.Queue()
    thread = threading.Thread(target=run_command, args=(command, output_queue))
    thread.start()

    output_lines = []

    while thread.is_alive() or not output_queue.empty():
        while not output_queue.empty():
            line = output_queue.get()
            output_lines.append(line)
        st.text_area('Console Output', value=''.join(output_lines), height=400, key='console_output')
        time.sleep(0.1)

if __name__ == "__main__":
    command = st.text_input('Enter the command to run:', value='echo Hello, Streamlit!')
    if st.button('Run Command'):
        stream_console_output(command)
