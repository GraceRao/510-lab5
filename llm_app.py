import requests
import os
from dotenv import load_dotenv

load_dotenv()

# st.set_page_config(
#     page_title="Book Search & Filter App",
#     page_icon="📚",
#     layout="centered",
# )

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

data = {
    "contents":[
        {
            "parts":[
                {"text":"Write a story about a magic backpack"}
            ]
        }
    ]
}

res = requests.post(
    URL,
    headers={
        "Content-Type": "application/json" # tell the server we are sending JSON
    }, 
    json = data,
    params = {"key": os.getenv("GOOGLE_API_KEY")}
)

json_res = res.json()
#print(json_res)

joke = json_res["contents"][0]["parts"][0]["text"]
print(joke)
