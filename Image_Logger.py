import requests

# Replace this with your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1351323798330277960/p2eQzB6sw4cepRorvi71v8tKs6fgYZcInD-lkaxzkRM8fKyC9HjuGc3CQAsU4sHoVjub"

def get_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        response.raise_for_status()
        return response.json().get("ip")
    except requests.RequestException as e:
        return f"Error: {e}"

def send_to_webhook(ip):
    data = {
        "content": f"Public IP: {ip}"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        response.raise_for_status()
        print("IP sent successfully!")
    except requests.RequestException as e:
        print(f"Failed to send IP: {e}")

if __name__ == "__main__":
    ip = get_ip()
    send_to_webhook(ip)
