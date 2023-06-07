import streamlit as st

def main():
    # Add navigation bar
    st.markdown(
        """
        <style>
        .navbar {
            display: flex;
            background-color: #333;
            padding: 10px;
            color: #fff;
        }

        .navbar a {
            color: #fff;
            margin-right: 10px;
            text-decoration: none;
        }
        </style>
        """
        ,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </div>
        """
        ,
        unsafe_allow_html=True
    )

    # Add content based on selected page
    page = st.sidebar.radio("Navigation", ["Home", "About", "Contact"])

    if page == "Home":
        st.write("Welcome to the Home page!")
        url = st.text_input("Enter URL")
        if st.button("Submit"):
            st.write("URL submitted:", url)
    elif page == "About":
        st.write("This is the About page.")
    elif page == "Contact":
        st.write("You can reach us on the Contact page.")

if __name__ == "__main__":
    main()
