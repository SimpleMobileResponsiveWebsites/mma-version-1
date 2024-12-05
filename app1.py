import streamlit as st
import pandas as pd

def main():
    # Set page configuration
    st.set_page_config(page_title="MMA Fight Scorecard", page_icon="🥊", layout="wide")

    # Title
    st.title("MMA Fight Scorecard App")

    # Sidebar for navigation
    page = st.sidebar.selectbox("Choose a page", ["Home", "Score Fights", "Results", "About"])

    if page == "Home":
        st.header("Welcome to the MMA Fight Scorecard")
        st.write("""
        Here you can score each fight in an MMA event, track your scores, and compare them with official results or other viewers.
        """)

    elif page == "Score Fights":
        score_fights()

    elif page == "Results":
        display_results()

    elif page == "About":
        st.header("About")
        st.write("This app allows viewers to score MMA fights in real-time or retrospectively.")

    # Footer
    st.markdown("---")
    st.write("Made with ❤️ using Streamlit")

def score_fights():
    st.header("Score the Fights")

    # Assume we have a predefined list of fights for an event
    fights = [
        {"Fight": "Fight 1", "Fighter A": "John Doe", "Fighter B": "Jane Smith"},
        {"Fight": "Fight 2", "Fighter A": "Alex Johnson", "Fighter B": "Sam Lee"}
    ]

    # State to hold scores
    if 'scores' not in st.session_state:
        st.session_state['scores'] = {}

    for fight in fights:
        fight_name = fight['Fight']
        fighter_a = fight['Fighter A']
        fighter_b = fight['Fighter B']

        st.subheader(fight_name)
        col1, col2 = st.columns(2)
        with col1:
            score_a = st.slider(f"{fighter_a} Score", 0, 10, 0)
        with col2:
            score_b = st.slider(f"{fighter_b} Score", 0, 10, 0)

        # Store scores
        st.session_state['scores'][fight_name] = {'A': score_a, 'B': score_b}

    if st.button("Submit Scores"):
        st.success("Scores submitted successfully!")

def display_results():
    st.header("Fight Results")

    if 'scores' not in st.session_state or not st.session_state['scores']:
        st.write("No scores recorded yet.")
    else:
        scores_df = pd.DataFrame.from_dict(st.session_state['scores'], orient='index')
        scores_df = scores_df.rename(columns={'A': 'Fighter A Score', 'B': 'Fighter B Score'})
        st.dataframe(scores_df)

        # Here you could add logic to compare with official scores or other viewers

if __name__ == "__main__":
    main()
