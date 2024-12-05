import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="MMA Fight Scorecard", page_icon="🥊", layout="wide")
    st.title("MMA Fight Scorecard App")

    page = st.sidebar.selectbox("Choose a page", ["Home", "Score Fights", "Results", "About"])

    if page == "Home":
        st.header("Welcome to the MMA Fight Scorecard")
        st.write("""
        Here you can score each fight in an MMA event considering various aspects like effective striking, grappling, aggressiveness, area control, defense, and more. Track your scores and compare them with official results or other viewers.
        """)

    elif page == "Score Fights":
        score_fights()

    elif page == "Results":
        display_results()

    elif page == "About":
        st.header("About")
        st.write("""
        This app allows viewers to score MMA fights in real-time or retrospectively. It considers:
        - **Effective Striking/Grappling**: Strikes, knockdowns, grappling control, etc.
        - **Effective Aggressiveness**: Attempts to finish the fight.
        - **Fighting Area Control**: Cage/Octagon control, positioning.
        - **Defense**: Evasion, blocking, neutralizing opponent's offense.
        - **Other Considerations**: Illegal moves, sportsmanship, round-by-round scoring, and tiebreakers.
        """)

    st.markdown("---")
    st.write("Made with ❤️ using Streamlit")

def score_fights():
    st.header("Score the Fights")
    fights = [
        {"Fight": "Fight 1", "Fighter A": "John Doe", "Fighter B": "Jane Smith"},
        {"Fight": "Fight 2", "Fighter A": "Alex Johnson", "Fighter B": "Sam Lee"}
    ]

    if 'scores' not in st.session_state:
        st.session_state['scores'] = {}

    for fight in fights:
        fight_name = fight['Fight']
        fighter_a = fight['Fighter A']
        fighter_b = fight['Fighter B']

        st.subheader(f"{fight_name}: {fighter_a} vs. {fighter_b}")

        # Initialize scores for each fighter
        if fight_name not in st.session_state['scores']:
            st.session_state['scores'][fight_name] = {'A': {}, 'B': {}}

        # Scoring categories
        categories = [
            'Strikes', 'Knockdowns', 'Grappling', 'Aggressiveness', 'Area Control', 'Defense', 
            'Illegal Moves', 'Sportsmanship'
        ]

        for category in categories:
            col1, col2 = st.columns(2)
            with col1:
                score_a = st.slider(f"{fighter_a} - {category}", 0, 10, 0)
            with col2:
                score_b = st.slider(f"{fighter_b} - {category}", 0, 10, 0)

            st.session_state['scores'][fight_name]['A'][category] = score_a
            st.session_state['scores'][fight_name]['B'][category] = score_b

        # Round-by-Round scoring
        round_score = st.selectbox(f"Round Score for {fight_name}", options=['10-9', '10-8', '10-10'], key=f"round_{fight_name}")
        st.session_state['scores'][fight_name]['Round Score'] = round_score

        # Tiebreaker criteria (if applicable)
        if st.checkbox("Was this fight a draw?", key=f"draw_{fight_name}"):
            tiebreakers = [
                'Number of Knockdowns', 'Effective Damage', 'Takedowns', 'Better Defense', 
                'Attempts to Finish'
            ]
            for tiebreaker in tiebreakers:
                st.session_state['scores'][fight_name][tiebreaker] = st.radio(f"{tiebreaker} for {fight_name}", options=[fighter_a, fighter_b])

    if st.button("Submit Scores"):
        st.success("Scores submitted successfully!")

def display_results():
    st.header("Fight Results")

    if 'scores' not in st.session_state or not st.session_state['scores']:
        st.write("No scores recorded yet.")
    else:
        results = []
        for fight, scores in st.session_state['scores'].items():
            fight_data = {'Fight': fight}
            for fighter in ['A', 'B']:
                fight_data[f"Fighter {fighter} Scores"] = ', '.join([f"{k}: {v}" for k, v in scores[fighter].items()])
                fight_data[f"Round Score"] = scores['Round Score']
                if 'Number of Knockdowns' in scores:
                    fight_data['Tiebreaker'] = ', '.join([f"{k}: {v}" for k, v in scores.items() if k in ['Number of Knockdowns', 'Effective Damage', 'Takedowns', 'Better Defense', 'Attempts to Finish']])
            results.append(fight_data)

        df = pd.DataFrame(results)
        st.dataframe(df)

if __name__ == "__main__":
    main()
