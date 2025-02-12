"""
Utility functions for interacting with Azure OpenAI Service.
"""

import os
import json
from typing import Dict, List, Union, Optional
from dotenv import load_dotenv
import openai
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = "2023-05-15"

class AzureOpenAIHelper:
    def __init__(self):
        """Initialize the Azure OpenAI helper with environment variables."""
        self.model = os.getenv("AZURE_OPENAI_MODEL", "gpt-4")
        self._validate_setup()

    def _validate_setup(self) -> None:
        """Validate that all required environment variables are set."""
        required_vars = ["AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_MODEL"]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing_vars)}\n"
                "Please check your .env file and ensure all variables are set."
            )

    async def generate_completion(
        self,
        prompt: str,
        max_tokens: int = 1000,
        temperature: float = 0.7,
        system_message: Optional[str] = None
    ) -> str:
        """
        Generate a completion using Azure OpenAI.

        Args:
            prompt (str): The prompt to generate completion for
            max_tokens (int): Maximum number of tokens to generate
            temperature (float): Sampling temperature
            system_message (str, optional): System message to set context

        Returns:
            str: Generated completion text
        """
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})

        try:
            response = await openai.ChatCompletion.acreate(
                engine=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error generating completion: {str(e)}")

    def load_sales_data(self, filepath: str = "../data/sample_sales.json") -> Dict:
        """
        Load sample sales data from JSON file.

        Args:
            filepath (str): Path to the sales data JSON file

        Returns:
            Dict: Sales data as a dictionary
        """
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Error loading sales data: {str(e)}")

    def format_prompt_with_examples(
        self,
        prompt: str,
        examples: List[Dict[str, str]]
    ) -> str:
        """
        Format a prompt with few-shot examples.

        Args:
            prompt (str): Base prompt
            examples (List[Dict]): List of example dictionaries with 'input' and 'output' keys

        Returns:
            str: Formatted prompt with examples
        """
        formatted_examples = "\n\nExamples:\n"
        for i, example in enumerate(examples, 1):
            formatted_examples += f"\nExample {i}:\nInput: {example['input']}\nOutput: {example['output']}\n"
        
        return f"{prompt}\n{formatted_examples}\n\nNow, please provide your response:"

    def create_system_message(self, role: str = "sales analyst") -> str:
        """
        Create a system message for setting the AI's role.

        Args:
            role (str): Role to assign to the AI

        Returns:
            str: Formatted system message
        """
        roles = {
            "sales analyst": "You are an experienced sales analyst skilled at extracting insights from sales data.",
            "sales manager": "You are a sales manager focused on team performance and strategic decision-making.",
            "customer success": "You are a customer success manager analyzing customer interactions and satisfaction."
        }
        
        return roles.get(role, roles["sales analyst"])

    def log_completion(
        self,
        prompt: str,
        completion: str,
        metadata: Optional[Dict] = None
    ) -> None:
        """
        Log prompt and completion for analysis.

        Args:
            prompt (str): Original prompt
            completion (str): Generated completion
            metadata (Dict, optional): Additional metadata to log
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "completion": completion,
            "metadata": metadata or {}
        }
        
        # Ensure log directory exists
        os.makedirs("logs", exist_ok=True)
        
        # Append to log file
        with open("logs/completions.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")

# Example usage
if __name__ == "__main__":
    helper = AzureOpenAIHelper()
    print("✅ Azure OpenAI helper initialized successfully!")
