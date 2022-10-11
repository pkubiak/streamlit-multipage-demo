import streamlit as st

st.set_page_config(page_title=f"My Dashboard", page_icon="🤣")

with open("style.css") as file:
    STYLE = file.read()

MENU = [
    "",
    ("😂 About us", "info.py"),
    ("😍 Hello World", "info.py"),

    "About Dogs",
    *[(f"🐕 Dog {i}", "dog.py") for i in range(2)],
    
    "About Cats",
    *[(f"🐈 Cat {i}", "cat.py") for i in range(3)],

    "",
    ("🔢 Statistics", "info.py")
]


mapping = {"Error": (None,"error.py")}
with st.sidebar:
    st.title("My Dashboard")
    idx = 0 
    with st.container():
        for item in MENU:
            if isinstance(item, str):
                st.header(item)
            else:
                title, link = item
                if st.button(title):
                    st.experimental_set_query_params(view=title)
                mapping[title] = idx, link
            idx += 1

    st.markdown(f"<style>{STYLE}</style>", unsafe_allow_html=True)

    params = st.experimental_get_query_params()
    st.experimental_set_query_params(**params)

    view = None
    if "view" in params:
        view = params["view"][0]
        if view not in mapping:
            view = "Error"
    else:
        view = "😂 About us"
        st.experimental_set_query_params(view=view)

    focus_idx, focus_link = mapping[view]

    # Highlight current view in menu
    if focus_idx:
        st.markdown(f'<style>section  [data-testid="stVerticalBlock"] [data-testid="stVerticalBlock"] > div:nth-child({focus_idx+1}) button {{background: rgba(151, 166, 195, 0.15);}}</style><hr/>', unsafe_allow_html=True)



with open(f"views/{focus_link}", encoding="utf-8") as file:
    exec(file.read(), dict(view=view))