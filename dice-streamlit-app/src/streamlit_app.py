import streamlit as st
from dice import roll_dice

def main():
    st.title("🎲 Dice Roller App")
    
    if st.button("Roll the Dice"):
        result = roll_dice()
        st.success(f"You rolled a {result}!")

if __name__ == "__main__":
    main()