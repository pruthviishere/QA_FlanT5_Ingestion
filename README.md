# QA_FlanT5_Ingestion


FLAN-T5 is a Large Language Model open sourced by Google under the Apache license at the end of 2022. It is available in different sizes - see the model card.
https://huggingface.co/google/flan-t5-large

In this implementation I have builed a Qeustion Answering System to work with various types of Files to ingest into chroma db and get answers from those documents.keep docs in data dir.
once you run ingest data will be persistent in db dir. main.py calls this dir to get search for answers.
we are usinng T5 tokenizer and for question embbedding we are using "all-MiniLM-L6-v2" .
as this is flan t5 model is will only answer from provided documents only.so its zero/Few shot model. for this pre trained model we can provide any txt document releted to any specific industry or subject.and this will provide you answers.
once model is downloaded on machine we can use it offline without requiring and internet such that the data will be safe.we can run this locally with minimun hardware as compared to other models .
this is faster generally gives response in 12 seconds. there is a scope to improve accuracy and answer length.
we do not require any huggingface api token.
