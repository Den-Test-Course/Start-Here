# Troubleshooting Guide

## Common Setup Issues and Solutions

### 1. Azure Portal Access

#### Problem: Can't Access Azure Portal
```
Error: "Your account needs to be set up"
```

**Solution:**
1. Check your browser:
   ```
   ✓ Clear cache and cookies
   ✓ Try incognito/private mode
   ✓ Use Chrome or Edge
   ```

2. Account setup:
   ```
   → Go to portal.azure.com
   → Click "Set up account"
   → Follow activation steps
   → Wait 5 minutes for propagation
   ```

### 2. Azure OpenAI Service Creation

#### Problem: Region Not Available
```
Error: "Azure OpenAI is not available in selected region"
```

**Solution:**
Try these regions in order:
1. East US
2. South Central US
3. West Europe

#### Problem: Quota Limit
```
Error: "Quota limit reached"
```

**Solution:**
1. Check current usage:
   ```
   → Azure Portal
   → Your OpenAI resource
   → Quotas
   ```

2. Request increase:
   ```
   → Click "Request Increase"
   → Fill form:
     ├── Model: GPT-4
     ├── New limit: 1
     └── Justification: "For workshop training"
   ```

### 3. Python Environment

#### Problem: Python Not Found
```
'python' is not recognized as an internal or external command
```

**Solution:**
1. Windows:
   ```
   → Control Panel
   → System
   → Advanced system settings
   → Environment Variables
   → Path
   → Add Python installation directory
   ```

2. Verify installation:
   ```bash
   # Should show Python location
   where python
   ```

#### Problem: pip Install Errors
```
Error: Microsoft Visual C++ 14.0 is required
```

**Solution:**
1. Download Visual C++ Build Tools:
   ```
   → https://visualstudio.microsoft.com/visual-cpp-build-tools/
   → Run installer
   → Select "C++ build tools"
   → Install
   ```

2. Try installation again:
   ```bash
   pip install --upgrade pip
   pip install -r setup/requirements.txt
   ```

### 4. Environment Variables

#### Problem: .env Not Working
```
Error: Could not find .env file
```

**Solution:**
1. Check file location:
   ```
   project_root/
   └── .env  # Must be here
   ```

2. Verify file content:
   ```
   # No quotes needed
   AZURE_OPENAI_API_KEY=abc123...
   AZURE_OPENAI_ENDPOINT=https://...
   AZURE_OPENAI_MODEL=sales-gpt4
   ```

3. Check file visibility:
   ```bash
   # Windows
   dir /a
   
   # macOS/Linux
   ls -la
   ```

### 5. Azure OpenAI Connection

#### Problem: Authentication Failed
```
Error: Authentication failed. Check your API key
```

**Solution:**
1. Verify key format:
   ```
   ✓ No spaces before/after
   ✓ No quotes
   ✓ Copied entire key
   ```

2. Check endpoint format:
   ```
   ✓ Starts with https://
   ✓ Ends with .openai.azure.com
   ✓ No trailing slash
   ```

3. Test connection:
   ```bash
   python src/utils/validate_setup.py
   ```

### 6. Model Deployment

#### Problem: Model Not Found
```
Error: Model 'sales-gpt4' not found
```

**Solution:**
1. Check deployment:
   ```
   → Azure Portal
   → Your OpenAI resource
   → Model deployments
   → Verify:
     ├── Model: gpt-4
     ├── Deployment name: sales-gpt4
     └── Status: Succeeded
   ```

2. Wait for deployment:
   ```
   Deployment can take 5-10 minutes
   Status must be "Succeeded"
   ```

### 7. Exercise Execution

#### Problem: Import Error
```
ModuleNotFoundError: No module named 'azure'
```

**Solution:**
1. Check virtual environment:
   ```bash
   # Should show (venv)
   python -c "import sys; print(sys.prefix)"
   ```

2. Reinstall packages:
   ```bash
   pip uninstall -r setup/requirements.txt
   pip install -r setup/requirements.txt
   ```

### Need More Help?

1. Check Azure Status:
   ```
   → https://status.azure.com
   → Filter for OpenAI
   ```

2. Review Logs:
   ```bash
   # Check validation logs
   python src/utils/validate_setup.py --verbose
   ```

3. Contact Support:
   - Ask your instructor
   - Check Azure documentation
   - Review exercise README
