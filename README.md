# QA_FlanT5_Ingestion

👋 Welcome to the QA_FlanT5_Ingestion project! 🤖


FLAN-T5 is a Large Language Model open sourced by Google under the Apache license at the end of 2022. It is available in different sizes - see the model card. 🤖

🔗 [FLAN-T5 Model](https://huggingface.co/google/flan-t5-large)

Built with [LangChain](https://github.com/hwchase17/langchain), [Chroma](https://www.trychroma.com/) and [SentenceTransformers](https://www.sbert.net/) 

In this implementation, Built a Question Answering System to work with various types of Files and ingest them into Chroma DB to retrieve answers from those documents. 



🚀 Usage

  - 100% private, no data leaves your execution environment at any point. You can ingest documents and ask questions without an internet connection!
  
  - Once the ingestion process is complete, you can use the main.py script to search for answers in the ingested documents.
  
  - CPU friendly

  - No Token required

  - Open Source



💡 Features

  - Utilizes FLAN-T5 Large Language Model for question answering
  
  - Ingests various types of files (e.g., PDFs, text files) into a database
  
  - Provides fast response times (approximately 12 seconds for 1 file)
  
  - Supports zero/few-shot learning for answering questions related to specific industries or subjects
  
  - Can be used offline without requiring internet access
  
  - Minimal hardware requirements for local deployment we can run on commerical CPUs

  - No Hugging Face API token is required for this implementation  


  
 🔍 Improvement Scope

  - Performance and answer length can be improved further
  
  - Add support for more file formats
  
  - Integrate with other models or techniques for enhanced performance

  - GPU support

  - Will try with Flan T5 XXL model 
 
  
🤝 Contributions

  - Contributions are welcome! Feel free to fork, modify, and submit pull requests with your improvements or suggestions.



👍 Acknowledgments

  - Many thanks to the developers of FLAN-T5 and the Hugging Face Transformers library for their outstanding work. 🙏


So, what are you waiting for? 🤔 Dive in and start exploring the QA_FlanT5_Ingestion project today! 🚀



### QA FlanT5 Ingestion on Local Machine with Conda 🐳💻

Here are the implementation steps for QA FlanT5 Ingestion on a local machine using Conda for a smooth experience:

1. 🔧 Install Conda

Download and install Anaconda from the official website and choose the appropriate version (Anaconda or Miniconda) based on your system architecture (Windows, macOS, or Linux). Follow the installation instructions.

2. 📥 Clone the Repository

Open a terminal or command prompt, navigate to the directory where you want to clone the repository, and run the following command to clone the repository:
```bash
git clone https://github.com/pruthviishere/QA_FlanT5_Ingestion.git
```
3. 🔧 Create a Conda Environment

Open a terminal or command prompt, run the following command to create a new Conda environment:
```bash
conda create --name qa-flan-t5 python=3.10
```
This will create a new environment named "qa-flan-t5" with Python 3.10 as the interpreter.

4. 🔁 Activate the Conda Environment

Run the following command to activate the environment:
```bash
conda activate qa-flan-t5
```
5. 📦 Install Dependencies

Run the following command to install the dependencies listed in the `requirement.txt` file:
```bash
pip install -r requirement.txt
```
6. 📝 Keep Documents in the Data Folder

Create a folder named "data" in the root directory of the cloned repository and place your documents in this folder.

7. 🤖 Run ingest.py

Run the following command to ingest the documents:
```python
python ingest.py
```
8. 🚀 Run main.py

Run the following command to start the QA FlanT5 and ask questions:
```python
python main.py
```

That's it! You have successfully set up QA FlanT5 Ingestion on your local machine using Conda. 🎉
