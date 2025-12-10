# 🧪 JIRA QA Automation with AI 🐍🤖

Automatically generate BDD test scripts from JIRA stories using AI! This tool leverages OpenAI's language models and LangChain to analyze your JIRA stories and generate comprehensive Gherkin-style acceptance criteria.

## 🎯 Features

- 🤖 **AI-Powered Test Generation**: Automatically converts JIRA stories into BDD scenarios
- 📊 **Smart Context Understanding**: Uses FAISS vector database for intelligent story analysis
- 🏷️ **Auto-tagged Scenarios**: Generates `@positive`, `@negative`, and `@edgecase` scenarios
- 🔄 **Kanban Integration**: Pulls stories directly from your JIRA Kanban board
- 🧠 **LangChain Integration**: Utilizes advanced LLM capabilities for natural language processing
- 📝 **Custom Prompting**: Specialized prompts for QA-focused scenario generation

## 🤖 How It Works

1. Connects to your JIRA board and fetches story details
2. Processes story text using LangChain and embeddings
3. Stores context in FAISS vector database for semantic search
4. Uses OpenAI to generate relevant test scenarios
5. Outputs formatted Gherkin feature files

### 🔧 Technical Details

- **LangChain Components**:
  - 🔄 `LLMChain` for orchestrating the generation pipeline
  - 📝 `PromptTemplate` for structured scenario generation
  - 🎯 `OpenAIEmbeddings` for semantic text understanding
  
- **Vector Database**:
  - 📊 FAISS similarity search with cosine distance
  - 🧩 Chunk size: 500 characters with 50-character overlap
  - 🎯 Top-k retrieval (k=3) for relevant context

- **OpenAI Integration**:
  - 🤖 Model: Uses latest GPT for generation
  - 🎛️ Temperature: 0 (for consistent output)
  - 📝 Custom prompt engineering for QA focus

### ⚙️ Advanced Configuration

You can customize the behavior by modifying these parameters in `main.py`:

```python
# Vector DB Configuration
CHUNK_SIZE = 500           # Adjust for longer/shorter stories
CHUNK_OVERLAP = 50         # Increase for better context continuity
TOP_K_RESULTS = 3         # Number of similar chunks to consider

# LangChain Configuration
TEMPERATURE = 0           # 0 for consistent, up to 0.7 for creative
MAX_TOKENS = 1000        # Adjust based on scenario complexity
TEMPLATE_VERSION = "QA"   # Choose different prompt templates

# JIRA Integration
BATCH_SIZE = 10          # Number of stories to process at once
FIELDS = ["summary", "description", "acceptance_criteria"]
```

#### 🎛️ Available Prompt Templates:
- `QA`: Standard test scenario generation
- `API`: API testing focused scenarios
- `UI`: User interface testing scenarios
- `SECURITY`: Security testing scenarios

#### 🔋 Performance Optimization:
- Enable batch processing for multiple stories
- Use GPU acceleration for FAISS (install `faiss-gpu`)
- Cache embeddings for frequently accessed stories
- Implement parallel processing for large backlogs

## 📁 Project Structure

```bash
├── KAN-1.feature    # 📄 Feature file containing BDD scenarios
└── main.py         # 🚀 Python script for running BDD tests
```

## ✅ Prerequisites

Make sure you have the following installed:

- 🐍 Python 3.x
- 🔑 OpenAI API key
- 🎫 JIRA API credentials

### 🔐 Getting Your API Keys

