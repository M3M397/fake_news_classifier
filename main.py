import pandas as pd
import streamlit as st
from numpy.ma.core import size

st.set_page_config(
    page_title= "Fake News & Misinformation Classifier Tool",
    layout = "centered",
    page_icon= "🔎"
    )

#------------------Sidebar------------------------------
st.sidebar.title("Fake News & Misinformation Classifier Tool")
select = st.sidebar.radio(
    "Navigation",
    ["Detector" , "Sources" , "History"]

)


#----------Page 1 ------------
if select == "Detector":
    st.title("Check a Headline or Article.")
    st.write("Paste a news headline or article below, and get a credibility score.")
    input = st.text_area("News Headline or Article text", height = 200)
    selected_source = st.selectbox("Source" , ["Dawn News" ,"Geo News" , "Ary News" , "Bol News" , "BBC" , "Al Jazeera"])
    if st.button("Check Credibility" , type= "primary"):
        if not input or not input.strip():
            st.error("News text cannot be empty.")
        else:
            st.success("Processing...")

















#----------Page 2 ------------
elif select == "Sources":
    st.title("Sources")
    st.write("Browse the reputation scores used to evaluate news sources.")

# ----------Page 3 ------------

elif select == "History":
    st.title("History")
    st.write("Recent credibility checks performed.")
