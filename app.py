import streamlit as st
from transformers import pipeline
from transformers import AutoTokenizer
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
tokenizer = AutoTokenizer.from_pretrained(
    "sshleifer/distilbart-cnn-12-6"
)
def split_text(text, max_tokens=900):
    sentences = text.replace("\n", " ").split(". ")
    chunks = []
    current_chunk = []
    current_tokens = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        sentence_tokens = len(tokenizer.encode(sentence))

        if current_chunk and current_tokens + sentence_tokens > max_tokens:
            chunks.append(". ".join(current_chunk))
            current_chunk = []
            current_tokens = 0

        current_chunk.append(sentence)
        current_tokens += sentence_tokens

    if current_chunk:
        chunks.append(". ".join(current_chunk))

    return chunks

st.write(
    "Welcome! Turn your long study notes "
    "into simple summaries."
)

uploaded_file = st.file_uploader(
    "Or upload your notes (TXT or PDF):",
    type=["txt", "pdf"]
)

pasted_notes = st.text_area(
    "Or paste your study notes here:",
    height=250,
    placeholder="Enter your notes here..."
)

notes = pasted_notes

if uploaded_file is not None:
    if uploaded_file.name.lower().endswith(".txt"):
        notes = uploaded_file.getvalue().decode("utf-8", errors="replace")
    elif uploaded_file.name.lower().endswith(".pdf"):
        from pypdf import PdfReader
        import io

        pdf_reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
        notes = "\n".join(
            page.extract_text() or "" for page in pdf_reader.pages
        )

summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Long"]
)


if st.button("Summarize Notes"):
    if notes.strip():
        try:
            length_settings = {
                "Short": {"max_length": 60, "min_length": 10},
                "Medium": {"max_length": 130, "min_length": 30},
                "Long": {"max_length": 200, "min_length": 50},
            }

            chunks = split_text(notes)
            summaries = []

            with st.spinner("Generating your summary..."):
                for chunk in chunks:
                    result = summarizer(
                        chunk,
                        **length_settings[summary_length],
                        do_sample=False,
                        truncation=True
                    )
                    summaries.append(result[0]["summary_text"])

            summary = "\n\n".join(summaries)

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
        st.warning("Please paste or upload your notes first.")
