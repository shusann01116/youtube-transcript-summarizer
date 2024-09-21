# YOUTUBE TRANSCRIPT SUMMERIZER

This project summarizes YouTube transcripts using OpenAI's GPT-4o-mini model. It takes the user's input and returns a summary of approximately 500 characters. The summary starts with bullet points and ends with a conclusion.

## Features

- Summarizes YouTube transcripts in Japanese by default.
- Uses OpenAI's GPT-4o-mini model for generating summaries by default.
- Easy setup and usage with provided Makefile.

## Requirements

- Python 3.x
- OpenAI API Key

## Installation

1. Clone the repository.
2. Run `make setup` to install dependencies.
3. Fill OPENAI_API_KEY in `.env`. (See the official [doc](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) for the API Key)
4. Run `make run` or `python main.py` to run the script.
