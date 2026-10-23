# AI Study Notes Summarizer

An AI-powered application that transforms long study notes into shorter, easier-to-understand summaries.

**🚀 Live Demo:** [Try the app](https://apoorvabha4710-tech-ai-study-notes-summarizer-app-iykc5p.streamlit.app/)

## Features

- Summarizes study notes using an AI model
- Upload notes from TXT files
- Upload notes from PDF files
- Paste notes directly into the app
- Choose short, medium, or long summaries
- Download summaries as text files
- Simple, user-friendly Streamlit interface

## Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- DistilBART summarization model

## Installation

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

The first run downloads the AI model, so an internet connection is required. After downloading, the model runs locally.

## Usage

1. Paste your study notes into the text box.
2. Choose a summary length.
3. Click **Summarize Notes**.
4. Download your summary as a text file.

## App Screenshot

![AI Study Notes Summarizer](app-screenshot.png)
