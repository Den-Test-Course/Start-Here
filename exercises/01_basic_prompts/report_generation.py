"""
Exercise 1 - Task 3: Sales Report Generation
This script demonstrates prompt engineering for generating structured sales reports.
"""

import asyncio
import json
from typing import Dict
import sys
import os

# Add the parent directory to the Python path so we can import the utils module
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.utils.azure_openai_utils import AzureOpenAIHelper

async def generate_reports(sales_data: Dict) -> None:
    """Generate various sales reports using Azure OpenAI."""
    helper = AzureOpenAIHelper()

    # Example report structure for few-shot learning
    report_examples = [
        {
            "input": "Generate executive summary for Q1 sales",
            "output": """
Executive Summary: Q1 2024
- Total Revenue: $1.2M
- Key Achievement: 15% growth in enterprise segment
- Areas for Improvement: SMB pipeline development
            """
        }
    ]

    # TODO: Complete these prompt templates
    prompts = {
        "executive_summary": """
        Create a concise executive summary of the sales data.
        
        Requirements:
        - High-level overview of performance
        - Key metrics and achievements
        - Critical insights for executive attention
        
        Sales Data:
        {sales_data}
        
        Format the summary in a clear, professional style suitable for executive review.
        """,

        "kpi_report": """
        Generate a detailed KPI report from the sales data.
        
        Include:
        1. Revenue Metrics
           - Total revenue
           - Average deal size
           - Revenue by customer segment
        
        2. Sales Efficiency
           - Average sales cycle length
           - Conversion rate
           - Interactions per deal
        
        3. Customer Metrics
           - Customer segment distribution
           - Repeat customer rate
           - Product category performance
        
        Sales Data:
        {sales_data}
        
        Present the KPIs in a structured format with clear headings and metrics.
        """,

        "recommendations": """
        Based on the sales data, provide strategic recommendations.
        
        Consider:
        - Sales process optimization
        - Customer engagement improvements
        - Revenue growth opportunities
        - Risk mitigation strategies
        
        Sales Data:
        {sales_data}
        
        Format recommendations as actionable items with clear justification.
        """
    }

    # Example of a completed report prompt with specific formatting
    full_report_prompt = helper.format_prompt_with_examples(
        """
        Generate a comprehensive sales performance report using the following data.
        
        Sales Data:
        {sales_data}
        
        Structure the report as follows:

        1. EXECUTIVE SUMMARY
        -------------------
        • Overview of key performance indicators
        • Significant trends and patterns
        • Major achievements and challenges

        2. DETAILED ANALYSIS
        -------------------
        • Revenue Analysis
          - Break down by product category
          - Customer segment performance
          - Sales team performance
        
        • Sales Process Metrics
          - Conversion rates
          - Sales cycle duration
          - Interaction effectiveness
        
        3. RECOMMENDATIONS
        -----------------
        • Strategic opportunities
        • Process improvements
        • Risk mitigation
        
        Use data-driven insights and specific metrics to support all findings.
        """,
        report_examples
    )

    try:
        # Generate completion for the example prompt
        print("\n📝 Generating comprehensive sales report...")
        report_response = await helper.generate_completion(
            full_report_prompt.format(sales_data=json.dumps(sales_data, indent=2)),
            system_message=helper.create_system_message("sales manager"),
            temperature=0.7  # Slightly higher temperature for more creative report writing
        )
        print("\n📊 Sales Report:")
        print(report_response)

        # TODO: Implement your own prompts and analyze the results
        # Example structure:
        # summary_response = await helper.generate_completion(
        #     prompts["executive_summary"].format(sales_data=json.dumps(sales_data, indent=2))
        # )

    except Exception as e:
        print(f"\n❌ Error generating reports: {str(e)}")
        return

def main():
    """Main function to run the report generation."""
    helper = AzureOpenAIHelper()
    sales_data = helper.load_sales_data()
    
    print("\n🚀 Starting sales report generation...")
    asyncio.run(generate_reports(sales_data))

if __name__ == "__main__":
    main()
