from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI

import yaml
from jinja2 import Environment, FileSystemLoader
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

def create_prompt_from_template():
    with open("macros.yml") as f:
        vars = yaml.safe_load(f,)

        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("prompt_template.md")

        # Render and save
        output = template.render(vars)
        with open("prompt.md", "w") as f:
            f.write(output)

if __name__ == "__main__":
    create_prompt_from_template()