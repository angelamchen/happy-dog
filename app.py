from flask import Flask, render_template
import os
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_dog():
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    payload = json.loads(r.text)

    if payload['status'] == "success":
        return render_template(
            'index.html',
            image=payload['message']
        )
    else:
        return render_template(
            error.html
        )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    
    
# import request

# response = requests.get("...")
# response.status_code
# payload = response.json();

# obj = json.loads(payload)

# ob['field']

params = {
    "thing": asdasd,
    "thing": asdasd
}

r = requests.get("url", params=params)
