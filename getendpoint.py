import runpod
import os

# Set your API key
runpod.api_key = "rpa_ZS8OMILJDSU0UP3PCTDG3VZ5QEUYLKTRDJZEU09Z966i20"

# Fetch all available endpoints
endpoints = runpod.get_endpoints()

# Print endpoint IDs and names
for endpoint in endpoints:
    print(f"ID: {endpoint['id']}, Name: {endpoint['name']}")