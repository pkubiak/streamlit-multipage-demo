import streamlit as st


st.header(view)

if st.button("Hello"):
    st.warning("⚠")


if st.button("Hello2"):
    st.success("⚠")

for i in ["🐕 Dog 0", "🐕 Dog 1", "🐈 Cat 0", "🐈 Cat 1", "🐈 Cat 2"]:
    if st.button(f'Go to "{i}"'):
        st.experimental_set_query_params(view=i)
        st.experimental_rerun()