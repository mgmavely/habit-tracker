import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.environ.get("USERNAME")

user_params = {
    "token": os.environ.get("TOKEN"),
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "min",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": os.environ.get("TOKEN")
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.now()


pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "24",
}

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20210216"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)

