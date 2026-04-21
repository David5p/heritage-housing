import streamlit as st


class MultiPage:
    """Handles multi-page navigation for the Streamlit app."""

    def __init__(self, app_name):
        self.app_name = app_name
        self.pages = []

        st.sidebar.title(self.app_name)
        self.selection = None

    def add_page(self, title, func):
        """
        Adds a page to the multipage app.
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Displays sidebar navigation and runs the selected page.
        """
        page_titles = [page["title"] for page in self.pages]

        self.selection = st.sidebar.radio("Go to", page_titles)

        for page in self.pages:
            if page["title"] == self.selection:
                page["function"]()
