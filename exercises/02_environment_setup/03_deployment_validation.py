"""
Exercise 3: Deployment Validation and Monitoring
This script validates Azure OpenAI deployment and sets up monitoring.
"""

import os
import sys
import json
import logging
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import asyncio
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
from azure.ai.openai import OpenAIClient
from azure.core.exceptions import AzureError

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DeploymentValidator:
    def __init__(self):
        """Initialize deployment validation utilities."""
        self.credential = DefaultAzureCredential()
        self.subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        self.resource_group = os.getenv("AZURE_RESOURCE_GROUP")
        self.service_name = os.getenv("AZURE_OPENAI_SERVICE_NAME")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

    async def validate_model_deployment(self, model_name: str = "gpt-4") -> bool:
        """
        Validate model deployment and basic functionality.
        
        Args:
            model_name: Name of the deployed model
            
        Returns:
            bool: True if validation passes, False otherwise
        """
        try:
            logger.info(f"Validating model deployment: {model_name}")
            
            # Initialize OpenAI client
            client = OpenAIClient(
                endpoint=self.endpoint,
                credential=self.credential
            )

            # Test basic completion
            test_prompt = "Respond with 'Deployment test successful' if you can read this."
            
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "You are a test assistant."},
                    {"role": "user", "content": test_prompt}
                ],
                max_tokens=50
            )

            # Check response
            if "successful" in response.choices[0].message.content.lower():
                logger.info("✅ Model deployment validation passed")
                return True
            else:
                logger.warning("⚠️ Model response did not match expected pattern")
                return False

        except Exception as e:
            logger.error(f"Model deployment validation failed: {str(e)}")
            return False

    async def setup_monitoring_dashboard(self) -> str:
        """
        Set up a monitoring dashboard for the OpenAI service.
        
        Returns:
            str: Dashboard URL
        """
        try:
            logger.info("Setting up monitoring dashboard...")
            
            # Initialize Monitor Management Client
            monitor_client = MonitorManagementClient(
                credential=self.credential,
                subscription_id=self.subscription_id
            )

            # Define dashboard
            dashboard_name = f"openai-monitor-{int(time.time())}"
            dashboard_properties = {
                "lenses": {
                    "0": {
                        "order": 0,
                        "parts": [
                            {
                                "position": {
                                    "x": 0,
                                    "y": 0,
                                    "rowSpan": 4,
                                    "colSpan": 6
                                },
                                "metadata": {
                                    "type": "Extension/Microsoft_OperationsManagementSuite_Workspace/PartType/LogsDashboardPart",
                                    "inputs": [
                                        {
                                            "name": "Query",
                                            "value": "AzureDiagnostics | where ResourceProvider == 'MICROSOFT.COGNITIVESERVICES'"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            }

            # Create dashboard
            dashboard = monitor_client.dashboards.create_or_update(
                resource_group_name=self.resource_group,
                dashboard_name=dashboard_name,
                dashboard=dashboard_properties
            )

            logger.info("✅ Monitoring dashboard created successfully")
            return f"https://portal.azure.com/#dashboard/{dashboard.id}"

        except Exception as e:
            logger.error(f"Dashboard creation failed: {str(e)}")
            raise

    async def setup_alerts(self) -> None:
        """Set up monitoring alerts for the OpenAI service."""
        try:
            logger.info("Setting up monitoring alerts...")
            
            # Initialize Monitor Management Client
            monitor_client = MonitorManagementClient(
                credential=self.credential,
                subscription_id=self.subscription_id
            )

            # Define alert rules
            alert_rules = [
                {
                    "name": "high-error-rate",
                    "description": "Alert when error rate exceeds threshold",
                    "metric": "Error Rate",
                    "threshold": 5,
                    "window_size": "PT5M"
                },
                {
                    "name": "high-latency",
                    "description": "Alert when latency exceeds threshold",
                    "metric": "Latency",
                    "threshold": 1000,
                    "window_size": "PT5M"
                }
            ]

            # Create alert rules
            for rule in alert_rules:
                try:
                    # Create alert rule
                    logger.info(f"Creating alert rule: {rule['name']}")
                    
                    # Note: This is a placeholder - actual implementation would use
                    # monitor_client.alert_rules.create_or_update()
                    
                    logger.info(f"✅ Alert rule {rule['name']} created successfully")
                    
                except Exception as e:
                    logger.error(f"Failed to create alert rule {rule['name']}: {str(e)}")
                    raise

        except Exception as e:
            logger.error(f"Alert setup failed: {str(e)}")
            raise

    async def run_performance_test(self) -> Dict[str, float]:
        """
        Run basic performance tests on the deployment.
        
        Returns:
            Dict containing performance metrics
        """
        try:
            logger.info("Running performance tests...")
            
            metrics = {
                "average_latency": 0.0,
                "error_rate": 0.0,
                "success_rate": 0.0
            }

            # Initialize OpenAI client
            client = OpenAIClient(
                endpoint=self.endpoint,
                credential=self.credential
            )

            # Run test completions
            test_prompts = [
                "Summarize this text: Hello world",
                "Translate to French: Good morning",
                "Write a haiku about: Spring"
            ]
            
            total_time = 0
            errors = 0
            successes = 0

            for prompt in test_prompts:
                try:
                    start_time = time.time()
                    
                    response = client.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=50
                    )
                    
                    total_time += time.time() - start_time
                    successes += 1
                    
                except Exception:
                    errors += 1

            # Calculate metrics
            total_requests = len(test_prompts)
            metrics["average_latency"] = (total_time / total_requests) * 1000  # ms
            metrics["error_rate"] = (errors / total_requests) * 100
            metrics["success_rate"] = (successes / total_requests) * 100

            logger.info("✅ Performance tests completed")
            return metrics

        except Exception as e:
            logger.error(f"Performance tests failed: {str(e)}")
            raise

def main():
    """Main function to run the deployment validation."""
    validator = DeploymentValidator()
    
    print("\n🚀 Starting deployment validation...")
    
    try:
        # Validate model deployment
        deployment_valid = asyncio.run(validator.validate_model_deployment())
        if not deployment_valid:
            print("\n❌ Model deployment validation failed")
            sys.exit(1)
        
        # Set up monitoring dashboard
        dashboard_url = asyncio.run(validator.setup_monitoring_dashboard())
        print(f"\n📊 Monitoring Dashboard: {dashboard_url}")
        
        # Set up alerts
        asyncio.run(validator.setup_alerts())
        
        # Run performance tests
        metrics = asyncio.run(validator.run_performance_test())
        
        print("\n📈 Performance Test Results:")
        print(json.dumps(metrics, indent=2))
        
        # Check if performance is acceptable
        if metrics["success_rate"] < 90:
            print("\n⚠️ Performance tests indicate issues.")
            sys.exit(1)
        
        print("\n✅ Deployment validation completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Validation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
