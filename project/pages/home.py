import streamlit as st

st.set_page_config(page_title=f"Data Science Portfolio using Streamlit")


def app():
    intro = f"""
    Here will be looking at some examples of predictive models in supervised and un-supervised learning.
    """

    table_of_contents = f"""
    ---
    - Supervised Learning Examples:
    - Unsupervised Learning Examples:
    """

    st.write(
        """
        # Data Science Portfolio Website using Streamlit! 👋
        """
    )
    st.write(intro)
    st.write(table_of_contents)
