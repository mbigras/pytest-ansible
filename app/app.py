from flask import Flask
import os

__version__ = "0.0.1"

app = Flask(__name__)

@app.route("/")
def up():
    return "up\n"


@app.route("/version")
def version():
    return f"{__version__}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
