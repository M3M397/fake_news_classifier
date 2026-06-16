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
            else:
            with st.spinner("Analyzing text credibility and emotional tone..."):
                try:
                    # 1. Initialize your tools from the packages
                    keyword_scorer = KeywordScorer()
                    sentiment_analyzer = SentimentAnalyzer()
                    
                    # 2. Run the user's text through both engines
                    kw_score, kw_flags = keyword_scorer.score(input)
                    sent_results = sentiment_analyzer.analyze(input)
                    
                    # 3. Calculate a blended credibility score (60% keyword facts, 40% emotion/bias)
                    final_score = (kw_score * 0.6) + (sent_results["score"] * 0.4)
                    
                    # 4. Draw the Results Layout on the web page
                    st.markdown("---")
                    st.subheader("📊 Credibility Analysis Report")
                    
                    # 5. Show numerical metrics side-by-side in 3 columns
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric(label="Overall Credibility", value=f"{round(final_score, 1)}%")
                    with col2:
                        st.metric(label="Subjectivity (Opinion)", value=f"{round(sent_results['subjectivity'] * 100, 1)}%")
                    with col3:
                        st.metric(label="Emotional Tone Score", value=f"{sent_results['polarity']}")
                    
                    # 6. Collect and display any yellow warning boxes for the user
                    st.markdown("### 🔍 Analysis Findings")
                    all_flags = kw_flags + sent_results["flags"]
                    
                    if all_flags:
                        for flag in all_flags:
                            st.warning(flag)
                    else:
                        st.success("Clean Text! No suspicious clickbait or heavy emotional bias detected.")
                        
                except InvalidInputError as e:
                    st.error(f"Input Error: {e}")
                except Exception as e:
                    st.error(f"An unexpected error occurred during processing: {e}")

















#----------Page 2 ------------
elif select == "Sources":
    st.title("Sources")
    st.write("Browse the reputation scores used to evaluate news sources.")

# ----------Page 3 ------------

elif select == "History":
    st.title("History")
    st.write("Recent credibility checks performed.")
