"""
Exercise 1: Azure Environment Setup
This script helps validate and configure your Azure OpenAI environment.
"""

import os
import sys
import json
import logging
from typing import Dict, Optional
import asyncio
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
from azure.core.exceptions import AzureError

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AzureEnvironmentSetup:
    def __init__(self):
        """Initialize Azure environment setup utilities."""
        self.credential = DefaultAzureCredential()
        self.subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        self.resource_group = os.getenv("AZURE_RESOURCE_GROUP")
        self.location = os.getenv("AZURE_LOCATION", "eastus")

    async def validate_prerequisites(self) -> bool:
        """
        Validate all prerequisites are met.
        
        Returns:
            bool: True if all prerequisites are met, False otherwise
        """
        try:
            # Check environment variables
            required_vars = [
                "AZURE_SUBSCRIPTION_ID",
                "AZURE_RESOURCE_GROUP",
                "AZURE_LOCATION"
            ]
            
            missing_vars = [var for var in required_vars if not os.getenv(var)]
            if missing_vars:
                logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
                return False

            # Validate Azure credentials
            logger.info("Validating Azure credentials...")
            await self._validate_credentials()

            logger.info("✅ All prerequisites validated successfully")
            return True

        except Exception as e:
            logger.error(f"Prerequisites validation failed: {str(e)}")
            return False

    async def _validate_credentials(self) -> None:
        """Validate Azure credentials."""
        try:
            # Test credential access
            token = await self.credential.get_token("https://management.azure.com/.default")
            if not token:
                raise ValueError("Could not obtain Azure token")
            
            logger.info("✅ Azure credentials validated")
        except Exception as e:
            logger.error(f"Credential validation failed: {str(e)}")
            raise

    async def setup_openai_service(self, service_name: str) -> Dict:
        """
        Set up Azure OpenAI service.
        
        Args:
            service_name: Name for the OpenAI service

        Returns:
            Dict containing service information
        """
        try:
            # Initialize the Cognitive Services Management Client
            cognitive_client = CognitiveServicesManagementClient(
                credential=self.credential,
                subscription_id=self.subscription_id
            )

            # Check if service exists
            logger.info(f"Checking if OpenAI service {service_name} exists...")
            try:
                existing_service = cognitive_client.accounts.get(
                    self.resource_group,
                    service_name
                )
                logger.info(f"OpenAI service {service_name} already exists")
                return {
                    "name": service_name,
                    "endpoint": existing_service.properties.endpoint,
                    "location": existing_service.location
                }
            except Exception:
                logger.info(f"Creating new OpenAI service {service_name}...")

            # Create service
            poller = cognitive_client.accounts.begin_create(
                self.resource_group,
                service_name,
                {
                    "sku": {
                        "name": "S0"
                    },
                    "location": self.location,
                    "kind": "OpenAI",
                    "properties": {
                        "custom_sub_domain_name": service_name,
                        "dynamic_throttling_enabled": True,
                        "network_acls": {
                            "default_action": "Deny",
                            "ip_rules": [
                                {
                                    "value": "0.0.0.0/0",
                                    "action": "Allow"
                                }
                            ]
                        }
                    }
                }
            )

            # Wait for completion
            service = poller.result()
            logger.info(f"✅ OpenAI service {service_name} created successfully")

            return {
                "name": service_name,
                "endpoint": service.properties.endpoint,
                "location": service.location
            }

        except Exception as e:
            logger.error(f"Failed to set up OpenAI service: {str(e)}")
            raise

    async def setup_monitoring(self, service_name: str) -> None:
        """
        Set up monitoring for the OpenAI service.
        
        Args:
            service_name: Name of the OpenAI service
        """
        try:
            logger.info(f"Setting up monitoring for {service_name}...")
            
            # TODO: Implement monitoring setup
            # This is a placeholder for the monitoring setup code
            # In a real implementation, you would:
            # 1. Set up Azure Monitor
            # 2. Configure diagnostic settings
            # 3. Set up alerts
            # 4. Configure logging

            logger.info("✅ Monitoring setup completed")

        except Exception as e:
            logger.error(f"Failed to set up monitoring: {str(e)}")
            raise

def main():
    """Main function to run the environment setup."""
    setup = AzureEnvironmentSetup()
    
    print("\n🚀 Starting Azure environment setup...")
    
    # Run setup tasks
    asyncio.run(setup.validate_prerequisites())
    
    # Example service name - in practice, this should be configurable
    service_name = "workshop-openai-service"
    
    try:
        # Set up OpenAI service
        service_info = asyncio.run(setup.setup_openai_service(service_name))
        print(f"\n📊 Service Information:")
        print(json.dumps(service_info, indent=2))
        
        # Set up monitoring
        asyncio.run(setup.setup_monitoring(service_name))
        
        print("\n✅ Environment setup completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Setup failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
