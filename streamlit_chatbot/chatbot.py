# father_letter.py
import streamlit as st

st.set_page_config(page_title="Father's Day Letter", page_icon="💌")

st.title("💖 Happy Father's Day, Dad! 💖")

letter = """
Dear Dad,

On this special day, I just want to say thank you for everything you've done for me.
Your love, guidance, and strength have shaped me into who I am today.

You've been my superhero, my mentor, and my greatest supporter.
I'm truly grateful for your presence in my life.

Wishing you the happiest Father's Day!

With love,  
Your Child
"""

st.markdown(letter)

