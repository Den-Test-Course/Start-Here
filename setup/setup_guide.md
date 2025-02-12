# Setup Guide: Azure OpenAI for Sales Analysis

## Overview
This guide will walk you through setting up your development environment for the Prompt Engineering lab. Follow each step carefully to ensure a smooth experience.

## Step 1: Azure OpenAI Service Setup (5 minutes)

### 1.1 Access Azure Portal
1. Navigate to [Azure Portal](https://portal.azure.com)
2. Sign in with your Azure credentials
3. If you don't have an account, create one with a free trial

### 1.2 Create Azure OpenAI Service
1. Click "Create a resource"
2. Search for "Azure OpenAI"
3. Click "Create"
4. Fill in the required information:
   - Subscription: Your Azure subscription
   - Resource group: Create new or use existing
   - Region: Choose the nearest available region
   - Name: Choose a unique name
   - Pricing tier: Standard S0

### 1.3 Get API Credentials
1. Once deployment is complete, go to your Azure OpenAI resource
2. Navigate to "Keys and Endpoint" in the left menu
3. Copy the following:
   - API Key
   - Endpoint URL

🤔 **Knowledge Check**: Can you locate your API key and endpoint in the Azure portal?

## Step 2: Python Environment Setup (3 minutes)

### 2.1 Verify Python Installation
```bash
python --version  # Should be 3.9 or higher
```

### 2.2 Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2.3 Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 3: Configuration (2 minutes)

### 3.1 Set Up Environment Variables
Create a `.env` file in your project root:
```plaintext
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_OPENAI_MODEL=gpt-4  # or your deployed model name
```

⚠️ **Important**: Never commit your `.env` file to version control!

### 3.2 Verify Setup
Run the validation script:
```bash
python src/utils/validate_setup.py
```

You should see: "✅ Setup validated successfully!"

## Troubleshooting

### Common Issues

1. **API Key Issues**
   - Ensure you've copied the full key
   - Check for extra spaces
   - Verify the key is active in Azure portal

2. **Dependencies**
   - Try running: `pip install --upgrade -r requirements.txt`
   - Check Python version compatibility

3. **Environment Variables**
   - Restart your terminal after setting env variables
   - Verify `.env` file is in the correct location

### Still Having Issues?
1. Check the Azure OpenAI status page
2. Review Azure OpenAI quotas and limits
3. Consult the troubleshooting guide

## Next Steps
Once your setup is validated:
1. Review the sample data in `data/sample_sales.json`
2. Open Exercise 01 in the exercises folder
3. Start with basic prompt creation

🎯 **Setup Complete!** You're ready to begin the lab exercises.
