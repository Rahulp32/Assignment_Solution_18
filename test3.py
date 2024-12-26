from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the Home Page"

@app.route("/about")
def about():
    return "This is the About Page"

@app.route("/links")
def links():
    home_url = url_for("home")
    about_url = url_for("about")
    return f"""
    <p>Home URL: <a href="{home_url}">{home_url}</a></p>
    <p>About URL: <a href="{about_url}">{about_url}</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)
