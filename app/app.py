from flask import Flask, jsonify, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python CI/CD Demo</title>
    </head>
    <body>
        <h1 id="title">Python CI/CD Demo</h1>

        <p id="message">
            Application Python fonctionnelle
        </p>

        <button id="hello-button" onclick="sayHello()">
            Say Hello
        </button>

        <p id="result"></p>

        <script>
            function sayHello() {
                document.getElementById("result").innerText =
                    "Hello from Selenium!";
            }
        </script>
    </body>
    </html>
    """)


@app.route("/api/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "python-ci-cd"
    })


@app.route("/api/users")
def users():
    return jsonify([
        {
            "id": 1,
            "name": "Ay mane"
        },
        {
            "id": 2,
            "name": "Test User"
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)