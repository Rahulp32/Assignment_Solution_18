from flask import Flask

app = Flask(__name__)

@app.route("/")
def company_info():
    return """
    <h1>Company Name: ABC Corporation</h1>
    <p>Location: India</p>
    <p>Contact Detail: 999-999-9999</p>
    """

@app.route("/welcome")
def welcome():
    return "Welcome to ABC Corporation"

if __name__ == "__main__":
    app.run(debug=True)
