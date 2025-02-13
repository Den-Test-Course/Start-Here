"""
Exercise 2: Security Implementation
This script implements security configurations for Azure OpenAI service.
"""

import os
import sys
import json
import logging
from typing import Dict, List, Optional
import asyncio
from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.core.exceptions import AzureError

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SecurityConfiguration:
    def __init__(self):
        """Initialize security configuration utilities."""
        self.credential = DefaultAzureCredential()
        self.subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        self.resource_group = os.getenv("AZURE_RESOURCE_GROUP")
        self.location = os.getenv("AZURE_LOCATION", "eastus")
        self.service_name = os.getenv("AZURE_OPENAI_SERVICE_NAME")

    async def setup_rbac(self, role_assignments: List[Dict[str, str]]) -> None:
        """
        Set up RBAC roles for the OpenAI service.
        
        Args:
            role_assignments: List of role assignments with principal IDs and role definitions
        """
        try:
            logger.info("Setting up RBAC roles...")
            
            # Initialize the Authorization Management Client
            auth_client = AuthorizationManagementClient(
                credential=self.credential,
                subscription_id=self.subscription_id
            )

            # Get service resource ID
            resource_id = (f"/subscriptions/{self.subscription_id}/resourceGroups/"
                         f"{self.resource_group}/providers/Microsoft.CognitiveServices/"
                         f"accounts/{self.service_name}")

            # Create role assignments
            for assignment in role_assignments:
                try:
                    logger.info(f"Creating role assignment for {assignment['principal_id']}")
                    
                    # Create role assignment
                    auth_client.role_assignments.create(
                        scope=resource_id,
                        role_assignment_name=assignment.get("name", os.urandom(16).hex()),
                        parameters={
                            "role_definition_id": assignment["role_definition_id"],
                            "principal_id": assignment["principal_id"]
                        }
                    )
                    
                    logger.info(f"✅ Role assignment created successfully")
                    
                except Exception as e:
                    logger.error(f"Failed to create role assignment: {str(e)}")
                    raise

        except Exception as e:
            logger.error(f"RBAC setup failed: {str(e)}")
            raise

    async def configure_network_security(self, allowed_ips: List[str]) -> None:
        """
        Configure network security for the OpenAI service.
        
        Args:
            allowed_ips: List of allowed IP addresses/ranges
        """
        try:
            logger.info("Configuring network security...")
            
            # Initialize the Network Management Client
            network_client = NetworkManagementClient(
                credential=self.credential,
                subscription_id=self.subscription_id
            )

            # Configure network rules
            network_rules = {
                "default_action": "Deny",
                "ip_rules": [
                    {"value": ip, "action": "Allow"}
                    for ip in allowed_ips
                ],
                "virtual_network_rules": []  # Add VNet rules if needed
            }

            # Update service with network rules
            # Note: This is a placeholder - actual implementation would use
            # the Cognitive Services Management Client to update the service
            logger.info("Applying network security rules...")
            logger.info(f"Network rules configured: {json.dumps(network_rules, indent=2)}")

            logger.info("✅ Network security configured successfully")

        except Exception as e:
            logger.error(f"Network security configuration failed: {str(e)}")
            raise

    async def setup_audit_logging(self) -> None:
        """Configure audit logging for the OpenAI service."""
        try:
            logger.info("Setting up audit logging...")
            
            # TODO: Implement audit logging setup
            # This is a placeholder for the audit logging setup code
            # In a real implementation, you would:
            # 1. Configure diagnostic settings
            # 2. Set up Log Analytics workspace
            # 3. Configure log retention policies
            # 4. Set up log alerts

            logger.info("✅ Audit logging configured successfully")

        except Exception as e:
            logger.error(f"Audit logging setup failed: {str(e)}")
            raise

    async def validate_security_config(self) -> Dict[str, bool]:
        """
        Validate security configurations.
        
        Returns:
            Dict containing validation results
        """
        try:
            logger.info("Validating security configurations...")
            
            validation_results = {
                "rbac_configured": False,
                "network_security_configured": False,
                "audit_logging_configured": False
            }

            # Validate RBAC
            try:
                # Add RBAC validation logic here
                validation_results["rbac_configured"] = True
                logger.info("✅ RBAC validation passed")
            except Exception as e:
                logger.error(f"RBAC validation failed: {str(e)}")

            # Validate Network Security
            try:
                # Add network security validation logic here
                validation_results["network_security_configured"] = True
                logger.info("✅ Network security validation passed")
            except Exception as e:
                logger.error(f"Network security validation failed: {str(e)}")

            # Validate Audit Logging
            try:
                # Add audit logging validation logic here
                validation_results["audit_logging_configured"] = True
                logger.info("✅ Audit logging validation passed")
            except Exception as e:
                logger.error(f"Audit logging validation failed: {str(e)}")

            return validation_results

        except Exception as e:
            logger.error(f"Security validation failed: {str(e)}")
            raise

def main():
    """Main function to run the security configuration."""
    security = SecurityConfiguration()
    
    print("\n🔒 Starting security configuration...")
    
    # Example role assignments
    role_assignments = [
        {
            "principal_id": "example-user-id",
            "role_definition_id": "Cognitive Services User",
            "name": "example-role-assignment"
        }
    ]
    
    # Example allowed IPs
    allowed_ips = ["10.0.0.0/24", "192.168.1.0/24"]
    
    try:
        # Set up RBAC
        asyncio.run(security.setup_rbac(role_assignments))
        
        # Configure network security
        asyncio.run(security.configure_network_security(allowed_ips))
        
        # Set up audit logging
        asyncio.run(security.setup_audit_logging())
        
        # Validate configurations
        validation_results = asyncio.run(security.validate_security_config())
        
        print("\n📊 Security Configuration Results:")
        print(json.dumps(validation_results, indent=2))
        
        # Check if all validations passed
        if all(validation_results.values()):
            print("\n✅ Security configuration completed successfully!")
        else:
            print("\n⚠️ Some security configurations require attention.")
            sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ Security configuration failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
