import os
import requests
import getpass

GITHUB_API = "https://api.github.com/app-manifests"

# Step 1: Prompt user for GitHub manifest code
print("Step 1: Go to https://github.com/settings/apps/new to create a new GitHub App.")
manifest_code = input("Paste the 'Manifest code' from GitHub here: ")

# Step 2: Exchange manifest code for app credentials
resp = requests.post(f"{GITHUB_API}/{manifest_code}/conversions")
if resp.status_code != 201:
    print("Error creating GitHub App. Check your manifest code.")
    exit(1)
data = resp.json()

app_id = data.get("id")
client_id = data.get("client_id")
webhook_secret = getpass.getpass("Enter a webhook secret (or leave blank to generate): ") or os.urandom(16).hex()
private_key = data.get("pem")

print("\nStep 2: App created!")
print(f"App ID: {app_id}")
print(f"Client ID: {client_id}")
print(f"Webhook Secret: {webhook_secret}")

# Step 3: Write to .env
with open(".env", "a") as f:
    f.write(f"GH_APP_ID={app_id}\n")
    f.write(f"GH_CLIENT_ID={client_id}\n")
    f.write(f"WEBHOOK_SECRET={webhook_secret}\n")
    f.write(f"GH_APP_PK={private_key.replace('\n', '')}\n")

print("\nStep 3: Credentials written to .env. Please review and restart your app if running.") 