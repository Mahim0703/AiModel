import requests

url = "https://api.deepseek.com/v3/chat"  # Confirm this is the correct endpoint
headers = {
    "Authorization": "Bearer 2uRvDxd3yZLjWMT8SXj6hcKPpB8JCp2RRGPw52yLJqLjxI5gylvNJQQJ99BDACHYHv6XJ3w3AAAAACOGVxdl",
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-chat-v3",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
}

response = requests.post(url, headers=headers, json=data)
print("Status Code:", response.status_code)
print("Response:", response.text)
