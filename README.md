# QA_FlanT5_Ingestion

👋 Welcome to the QA_FlanT5_Ingestion project! 🤖


FLAN-T5 is a Large Language Model open sourced by Google under the Apache license at the end of 2022. It is available in different sizes - see the model card. 🤖

🔗 FLAN-T5 Model

In this implementation, I have built a Question Answering System to work with various types of Files and ingest them into Chroma DB to retrieve answers from those documents. Please keep the documents in the data directory. 📂


🚀 Usage
  Run the following command to ingest the data files into the database:
  python ingest.py
  Once the ingestion process is complete, you can use the main.py script to search for answers in the ingested documents.
  Provide the path to the data directory as an argument when running main.py:


💡 Features
  Utilizes FLAN-T5 Large Language Model for question answering
  Ingests various types of files (e.g., PDFs, text files) into a database
  Provides fast response times (approximately 12 seconds)
  Supports zero/few-shot learning for answering questions related to specific industries or subjects
  Can be used offline without requiring internet access
  Minimal hardware requirements for local deployment

  
🔍 Improvement Scope
  Performance and answer length can be improved further
  Add support for more file formats
  Integrate with other models or techniques for enhanced performance
  No Hugging Face API token is required for this implementation 🔒

  
🤝 Contributions
  Contributions are welcome! Feel free to fork, modify, and submit pull requests with your improvements or suggestions.


👍 Acknowledgments
  Many thanks to the developers of FLAN-T5 and the Hugging Face Transformers library for their outstanding work. 🙏

 

So, what are you waiting for? 🤔 Dive in and start exploring the QA_FlanT5_Ingestion project today! 🚀
