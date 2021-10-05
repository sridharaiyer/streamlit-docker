import streamlit as st

from project.demos import counter, tic_tac_toe


def app():
    st.write(
        """
        # Try out Session State!

        One of the most highly requested Streamlit features is finally here! Session 
        state allows you to preserve information throughout a browser session. 
        Below are some ideas for how to use it. 
        
        More info in the [blog post](https://blog.streamlit.io/session-state-for-streamlit/).
        """
    )

    st.write("---")
    counter.show()
    st.caption(
        "[View code](https://github.com/streamlit/release-demos/blob/0.84/0.84/demos/counter.py)"
    )

    st.write("---")
    tic_tac_toe.show()
    st.caption(
        "[View code](https://github.com/streamlit/release-demos/blob/0.84/0.84/demos/tic_tac_toe.py)"
    )
