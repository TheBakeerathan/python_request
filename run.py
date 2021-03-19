import os
import requests

path = "./feedback/"
feedback_dict = {}
upload_url = "https://example.com"

for file in os.listdir(path):
    print(file)
    with open(path+file,'r') as current_file:
        feedback_dict["title"] = current_file.readline().rstrip()
        feedback_dict["name"] = current_file.readline().rstrip()
        feedback_dict["date"] = current_file.readline().rstrip()
        feedback_dict["feedback"] = current_file.readline().rstrip()
        print(feedback_dict)


        response = requests.post(upload_url,data=feedback_dict)
        print("Status Code: " + str(response.status_code))