import streamlit as st
import boto3
from botocore.exceptions import ClientError

# AWS Region
REGION = "us-east-1"

# Your Knowledge Base ID
KNOWLEDGE_BASE_ID = "TGDRD32SR0"

# Initialize Bedrock client
bedrock_agent_runtime = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)

# Streamlit UI
st.title("AWS Knowledge Assistant")
st.write("Ask questions about AWS documentation")

query = st.text_input("Ask your question")

if st.button("Ask"):
    if query:
        try:
            response = bedrock_agent_runtime.retrieve_and_generate(
                input={
                    "text": query
                },
                retrieveAndGenerateConfiguration={
                    "type": "KNOWLEDGE_BASE",
                    "knowledgeBaseConfiguration": {
                        "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                        "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-haiku-20240307-v1:0",
                        "retrievalConfiguration": {
                            "vectorSearchConfiguration": {
                                "numberOfResults": 5
                            }
                        }
                    }
                }
            )

            answer = response["output"]["text"]

            st.write("### Answer")
            st.write(answer)

        except ClientError as e:
            st.error(f"AWS Error: {e}")

        except Exception as e:
            st.error(f"Error: {e}")