from flask import Flask, request, render_template_string

app = Flask(__name__)

users = {"admin": "admin@example.com"}  # Simulated database

VULNERABLE_HTML = """
<!DOCTYPE html>
<html>
<head><title>Change Email</title></head>
<body>
    <h2>Change Email</h2>
    <form action="/change_email" method="POST">
        <input type="hidden" name="username" value="admin">
        <label>New Email:</label>
        <input type="email" name="email">
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(VULNERABLE_HTML)


@app.route("/change_email", methods=["POST"])
def change_email():
    username = request.form.get("username")
    email = request.form.get("email")

    if username in users:
        users[username] = email
        return f"Email changed to {email}"
    return "User not found", 400


if __name__ == "__main__":
    app.run(debug=True, port=7777)
