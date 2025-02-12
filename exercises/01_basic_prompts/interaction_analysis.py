"""
Exercise 1 - Task 2: Customer Interaction Analysis
This script demonstrates prompt engineering for analyzing customer interactions and sales cycles.
"""

import asyncio
import json
from typing import Dict
import sys
import os

# Add the parent directory to the Python path so we can import the utils module
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.utils.azure_openai_utils import AzureOpenAIHelper

async def analyze_interactions(sales_data: Dict) -> None:
    """Analyze customer interactions and sales cycles using Azure OpenAI."""
    helper = AzureOpenAIHelper()

    # Example of few-shot learning with interaction patterns
    interaction_examples = [
        {
            "input": "Email -> Demo -> Meeting -> Deal",
            "output": "Traditional sales cycle with standard touchpoints. 3 interactions before closure."
        },
        {
            "input": "Conference -> Site Visit -> Meeting -> Deal",
            "output": "Event-driven sales cycle with technical validation. High-touch enterprise pattern."
        }
    ]

    # TODO: Complete these prompt templates
    prompts = {
        "communication_pattern": """
        Analyze the interaction history for each sale and identify common communication patterns.
        Focus on the sequence of interactions and their effectiveness.

        Consider:
        - Most common interaction sequences
        - Time between interactions
        - Impact of different interaction types on deal closure

        Sales Data:
        {sales_data}

        Provide your analysis in bullet points, highlighting key patterns discovered.
        """,

        "sales_cycle": """
        Calculate and analyze the sales cycle duration for each transaction.
        
        For each sale, determine:
        1. Time from first interaction to deal closure
        2. Number of interactions required
        3. Most effective interaction sequence

        Sales Data:
        {sales_data}

        Format your response as a structured analysis with specific metrics.
        """,

        "decision_points": """
        Identify key decision points in the sales process based on the interaction history.
        
        Look for:
        - Interactions that led to significant progress
        - Common objections or concerns
        - Factors that accelerated the sale

        Sales Data:
        {sales_data}

        Present your findings as actionable insights for the sales team.
        """
    }

    # Example of a completed analysis prompt with context
    interaction_analysis_prompt = helper.format_prompt_with_examples(
        """
        Analyze the customer interaction patterns in the following sales data.
        Identify the most effective communication sequences and their impact on deal closure.
        
        Sales Data:
        {sales_data}
        
        Provide your analysis in the following format:
        1. Most Effective Pattern:
           - Sequence of interactions
           - Average time to close
           - Success rate indicators
        
        2. Key Observations:
           - Pattern effectiveness
           - Customer engagement indicators
           - Recommended improvements
        """,
        interaction_examples
    )

    try:
        # Generate completion for the example prompt
        print("\n🔍 Analyzing customer interactions...")
        analysis_response = await helper.generate_completion(
            interaction_analysis_prompt.format(sales_data=json.dumps(sales_data, indent=2)),
            system_message=helper.create_system_message("customer success")
        )
        print("\n📊 Interaction Analysis:")
        print(analysis_response)

        # TODO: Implement your own prompts and analyze the results
        # Example structure:
        # pattern_response = await helper.generate_completion(
        #     prompts["communication_pattern"].format(sales_data=json.dumps(sales_data, indent=2))
        # )

    except Exception as e:
        print(f"\n❌ Error analyzing interactions: {str(e)}")
        return

def main():
    """Main function to run the interaction analysis."""
    helper = AzureOpenAIHelper()
    sales_data = helper.load_sales_data()
    
    print("\n🚀 Starting customer interaction analysis...")
    asyncio.run(analyze_interactions(sales_data))

if __name__ == "__main__":
    main()
