# Exercise 1: Basic Prompt Engineering for Sales Analysis

## 🎯 Learning Objectives
In this exercise, you will learn to:
- Create effective prompts for analyzing sales data
- Extract meaningful insights from customer interactions
- Generate structured sales reports using GPT-4

## 🔍 Exercise Overview
You'll work with real sales data to create prompts that extract valuable business insights. This exercise focuses on fundamental prompt engineering techniques using Azure OpenAI Service.

## 📝 Tasks

### Task 1: Basic Sales Metrics (10 minutes)
1. Open `basic_metrics.py`
2. Complete the prompt template to extract:
   - Total sales amount
   - Number of transactions
   - Average deal size
3. Run the script and verify the output matches the expected format

🤔 **Knowledge Check**: What makes a prompt effective for extracting numerical data?

### Task 2: Customer Interaction Analysis (10 minutes)
1. Open `interaction_analysis.py`
2. Create prompts to analyze:
   - Customer communication patterns
   - Sales cycle duration
   - Key decision points
3. Compare results with the provided example outputs

🤔 **Knowledge Check**: How does adding context to your prompt improve the analysis?

### Task 3: Sales Report Generation (10 minutes)
1. Open `report_generation.py`
2. Develop prompts that generate:
   - Executive summary
   - Key performance indicators
   - Recommendations
3. Evaluate the quality of generated reports

## 💡 Tips for Success
- Start with simple, clear prompts
- Be specific about the format you want
- Include relevant context
- Test with different variations

## 🔨 Getting Started

1. Navigate to the exercise directory:
   ```bash
   cd exercises/01_basic_prompts
   ```

2. Review the sample code:
   ```python
   from utils.azure_openai_utils import AzureOpenAIHelper
   
   helper = AzureOpenAIHelper()
   sales_data = helper.load_sales_data()
   ```

3. Complete the prompt templates in each Python file

## 📊 Sample Data Structure
```json
{
  "transaction_id": "TX001",
  "customer": {
    "name": "John Smith",
    "company": "Tech Solutions Inc"
  },
  "total_amount": 24000.00
}
```

## ✅ Success Criteria
- All scripts run without errors
- Generated insights are relevant and accurate
- Output follows the specified format
- Prompts are clear and reusable

## 🎯 Challenge Tasks
Once you've completed the main tasks, try these challenges:
1. Add error handling for edge cases
2. Implement dynamic prompt generation
3. Create a comparative analysis across different time periods

## 📚 Resources
- [Azure OpenAI Best Practices](https://learn.microsoft.com/azure/cognitive-services/openai/concepts/best-practices)
- [Prompt Engineering Guide](https://learn.microsoft.com/azure/cognitive-services/openai/concepts/prompt-engineering)
- Sample solutions in the `solutions` directory

## 🆘 Need Help?
- Check the troubleshooting guide
- Review the solution hints
- Ask your instructor for guidance
