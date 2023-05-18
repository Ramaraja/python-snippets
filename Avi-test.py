import requests
import json

controller_ip = 'your_controller_ip'
username = 'your_username'
password = 'your_password'

# Authenticate and get the session token
auth_data = {
    'username': username,
    'password': password
}
auth_url = f'https://{controller_ip}/login'
response = requests.post(auth_url, data=json.dumps(auth_data), verify=False)
if response.status_code != 200:
    print('Authentication failed')
    exit(1)

session_token = response.json()['token']
headers = {
    'X-Avi-Version': '18.2.9',  # Specify your Avi Controller version here
    'Content-Type': 'application/json',
    'X-Avi-Tenant': 'admin',
    'Authorization': f'Avi-v1; token="{session_token}"'
}

# Get all virtual services
vs_url = f'https://{controller_ip}/api/virtualservice'
response = requests.get(vs_url, headers=headers, verify=False)
if response.status_code != 200:
    print('Failed to fetch virtual services')
    exit(1)

virtual_services = response.json()['results']

# Process virtual services
for vs in virtual_services:
    vip = vs['ip_address']['addr']
    status = vs['runtime']['oper_status']['state']
    print(f'Virtual Service: {vs["name"]}\nVIP: {vip}\nStatus: {status}\n{"-" * 20}')

# Logout
logout_url = f'https://{controller_ip}/logout'
requests.get(logout_url, headers=headers, verify=False)
