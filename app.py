from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "Satheesh")
    return f"""
    <html>
      <head>
        <title>Employee Application</title>
      </head>
      <body>
        <h1>Welcome to Employee Application</h1>
        <h2>OpenShift End-to-End Project</h2>
        <p>Environment: {environment}</p>
        <p>Application is running successfully!</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
