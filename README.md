# OpenAI Chatbot

This project is a simple command-line chatbot application built using OpenAI's API, specifically using the `chatgpt.py` script. The chatbot is designed to handle natural language conversations, providing useful, contextually relevant responses to user inputs.

## Features

-   Interactive command-line interface.
-   Powered by OpenAI's `gpt-3.5-turbo` model by default.
-   Easy setup using an environment file for your API key.
-   Easily customizable to use other OpenAI chat models.

## Prerequisites

-   Python 3.x
-   An API key from OpenAI.

## Getting Started

Follow these steps to get the chatbot running on your local machine.

### 1. Clone the Repository

Clone this repository to your local machine. If you don't have a repository URL, you can just download the files.

```bash
# Example of cloning a repository
git clone <repository-url>
cd openai-chatbot
```

### 2. Install Dependencies

The script requires the `openai` and `python-dotenv` libraries. It's recommended to use a virtual environment. You can install them using the `requirements.txt` file.

```bash
# Install the required packages
pip install -r requirements.txt
```

### 3. Configure API Key

The application loads your OpenAI API key from a `.env` file for security.

1.  In the project's root directory (the same directory as `chatgpt.py`), create a file named `.env`.
2.  Add the following line to the `.env` file, replacing `your-openai-api-key` with your actual secret key:

    ```env
    OPENAI_API_KEY='your-openai-api-key'
    ```

## Usage

To run the chatbot, execute the `chatgpt.py` script from your terminal:

```bash
python chatgpt
```

You can now start a conversation in your terminal. To end the session, type `exit` and press Enter.

## Customization

### Changing the AI Model

By default, the chatbot uses the `gpt-3.5-turbo` model. You can easily switch to another model available to your account (e.g., `gpt-4`, `gpt-4-turbo`) by editing the `chatgpt.py` file.

Locate the `chatbot` function and change the value of the `model` parameter in the `client.chat.completions.create` call.
