import functions
import streamlit as st

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title('\~KG To-Do\~')
st.subheader('Simple checklist app')
st.write('This app is designed to increase your productivity ')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a to-do item: ', placeholder='Add a new to-do...',
              on_change=add_todo, key='new_todo')