#### OpenAI API Key
1. Go to [OpenAI API Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new secret key
5. Copy and save it securely (you won't be able to see it again!)

#### JIRA API Token
1. Log in to [Atlassian Account Settings](https://id.atlassian.com/manage/api-tokens)
2. Click "Create API Token"
3. Give it a meaningful label (e.g., "QA-Automation")
4. Copy and save the token securely

Your JIRA credentials will include:
- 👤 Username: Your Atlassian account email
- 🔑 API Token: The token you just created
- 🌐 Instance URL: Your JIRA instance URL (e.g., `https://your-domain.atlassian.net`)

## 📦 Dependencies

You can install all required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install the following packages:
- 📝 `python-dotenv` - For environment variables management
- 🔌 `atlassian-python-api` - For JIRA integration
- 🧠 `langchain` - For LLM operations
- 🤖 `openai` - For OpenAI integration
- 🔍 `faiss-cpu` - For vector similarity search
- 🧪 `behave` - For BDD testing

Alternatively, you can install packages individually:

```bash
pip install python-dotenv         # For environment variables
pip install atlassian-python-api # For JIRA integration
pip install langchain           # For LLM operations
pip install openai              # For OpenAI integration
pip install faiss-cpu           # For vector similarity search
pip install behave              # For BDD testing
```

## � Environment Setup

Create a `.env` file in the root directory with the following variables:

```env
JIRA_USERNAME=your_jira_username
JIRA_API_TOKEN=your_jira_api_token
JIRA_INSTANCE_URL=your_jira_url
OPENAI_API_KEY=your_openai_api_key
```

## ⚙️ Setup Instructions

1. 🔁 Clone the repository:
```bash
git clone https://github.com/aiqualitylab/jira-qa-automation.git
cd jira-qa-automation
```

2. ✅ Install Behave:
```bash
pip install behave
```

🗂️ Organize your feature files inside a `features/` folder if your project grows.

## 🧾 About the Feature Files

The AI automatically generates feature files with comprehensive test coverage:

- ✅ **Positive Scenarios**: Happy path test cases
- ❌ **Negative Scenarios**: Error handling and invalid inputs
- 🔄 **Edge Cases**: Boundary conditions and special situations
- 📝 **Clear Documentation**: AI-generated descriptions for each scenario

### 🤖 AI-Generated Features

The system uses:
- 📊 **FAISS Vector DB**: For semantic similarity search in story content
- 🔍 **LangChain**: For advanced prompt engineering and context management
- 🧠 **OpenAI**: For natural language understanding and scenario generation

### 📚 Example AI-Generated Scenarios for Different Story Types:

#### 1️⃣ E-Commerce Story (KAN-1)
```gherkin
Feature: Shopping Cart Checkout Process

  @positive
  Scenario: Successful checkout with valid payment
    Given the user has items in their shopping cart
    When they proceed to checkout
    And enter valid payment details
    Then the order should be confirmed
    And they should receive a confirmation email

  @negative
  Scenario: Checkout with insufficient funds
    Given the user has items in their shopping cart
    When they proceed to checkout
    And enter payment details with insufficient funds
    Then they should see an "Insufficient Funds" error
    And the order should not be processed
```

## 🤝 Contributing

We welcome improvements and new scenarios!

1. 🍴 Fork the repository

2. 🌿 Create a new branch:
```bash
git checkout -b feature/my-new-feature
```

3. 💾 Commit your changes:
```bash
git commit -m "Add new test scenario"
```

4. 🚀 Push your branch:
```bash
git push origin feature/my-new-feature
```

5. 📬 Open a Pull Request

## 📄 License

📜 Open for changes

## ❗ Troubleshooting Guide

### Common Issues and Solutions

1. **🔑 API Key Issues**:
   - Error: "OpenAI API key not found"
     - ✅ Check if `.env` file exists in root directory
     - ✅ Verify OPENAI_API_KEY is correctly set
     - ✅ Ensure no spaces around the API key

2. **🔌 JIRA Connection**:
   - Error: "JIRA authentication failed"
     - ✅ Verify JIRA credentials in `.env`
     - ✅ Check if JIRA URL includes `https://`
     - ✅ Ensure API token has required permissions

3. **💾 Vector DB Issues**:
   - Error: "FAISS index build failed"
     - ✅ Check if story text is not empty
     - ✅ Verify Python environment has required packages
     - ✅ Try clearing the FAISS index cache

4. **🐍 Python Environment**:
   - Error: "Module not found"
     - ✅ Run `pip install -r requirements.txt`
     - ✅ Activate virtual environment if using one
     - ✅ Check Python version compatibility

### 📊 Performance Tips

1. **Optimal Story Format**:
   - Keep JIRA stories concise and structured
   - Include acceptance criteria in story description
   - Use consistent formatting in JIRA

2. **Vector DB Optimization**:
   - Regular cleanup of old indices
   - Adjust chunk size for better context
   - Monitor memory usage with large stories

## 📬 Contact

For questions or collaboration, connect with us:

🧪 GitHub: [aiqualitylab](https://github.com/aiqualitylab)


