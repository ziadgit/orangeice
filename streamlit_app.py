import streamlit as st
import random

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return 'You win!'
    else:
        return 'Computer wins!'

st.title('Rock-Paper-Scissors Game')

user_choice = st.selectbox('Choose your option:', ['Rock', 'Paper', 'Scissors'])
if st.button('Play'):
    computer_choice = get_computer_choice()
    result = get_winner(user_choice, computer_choice)

    st.write(f'You chose: {user_choice}')
    st.write(f'The computer chose: {computer_choice}')
    st.write(f'Result: {result}')
