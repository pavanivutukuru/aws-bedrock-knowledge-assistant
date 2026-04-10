AWS Knowledge Assistant using Amazon Bedrock
  Project Overview

        This project is an AWS Knowledge Assistant built using Amazon Bedrock Knowledge Bases and Streamlit.
It allows users to ask questions about AWS documentation and receive AI-generated responses using Retrieval-Augmented Generation (RAG).

The system retrieves relevant information from documents stored in Amazon S3, processes them using Amazon Bedrock embeddings, and generates responses using Amazon Bedrock foundation models.

Features:

** AWS Knowledge Assistant UI using Streamlit
** Amazon Bedrock Knowledge Base integration
** Retrieval-Augmented Generation (RAG)
** Amazon Bedrock foundation models
** Amazon S3 document storage
** Vector store using Amazon S3 Vectors
** Real-time AI responses


Architecture:

User Query
    ↓
Streamlit UI
    ↓
Amazon Bedrock RetrieveAndGenerate
    ↓
Knowledge Base
    ↓
Vector Store (S3 Vectors)
    ↓
AWS Documents (S3)


Technologies Used:

-- Python
-- Streamlit
-- AWS Bedrock
-- Amazon S3
-- AWS IAM
-- Boto3


Project Structure:

aws-bedrock-knowledge-assistant/
│
├── app.py
├── requirements.txt
└── README.md

Installation:

Navigate to Project Folder
cd aws-bedrock-knowledge-assistant

Install Dependencies
pip install -r requirements.txt

Run Application
streamlit run app.py

How It Works:

1. User enters question in Streamlit UI
2. Query is sent to Amazon Bedrock
3. Bedrock retrieves relevant documents
4. AI model generates response
5. Answer displayed in UI

AWS Services Used:

1. Amazon Bedrock
2. Amazon Bedrock Knowledge Bases
3. Amazon S3
4. Amazon S3 Vector Store
5. AWS IAM

Models Used:

** Embedding Model
** Titan Embeddings G1 - Text v1.2
** Generation Model
** Claude 3 Haiku (Amazon Bedrock)

Requirements

Created a requirements.txt file:

streamlit
boto3
botocore

Output:

The application provides AI-generated answers based on AWS documentation.


Author
Pavani Vutukuru
