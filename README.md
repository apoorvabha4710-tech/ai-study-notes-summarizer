# 📚 AI Study Notes Summarizer

An AI-powered web application that turns long study notes into simple, easy-to-understand summaries.

## Features

- Generate summaries using a locally running AI model.
- Choose short, medium, or long summaries.
- Download summaries as text files.
- Simple, user-friendly interface built with Streamlit.

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
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