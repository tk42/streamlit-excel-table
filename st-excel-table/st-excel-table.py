import streamlit as st
import streamlit.components.v1 as components

_react_excel_table = components.declare_component(
    "react_excel_table",
    url="http://localhost:3001",
)


def react_excel_table(d, c, o):
    return _react_excel_table(data=d, columns=c, options=o)


st.title("Streamlit-Excel-Table")

data = [
    {"id": "hoge", "x": 5.77, "y": 8.85, "color": "red"},
    {"id": "hogedb", "x": 15.77, "y": 18.85, "color": "red"},
    {"id": "hogeba", "x": 25.77, "y": 28.85, "color": "red"},
    {"id": "hogeas", "x": 35.77, "y": 38.85, "color": "red"},
]

columns = [
    {"name": "id"},
    {"name": "x"},
    {"name": "y"},
    {"name": "color"},
]

options = {"sortable": False, "filterable": False}

react_excel_table(data, columns, options)
