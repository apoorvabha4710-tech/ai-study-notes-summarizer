import streamlit as st
from transformers import pipeline
st.title("📚 AI Study Notes Summarizer")
with st.sidebar:
    st.header("About")
    st.write("Turn long study notes into simple summaries.")
    st.write("Choose a summary length and download your result.")
@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

summarizer = load_summarizer()

st.write(
    "Welcome! Turn your long study notes "
    "into simple summaries."
)

notes = st.text_area(
    "Paste your study notes here:",
    height=250,
    placeholder="Enter your notes here..."
)
summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Long"]
)

if st.button("Summarize Notes"):
    if notes.strip():
        try:
            with st.spinner("Generating your summary..."):
                length_settings = {
                    "Short": {"max_length": 60, "min_length": 10},
                    "Medium": {"max_length": 130, "min_length": 30},
                    "Long": {"max_length": 200, "min_length": 50},
                }

                result = summarizer(
                    notes,
                    **length_settings[summary_length],
                    do_sample=False,
                    truncation=True
                )

            
            summary = result[0]["summary_text"]

            st.subheader("Your Summary")
            st.write(summary)

            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="study_summary.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please paste your notes first.")

        
