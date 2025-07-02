import os
import requests
import click
import getpass

@click.command()
@click.option('--pat', prompt='GitHub Personal Access Token', hide_input=True, help='A GitHub PAT with app creation permissions')
def main(pat):
    """Onboard: Register a GitHub App and write credentials to .env."""
    print("Step 1: Go to https://github.com/settings/apps/new to create a new GitHub App.")
    manifest_code = click.prompt("Paste the 'Manifest code' from GitHub here")
    headers = {"Authorization": f"token {pat}", "Accept": "application/vnd.github+json"}
    resp = requests.post(f"https://api.github.com/app-manifests/{manifest_code}/conversions", headers=headers)
    if resp.status_code != 201:
        print("Error creating GitHub App. Check your manifest code and PAT.")
        exit(1)
    data = resp.json()
    app_id = data.get("id")
    client_id = data.get("client_id")
    webhook_secret = getpass.getpass("Enter a webhook secret (or leave blank to generate): ") or os.urandom(16).hex()
    private_key = data.get("pem")
    print(f"\nApp ID: {app_id}\nClient ID: {client_id}\nWebhook Secret: {webhook_secret}")
    # Write to .env if not present
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write(f"GH_APP_ID={app_id}\n")
            f.write(f"GH_CLIENT_ID={client_id}\n")
            f.write(f"WEBHOOK_SECRET={webhook_secret}\n")
            f.write(f"GH_APP_PK={private_key.replace('\n', '')}\n")
        print("\nCredentials written to .env. Please review and restart your app if running.")
    else:
        print(".env already exists. Not overwriting.")

if __name__ == "__main__":
    main() 