import streamlit as st
import pandas as pd

# Constants
FIGHTS = [
    {"Fight": "Fight 1", "Fighter A": "John Doe", "Fighter B": "Jane Smith"},
    {"Fight": "Fight 2", "Fighter A": "Alex Johnson", "Fighter B": "Sam Lee"}
]

CATEGORIES = ['Strikes', 'Knockdowns', 'Grappling', 'Aggressiveness', 'Area Control', 'Defense', 'Illegal Moves', 'Sportsmanship']
TIEBREAKERS = ['Number of Knockdowns', 'Effective Damage', 'Takedowns', 'Better Defense', 'Attempts to Finish']

def main():
    st.set_page_config(page_title="MMA Fight Scorecard", page_icon="🥊", layout="wide")
    st.title("MMA Fight Scorecard App")

    page = st.sidebar.selectbox("Choose a page", ["Home", "Score Fights", "Results", "About"])

    if page == "Home":
        display_home()
    elif page == "Score Fights":
        score_fights()
    elif page == "Results":
        display_results()
    elif page == "About":
        display_about()

    st.markdown("---")
    st.write("Made with ❤️ using Streamlit")

def display_home():
    st.header("Welcome to the MMA Fight Scorecard")
    st.write("Here you can score each fight in an MMA event considering various aspects like effective striking, grappling, aggressiveness, area control, defense, and more. Track your scores and compare them with official results or other viewers.")

def score_fights():
    st.header("Score the Fights")

    if 'scores' not in st.session_state:
        st.session_state['scores'] = {}

    for fight in FIGHTS:
        score_fight(fight)

    if st.button("Submit Scores"):
        st.success("Scores submitted successfully!")

def score_fight(fight):
    fight_name = fight['Fight']
    fighter_a, fighter_b = fight['Fighter A'], fight['Fighter B']
    st.subheader(f"{fight_name}: {fighter_a} vs. {fighter_b}")

    if fight_name not in st.session_state['scores']:
        st.session_state['scores'][fight_name] = {'A': {}, 'B': {}}

    for category in CATEGORIES:
        score_category(fight_name, fighter_a, fighter_b, category)

    # Round-by-Round scoring
    st.session_state['scores'][fight_name]['Round Score'] = st.selectbox(f"Round Score for {fight_name}", ['10-9', '10-8', '10-10'], key=f"round_{fight_name}")

    # Tiebreaker criteria
    if st.checkbox("Was this fight a draw?", key=f"draw_{fight_name}"):
        for tiebreaker in TIEBREAKERS:
            st.session_state['scores'][fight_name][tiebreaker] = st.radio(f"{tiebreaker} for {fight_name}", [fighter_a, fighter_b])

def score_category(fight_name, fighter_a, fighter_b, category):
    col1, col2 = st.columns(2)
    with col1:
        st.session_state['scores'][fight_name]['A'][category] = st.slider(f"{fighter_a} - {category}", 0, 10, 0)
    with col2:
        st.session_state['scores'][fight_name]['B'][category] = st.slider(f"{fighter_b} - {category}", 0, 10, 0)

def display_results():
    st.header("Fight Results")

    if 'scores' not in st.session_state or not st.session_state['scores']:
        st.write("No scores recorded yet.")
    else:
        results = []
        for fight_name, scores in st.session_state['scores'].items():
            fight_data = {'Fight': fight_name}
            for fighter in ['A', 'B']:
                fight_data[f"Fighter {fighter} Scores"] = ', '.join([f"{k}: {v}" for k, v in scores[fighter].items()])
            fight_data['Round Score'] = scores['Round Score']
            if 'Number of Knockdowns' in scores:
                fight_data['Tiebreaker'] = ', '.join([f"{k}: {v}" for k, v in scores.items() if k in TIEBREAKERS])
            results.append(fight_data)

        df = pd.DataFrame(results)
        st.dataframe(df)

def display_about():
    st.header("About")
    st.write("""
    This app allows viewers to score MMA fights in real-time or retrospectively. It considers:
    - **Effective Striking/Grappling**: Strikes, knockdowns, grappling control, etc.
    - **Effective Aggressiveness**: Attempts to finish the fight.
    - **Fighting Area Control**: Cage/Octagon control, positioning.
    - **Defense**: Evasion, blocking, neutralizing opponent's offense.
    - **Other Considerations**: Illegal moves, sportsmanship, round-by-round scoring, and tiebreakers.
    """)

if __name__ == "__main__":
    main()
