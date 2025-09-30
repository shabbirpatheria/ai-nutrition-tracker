from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI

import getpass
import os

load_dotenv(override=True)

if "AZURE_OPENAI_API_KEY" not in os.environ:
    print("Please set the AZURE_OPENAI_API_KEY environment variable.")
if "AZURE_OPENAI_ENDPOINT" not in os.environ:
    print("Please set the AZURE_OPENAI_ENDPOINT environment variable.")
if "AZURE_OPENAI_DEPLOYMENT_NAME" not in os.environ:
    print("Please set the AZURE_OPENAI_DEPLOYMENT_NAME environment variable.")
if "AZURE_OPENAI_API_VERSION" not in os.environ:
    print("Please set the AZURE_OPENAI_API_VERSION environment variable.")

llm = AzureChatOpenAI(
    azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)

