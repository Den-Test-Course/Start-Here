"""
Exercise 1 - Task 1: Basic Sales Metrics
This script demonstrates basic prompt engineering for extracting sales metrics.
"""

import asyncio
import json
from typing import Dict
import sys
import os

# Add the parent directory to the Python path so we can import the utils module
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.utils.azure_openai_utils import AzureOpenAIHelper

async def analyze_basic_metrics(sales_data: Dict) -> None:
    """Analyze basic sales metrics using Azure OpenAI."""
    helper = AzureOpenAIHelper()

    # TODO: Complete these prompt templates
    prompts = {
        "total_sales": """
        Analyze the following sales data and calculate the total sales amount.
        Return only the numerical value without any text or formatting.
        
        Sales Data:
        {sales_data}
        """,
        
        "transaction_count": """
        Count the number of unique transactions in the following sales data.
        Return only the numerical value without any text or formatting.
        
        Sales Data:
        {sales_data}
        """,
        
        "average_deal": """
        Calculate the average deal size from the following sales data.
        Return only the numerical value without any text or formatting.
        
        Sales Data:
        {sales_data}
        """,
    }

    # Example of a completed prompt with proper formatting and context
    sales_summary_prompt = """
    You are a sales analyst reviewing recent transaction data. Please provide a brief summary
    of the following sales metrics in a clear, structured format:
    
    Sales Data:
    {sales_data}
    
    Please format your response as follows:
    Total Sales: $X
    Number of Transactions: X
    Average Deal Size: $X
    
    Additional insights:
    - Mention any notable patterns
    - Highlight largest transaction
    - Identify most frequent customer
    """

    try:
        # Generate completion for the example prompt
        print("\n🔍 Generating sales summary...")
        summary_response = await helper.generate_completion(
            sales_summary_prompt.format(sales_data=json.dumps(sales_data, indent=2)),
            system_message=helper.create_system_message("sales analyst")
        )
        print("\n📊 Sales Summary:")
        print(summary_response)

        # TODO: Implement your own prompts and analyze the results
        # Example structure:
        # total_sales_response = await helper.generate_completion(
        #     prompts["total_sales"].format(sales_data=json.dumps(sales_data, indent=2))
        # )
        
    except Exception as e:
        print(f"\n❌ Error analyzing sales metrics: {str(e)}")
        return

def main():
    """Main function to run the sales metrics analysis."""
    helper = AzureOpenAIHelper()
    sales_data = helper.load_sales_data()
    
    print("\n🚀 Starting basic sales metrics analysis...")
    asyncio.run(analyze_basic_metrics(sales_data))

if __name__ == "__main__":
    main()
