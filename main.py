from flask import Flask, jsonify
import os
import torch
import io
import requests

app = Flask(__name__)


@app.route('/')
def index():
    urlModelo="https://firebasestorage.googleapis.com/v0/b/proyecto1-1323e.appspot.com/o/files%2Fmodelo_0.pth?alt=media&token=ffc303b3-62b4-4eb4-a9a5-895c93134f39"
    
    # Download the .pth file
    response = requests.get(urlModelo)
    response.raise_for_status()

    buffer = io.BytesIO(response.content)
    
    net=torch.load(buffer)
    refInfo=f"${net}"
    return jsonify({"modelo": refInfo})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
