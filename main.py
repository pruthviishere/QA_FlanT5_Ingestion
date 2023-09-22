 
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from transformers import T5Tokenizer, T5ForConditionalGeneration
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from chromadb.config import Settings
import chromadb
import argparse
import time
from transformers import pipeline
from langchain import HuggingFacePipeline
from langchain.prompts import PromptTemplate

def main():
    args = parse_arguments()
 
    target_source_chunks = 4
 
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large", device_map="cpu")

    
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    llm = HuggingFacePipeline(
        pipeline = pipe,
        model_kwargs={"temperature": 0, "max_length": 512},
    )
    #print(llm)


    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Keep the answer as concise as possible. 
    {context}
    Question: {question}
    """
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
 
    EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
   
    embeddings = HuggingFaceEmbeddings(model_name= "all-MiniLM-L6-v2")
     
    persist_directory ="db"
    CHROMA_SETTINGS = Settings(
            persist_directory=persist_directory,
            anonymized_telemetry=False
    )
    chroma_client = chromadb.PersistentClient(settings=CHROMA_SETTINGS , path=persist_directory)
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, 
                client_settings=CHROMA_SETTINGS, client=chroma_client)
    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
        # activate/deactivate the streaming StdOut callback for LLMs
    callbacks = [] if args.mute_stream else [StreamingStdOutCallbackHandler()]
    
    qa_chain = RetrievalQA.from_chain_type(   
    llm=llm,   
    chain_type="stuff",   
    retriever=retriever ,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    callbacks=callbacks,
      return_source_documents= not args.hide_source
    ) 
    while True:
        query = input("\nEnter a query: ")
        if query == "exit":
            break
        if query.strip() == "":
            continue

        # Get the answer from the chain
        start = time.time()
        res = qa_chain(query)
        answer, source_docs = res['result'], [] if args.hide_source else res['source_documents']
        end = time.time()

         
        print(f"\n> Answer (took {round(end - start, 2)} s.):")
        print(answer)
        print(f"\n Source Docs : \n",source_docs)

        
 
def parse_arguments():
    parser = argparse.ArgumentParser(description='privateGPT: Ask questions to your documents without an internet connection, '
                                                'using the power of LLMs.')
    parser.add_argument("--hide-source", "-S", action='store_true',
                        help='Use this flag to disable printing of source documents used for answers.')

    parser.add_argument("--mute-stream", "-M",
                        action='store_true',
                        help='Use this flag to disable the streaming StdOut callback for LLMs.')

    return parser.parse_args()
 
if __name__ == "__main__":
    main()
 