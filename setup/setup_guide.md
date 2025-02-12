# Setup Guide: Azure OpenAI for Sales Analysis

## Step-by-Step Setup Instructions

### 1. Azure OpenAI Service Setup (5 minutes)

#### 1.1 Access Azure Portal
1. Open your web browser and navigate to [Azure Portal](https://portal.azure.com)
2. Sign in with your Azure credentials
   ```
   Note: If you don't have an account:
   a. Go to https://azure.microsoft.com/free
   b. Click "Start free"
   c. Follow the registration process
   ```

#### 1.2 Create Azure OpenAI Service
1. In the Azure Portal:
   ```
   → Click "＋ Create a resource" (top left)
   → Search bar: Type "Azure OpenAI"
   → Select "Azure OpenAI" from results
   → Click "Create"
   ```

2. Fill in the required information:
   ```
   Basics Tab:
   ├── Subscription: [Your Azure subscription]
   ├── Resource group: [Create new or use existing]
   │   └── If new: Click "Create new"
   │       └── Name it: "openai-workshop-rg"
   ├── Name: [Choose unique name, e.g., "sales-analysis-openai"]
   ├── Region: [Choose nearest available]
   └── Pricing tier: Standard S0
   ```

3. Click "Review + create"
   - Wait for validation to pass (green checkmark)
   - Click "Create"
   - Wait for deployment (2-3 minutes)

#### 1.3 Get API Credentials
1. Once deployment completes:
   ```
   → Click "Go to resource"
   → Left menu: Click "Keys and Endpoint"
   → You'll see:
     ├── KEY 1
     ├── KEY 2
     └── Endpoint
   ```

2. Copy these values - you'll need them later:
   ```
   AZURE_OPENAI_API_KEY=[Copy KEY 1]
   AZURE_OPENAI_ENDPOINT=[Copy Endpoint URL]
   ```

#### 1.4 Deploy a Model
1. In your Azure OpenAI resource:
   ```
   → Left menu: Click "Model deployments"
   → Click "＋ Create new deployment"
   → Fill in:
     ├── Model: gpt-4
     ├── Model version: [Latest]
     ├── Deployment name: sales-gpt4
     └── Advanced options: [Leave default]
   → Click "Create"
   ```

### 2. Python Environment Setup (3 minutes)

#### 2.1 Verify Python Installation
Open your terminal and run:
```bash
# Windows
python --version

# macOS/Linux
python3 --version

# Expected output: Python 3.9.0 or higher
```

If Python is not installed or version is too low:
1. Download from [Python.org](https://python.org/downloads)
2. During installation:
   ```
   ✓ Add Python to PATH
   ✓ Install pip
   ```

#### 2.2 Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Your prompt should change to show (venv)
```

#### 2.3 Install Dependencies
```bash
# Make sure you're in the project root directory
pip install -r setup/requirements.txt

# Expected output:
# Successfully installed openai-1.0.0 ...
```

### 3. Configuration (2 minutes)

#### 3.1 Set Up Environment Variables
1. Create a new file named `.env` in the project root:
   ```
   # Windows
   copy nul .env
   
   # macOS/Linux
   touch .env
   ```

2. Add your credentials to `.env`:
   ```plaintext
   AZURE_OPENAI_API_KEY=your_api_key_here
   AZURE_OPENAI_ENDPOINT=your_endpoint_here
   AZURE_OPENAI_MODEL=sales-gpt4
   ```

⚠️ **Important Security Notes**:
- Never commit `.env` to version control
- Keep your API key secure
- Don't share your credentials

#### 3.2 Verify Setup
Run the validation script:
```bash
python src/utils/validate_setup.py
```

You should see:
```
🔍 Running setup validation...

✓ Python version meets requirements
✓ All required environment variables are set
✓ Sample sales data file is valid
✓ Successfully connected to Azure OpenAI

📋 Validation Summary:
✅ All checks passed! You're ready to start the workshop!
```

### Troubleshooting Common Issues

#### API Key Issues
If you see: "Error: Invalid API key"
```
→ Check for extra spaces in .env
→ Verify key is active in Azure portal
→ Try copying the key again
```

#### Python Environment Issues
If you see: "Module not found"
```
→ Verify virtual environment is activated
→ Run: pip install -r setup/requirements.txt
→ Check Python version: python --version
```

#### Azure OpenAI Connection Issues
If you see: "Could not connect to Azure OpenAI"
```
→ Check your internet connection
→ Verify endpoint URL format
→ Confirm model deployment is complete
```

### Next Steps
Once your setup is validated:
1. Open `exercises/01_basic_prompts/README.md`
2. Review the exercise objectives
3. Start with Task 1: Basic Sales Metrics

Need help? Check:
- Azure OpenAI Documentation
- Workshop Troubleshooting Guide
- Ask your instructor
