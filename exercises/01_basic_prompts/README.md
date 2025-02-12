# Exercise 1: Basic Prompt Engineering for Sales Analysis

## 🎯 Learning Objectives
By completing this exercise, you will be able to:
- Create effective prompts for analyzing sales data
- Extract meaningful insights from customer interactions
- Generate structured sales reports using GPT-4

## 📋 Prerequisites Check
Before starting, ensure you have:
- [ ] Completed the setup guide
- [ ] Validated your Azure OpenAI connection
- [ ] Activated your Python virtual environment
- [ ] Installed all requirements

## 🗺️ Exercise Roadmap
```
Task 1 (10 min) → Task 2 (10 min) → Task 3 (10 min)
Basic Metrics    Interaction      Report
Analysis         Analysis         Generation
```

## 📝 Detailed Task Instructions

### Task 1: Basic Sales Metrics (10 minutes)

#### Step 1: Prepare Your Environment
```bash
# Ensure you're in the exercise directory
cd exercises/01_basic_prompts

# Verify your virtual environment is active
# Your prompt should show (venv)
```

#### Step 2: Open the Exercise File
1. Open `basic_metrics.py` in your editor
2. Locate the `prompts` dictionary containing template prompts
3. You'll see three TODO sections:
   ```python
   prompts = {
       "total_sales": "...",
       "transaction_count": "...",
       "average_deal": "..."
   }
   ```

#### Step 3: Complete the Prompts
1. Total Sales Prompt:
   ```python
   # Example structure:
   total_sales = """
   Analyze the following sales data and calculate the total sales amount.
   Return only the numerical value without any text or formatting.
   
   Sales Data:
   {sales_data}
   """
   ```

2. Expected Output Format:
   ```
   71500.00
   ```

🤔 **Knowledge Check Point 1**:
- Does your prompt specify exact output format?
- Have you removed any unnecessary context?
- Is the instruction clear and unambiguous?

#### Step 4: Run and Validate
```bash
# Run the script
python basic_metrics.py

# Expected output:
🚀 Starting basic sales metrics analysis...
📊 Sales Summary:
[Your generated metrics will appear here]
```

#### Step 5: Refine Your Prompts
If the output isn't as expected:
1. Check the format specification
2. Adjust the constraints
3. Run again to verify

### Task 2: Customer Interaction Analysis (10 minutes)

[Similar detailed steps for Task 2...]

### Task 3: Sales Report Generation (10 minutes)

[Similar detailed steps for Task 3...]

## ✅ Success Validation Checklist

### Task 1 Validation
- [ ] Total sales calculation matches expected value
- [ ] Transaction count is accurate
- [ ] Average deal size is correctly calculated
- [ ] All outputs are properly formatted

### Task 2 Validation
- [ ] Communication patterns are identified
- [ ] Sales cycle duration is accurate
- [ ] Decision points are clearly highlighted

### Task 3 Validation
- [ ] Executive summary is concise and clear
- [ ] KPIs are accurately reported
- [ ] Recommendations are actionable

## 🔍 Code Review Guidelines

When reviewing your prompts, check:
```python
# Good Prompt Example:
"""
Calculate the total sales amount from the data.
Requirements:
1. Sum all 'total_amount' fields
2. Return only the number
3. Use 2 decimal places
"""

# Bad Prompt Example:
"""
What are the total sales?
"""
```

## 🆘 Troubleshooting Guide

### Common Issues and Solutions

1. Incorrect Output Format
   ```
   Problem: "Total sales are $71,500.00"
   Solution: Specify "Return only the number without currency symbols"
   ```

2. Missing Data
   ```
   Problem: "Cannot find sales_data"
   Solution: Check file path in load_sales_data()
   ```

3. Prompt Too Vague
   ```
   Problem: Getting narrative responses
   Solution: Add specific format requirements
   ```

## 📚 Additional Resources
- [Azure OpenAI Prompt Engineering Guide](https://learn.microsoft.com/azure/cognitive-services/openai/concepts/prompt-engineering)
- [Sample Solutions](./solutions/)
- [Advanced Challenges](./challenges/)

## 🎯 Extension Activities
Once you've completed the main tasks:

1. Error Handling
   ```python
   # Add validation for edge cases
   if not sales_data:
       handle_empty_data()
   ```

2. Dynamic Prompts
   ```python
   # Create prompt templates
   prompt = template.format(
       metric="total_sales",
       format="numerical"
   )
   ```

3. Comparative Analysis
   ```python
   # Compare performance across periods
   analyze_trends(current_data, historical_data)
   ```

Need help? 
- Check solution_hints.md
- Ask your instructor
- Review the example code
