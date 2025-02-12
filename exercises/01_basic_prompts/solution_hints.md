# Solution Hints

Use these hints if you get stuck, but try to solve the exercises on your own first!

## Task 1: Basic Sales Metrics

### Hint 1: Total Sales
- Consider how to make your prompt focus on numerical calculations
- Think about specifying the exact format you want the response in
- Try adding constraints like "return only the number"

Example approach:
```python
# Instead of just asking for total sales, be specific:
prompt = """
Calculate the sum of all total_amount fields in the sales data.
Return only the numerical value without currency symbols or formatting.
"""
```

### Hint 2: Transaction Count
- Remember to look for unique transaction IDs
- Consider how to handle potential duplicates
- Think about what makes a transaction unique

### Hint 3: Average Deal Size
- Consider the relationship between total sales and number of transactions
- Think about handling currency formatting
- Remember to specify the precision you want

## Task 2: Customer Interaction Analysis

### Hint 1: Communication Patterns
- Look for sequences in the interaction_history
- Consider the timing between interactions
- Think about how to identify successful patterns

Example approach:
```python
# Use system message to set context:
system_message = "You are analyzing sales interaction patterns to identify the most effective sequences."
```

### Hint 2: Sales Cycle
- Pay attention to timestamps in interaction_history
- Consider how to measure the time between first and last interaction
- Think about what constitutes the start and end of a cycle

### Hint 3: Decision Points
- Look for interactions that led to progress
- Consider what types of interactions precede successful outcomes
- Think about the context of each interaction

## Task 3: Report Generation

### Hint 1: Executive Summary
- Focus on high-level insights
- Consider your audience (executives)
- Think about what metrics matter most

Example structure:
```python
prompt = """
Provide an executive summary with exactly:
1. Three key performance metrics
2. One major trend
3. One actionable recommendation
"""
```

### Hint 2: KPI Report
- Group related metrics together
- Consider using bullet points or sections
- Think about the hierarchy of information

### Hint 3: Recommendations
- Base recommendations on data patterns
- Consider both opportunities and risks
- Think about actionable next steps

## General Tips

1. **Prompt Structure**
   - Start with clear instructions
   - Specify output format
   - Include relevant context

2. **System Messages**
   - Use them to set the role and expertise level
   - Consider different perspectives (analyst, manager, etc.)

3. **Error Handling**
   - Consider edge cases in your prompts
   - Think about data validation
   - Plan for unexpected responses

4. **Output Formatting**
   - Be explicit about the format you want
   - Consider using examples in your prompts
   - Think about how the output will be used

Remember: The goal is to create clear, specific prompts that consistently produce the desired output format and content.

## Still Stuck?

If you're still having trouble:
1. Review the example prompts in the code
2. Check the Azure OpenAI documentation
3. Ask your instructor for guidance
4. Look at how the sample data is structured
5. Try breaking down the task into smaller steps
