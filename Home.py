import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("World City — Home")
st.write(
    """
    Welcome to the World City Streamlit app.
    
    Use the button below to open the app page (app.py) that you've placed inside the `pages/` folder.
    """
)

def go_to_app():
    # Try to navigate to the page by setting the query param Streamlit uses for multipage navigation,
    # then force a rerun. If that doesn't work (different Streamlit versions / hosting), the fallback
    # link below can be used.
    try:
        st.experimental_set_query_params(page="app")
        st.experimental_rerun()
    except Exception:
        st.warning("Automatic navigation failed — use the link below to open the app page manually.")

if st.button("Open App"):
    go_to_app()

st.markdown("---")
st.markdown("If the button doesn't navigate, open the app page manually:")
st.markdown("[Open App Page](/?page=app)")