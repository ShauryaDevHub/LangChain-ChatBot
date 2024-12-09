# LangChain-ChatBot

This repository contains a Python script `langchain_hands_on.py`, which serves as a hands-on tutorial for demonstrating the capabilities of the LangChain library in conjunction with OpenAI's language models. It showcases various advanced features including conversation management, document embedding, retrieval-based question answering, and integrating external APIs for expanded functionalities.

## Features

- **Language Model Interaction**: Demonstrates how to instantiate and use OpenAI's GPT models for generating text based on specific prompts.
- **Prompt Management**: Utilizes LangChain's prompt templates for dynamic text generation tasks.
- **Conversation Chains**: Implements conversation chains for managing ongoing dialogues with language models.
- **Document Embedding and Retrieval**: Showcases how to create document embeddings using OpenAI's models and store/retrieve them using DeepLake.
- **Retrieval-Based QA**: Implements a retrieval-based question answering system combining language models with document retrieval.
- **External API Integration**: Demonstrates integrating Google Search API for real-time information retrieval and response generation.

## Installation

Before running the script, ensure you have Python 3.6+ installed. Then, clone this repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/langchain-hands-on.git
cd langchain-hands-on
pip install -r requirements.txt

Make sure you have the necessary API keys and tokens set as environment variables:

    OpenAI API Key (OPENAI_API_KEY)
    Activeloop Token (ACTIVELOOP_TOKEN)
    Google API Key and Custom Search Engine ID (GOOGLE_API_KEY, GOOGLE_CSE_ID)

Contributing

Contributions are welcome! If you'd like to improve the script or add more examples, please feel free to fork the repository and submit a pull request.
