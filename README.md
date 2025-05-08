# DocuSearch

## Overview

DocuSearch is a multi-agent document search system that reads PDF files, generates text embeddings, and answers user queries using OpenAI and FAISS. It integrates advanced text processing and embedding strategies to provide accurate and context-aware responses from documents.

## Features

* Extract text from PDF files
* Split text into manageable chunks for efficient searching
* Generate embeddings using OpenAI and SentenceTransformers
* Perform similarity-based document search with FAISS
* Provide contextually accurate responses using Langchain

## Project Structure

```
.
├── main.py                 # Main script for running the chatbot
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── pdfs/                   # Directory to store PDF files
```

## Installation

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```
2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your PDF files in the `pdfs/` directory.
2. Replace the placeholder `openai_key` with your actual OpenAI API key in the code.
3. Run the main script:

   ```bash
   python main.py
   ```
4. Test the chatbot with your query:

   ```python
   query = "How do I make a file public in Amazon S3?"
   response, source = orchestrator.get_response(query)
   print(f"Response: {response}")
   print(f"Source: {source}")
   ```

## Configuration

* **OpenAI API Key**: Set your OpenAI API key in the environment variable `OPENAI_API_KEY`.
* **PDF Path**: Update the `pdf_path` variable in the script to point to the PDF file you want to search.
* **FAQ Data**: Customize the FAQ dictionary as needed.

## Dependencies

* PyPDF2
* langchain
* sentence-transformers
* openai
* scikit-learn
* faiss-cpu

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Future Improvements

* Add support for multiple PDFs
* Integrate a web front-end for a more interactive user experience
* Implement caching for faster responses
* Add support for more languages and larger models

## License

MIT License

## Contributing

Feel free to open issues, create pull requests, or reach out if you have suggestions for improvements.

## Contact

For any inquiries, please reach out via GitHub issues or direct email.

