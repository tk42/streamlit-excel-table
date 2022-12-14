import os
from typing import List, Dict
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = not ("TERM_PROGRAM" in os.environ and os.environ["TERM_PROGRAM"] == "vscode")

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "table",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("table", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def Table(
    data: List[Dict],
    columns: List[Dict] = None,
    key: str = None,
    sortable: bool = False,
    filterable: bool = False,
    **kwargs,
) -> None:
    """Create a new instance of "Table".

    Parameters
    ----------
    data: List[Dict]
        Display data
        {"id": "hoge", "x": 5.77, "y": 8.85, "color": "red"},

    Returns
    -------
    None

    """

    # All data must have the same keys.
    header = data[0].keys()
    for i, d in enumerate(data):
        assert header == d.keys(), f"Index {i} {d.keys()} is not same with {header}"

    columns = [{"name": k} for k in header] if columns is None else columns

    options = {"sortable": False, "filterable": False}
    if sortable:
        options["sortable"] = True
    if filterable:
        options["filterable"] = True

    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(data=data, columns=columns, key=key, options=options, **kwargs)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run st_excel_table/__init__.py`
if not _RELEASE:
    import streamlit as st

    st.title("Streamlit-Excel-Table")

    data = [
        {"id": "hoge", "x": 5.77, "y": 8.85, "color": "red"},
        {"id": "hogedb", "x": 15.77, "y": 18.85, "color": "red"},
        {"id": "hogeba", "x": 25.77, "y": 28.85, "color": "red"},
        {"id": "hogeas", "x": 35.77, "y": 38.85, "color": "red"},
    ]

    Table(data)
