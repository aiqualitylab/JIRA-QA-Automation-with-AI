import os
from dotenv import load_dotenv
from atlassian import Jira
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

# Load credentials and config
jira_username = os.getenv("JIRA_USERNAME")
jira_token = os.getenv("JIRA_API_TOKEN")
jira_url = os.getenv("JIRA_INSTANCE_URL")
openai_api_key = os.getenv("OPENAI_API_KEY")

# 1. Connect to Jira
jira = Jira(
    url=jira_url,
    username=jira_username,
    password=jira_token
)

# 2. Fetch Jira issue
issue_key = "KAN-1"
issue = jira.issue(issue_key)

if not issue:
    raise ValueError("❌ Failed to retrieve Jira issue KAN-1")

summary = issue["fields"].get("summary", "")
description = issue["fields"].get("description", "")
ticket_text = f"Summary: {summary}\n\nDescription: {description}"

# 3. Chunk the text
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(ticket_text)

# 4. Embed and store in FAISS (local vector DB)
embedding_model = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(chunks, embedding_model)

# 5. Retrieve most relevant chunks (simulate question)
docs = vectorstore.similarity_search("Generate testable acceptance criteria", k=3)
context = "\n\n".join([doc.page_content for doc in docs])

# 6. Generate Gherkin acceptance criteria
llm = OpenAI(temperature=0)

prompt = PromptTemplate.from_template("""
As a QA Automation Engineer, given a Jira ticket, generate Gherkin-style acceptance criteria with @positive, @negative, and @edgecase tags to cover all test scenarios.
{context}

Format:
Given ...
When ...
Then ...
""")

chain = LLMChain(llm=llm, prompt=prompt)
gherkin_output = chain.run(context=context)

# 7. Output result
print("\n✅ Generated Gherkin Acceptance Criteria:\n")
print(gherkin_output)

# 8. Export to .feature file
feature_filename = f"{issue_key}.feature"
with open(feature_filename, "w", encoding="utf-8") as f:
    f.write(f"# Jira Ticket: {issue_key}\n")
    f.write(f"# Summary: {summary}\n\n")
    f.write("Feature: Acceptance Criteria\n\n")
    f.write(gherkin_output.strip())
    f.write("\n")

print(f"\n📄 Gherkin exported to: {feature_filename}")

