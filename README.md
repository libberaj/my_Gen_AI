Here's the README file with specific instructions for installing the required modules using `pip`:

# Langchain Demo with Mixtral API

## Overview

This Streamlit application demonstrates how to integrate the Mixtral API with the Langchain framework to provide a chat interface and analytics dashboard. The app uses the `ChatGroq` model for generating responses and performs text analysis using SpaCy.

## Features

- **Chat Interface**: Ask questions and get instant responses from the Mixtral API.
- **Chat History**: View previous interactions in the chat history.
- **Analytics Dashboard**: Analyze response times and text statistics, including word count and stop words.

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Modules**

   Install the required Python packages using `pip`:

   ```bash
   pip install streamlit plotly pandas spacy python-dotenv langchain-groq langchain-core
   ```

4. **Download SpaCy Model**

   Download the SpaCy English model `en_core_web_sm`:

   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Set Up Environment Variables**

   Create a `.env` file in the project root and add your GROQ API key:

   ```dotenv
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Replace `your_groq_api_key_here` with your actual GROQ API key.

## Running the Application

Run the Streamlit application using the following command:

```bash
streamlit run app.py
```

Where `app.py` is the filename of your Streamlit script.

## Code Overview

- **Imports**: The script imports necessary libraries and modules.
- **Environment Variables**: Loaded from `.env` file and used to configure the API key.
- **SpaCy Model**: Loaded for text processing and analysis.
- **Streamlit Interface**: Contains two main pages:
  - **Chat**: For interacting with the Mixtral API and viewing chat history.
  - **Show Analytics**: For displaying analytics related to response times and text statistics.

## Modules to Download

Here are the modules you need to install for this project:

- **`streamlit`**: For creating the web app interface.
- **`plotly`**: For interactive plots and charts.
- **`pandas`**: For data manipulation and analysis.
- **`spacy`**: For natural language processing tasks.
- **`python-dotenv`**: For loading environment variables from a `.env` file.
- **`langchain-groq`**: For interacting with the Mixtral API.
- **`langchain-core`**: For prompt templates and output parsing.

## Getting GROQ API Key

To obtain a GROQ API key, follow these steps:

1. **Sign Up**: Go to the [GROQ website](https://groq.com/) and sign up for an account.
2. **API Key**: Once logged in, navigate to the API section of your account dashboard.
3. **Generate Key**: Follow the instructions to generate and copy your API key.
4. **Add Key**: Paste your API key into the `.env` file as described above.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Langchain**: For providing the framework to integrate with language models.
- **Mixtral API**: For offering advanced conversational AI capabilities.
- **SpaCy**: For powerful natural language processing tools.
- **Plotly**: For creating interactive visualizations.

