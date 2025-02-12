"""
Setup validation script for Azure OpenAI workshop.
"""

import os
import sys
from typing import List, Tuple
import json
from dotenv import load_dotenv
import openai
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

def print_status(message: str, success: bool = True) -> None:
    """Print a status message with color."""
    if success:
        print(f"{Fore.GREEN}✓{Style.RESET_ALL} {message}")
    else:
        print(f"{Fore.RED}✗{Style.RESET_ALL} {message}")

def check_python_version() -> Tuple[bool, str]:
    """Check if Python version meets requirements."""
    current_version = sys.version_info
    required_version = (3, 9)
    
    if current_version >= required_version:
        return True, f"Python version {current_version.major}.{current_version.minor} meets requirements"
    else:
        return False, f"Python version {current_version.major}.{current_version.minor} does not meet minimum requirement of 3.9"

def check_environment_variables() -> Tuple[bool, List[str]]:
    """Check if all required environment variables are set."""
    load_dotenv()
    
    required_vars = [
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_MODEL"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    return len(missing_vars) == 0, missing_vars

def check_sales_data() -> Tuple[bool, str]:
    """Check if sample sales data file exists and is valid JSON."""
    data_path = os.path.join(os.path.dirname(__file__), "../../data/sample_sales.json")
    
    if not os.path.exists(data_path):
        return False, "Sample sales data file not found"
    
    try:
        with open(data_path, 'r') as f:
            json.load(f)
        return True, "Sample sales data file is valid"
    except json.JSONDecodeError:
        return False, "Sample sales data file contains invalid JSON"
    except Exception as e:
        return False, f"Error reading sample sales data: {str(e)}"

def test_azure_openai_connection() -> Tuple[bool, str]:
    """Test connection to Azure OpenAI service."""
    try:
        openai.api_type = "azure"
        openai.api_version = "2023-05-15"
        openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
        
        # Simple test completion
        response = openai.ChatCompletion.create(
            engine=os.getenv("AZURE_OPENAI_MODEL"),
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say 'Connection successful' if you can read this."}
            ],
            max_tokens=50
        )
        
        if "Connection successful" in response.choices[0].message.content.lower():
            return True, "Successfully connected to Azure OpenAI"
        else:
            return False, "Connected to Azure OpenAI but received unexpected response"
            
    except Exception as e:
        return False, f"Failed to connect to Azure OpenAI: {str(e)}"

def main():
    """Run all validation checks."""
    print(f"\n{Fore.CYAN}🔍 Running setup validation...{Style.RESET_ALL}\n")
    
    # Check Python version
    python_success, python_message = check_python_version()
    print_status(python_message, python_success)
    
    # Check environment variables
    env_success, missing_vars = check_environment_variables()
    if env_success:
        print_status("All required environment variables are set")
    else:
        print_status(f"Missing environment variables: {', '.join(missing_vars)}", False)
    
    # Check sample data
    data_success, data_message = check_sales_data()
    print_status(data_message, data_success)
    
    # Test Azure OpenAI connection
    if env_success:
        connection_success, connection_message = test_azure_openai_connection()
        print_status(connection_message, connection_success)
    
    # Overall status
    print(f"\n{Fore.CYAN}📋 Validation Summary:{Style.RESET_ALL}")
    all_checks_passed = all([
        python_success,
        env_success,
        data_success,
        env_success and connection_success
    ])
    
    if all_checks_passed:
        print(f"\n{Fore.GREEN}✅ All checks passed! You're ready to start the workshop!{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}❌ Some checks failed. Please fix the issues above before continuing.{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
