### Steps:
    Create a Flask web app that allows a user to change their email.
    The form submission will be vulnerable because it doesn't use CSRF protection.
    You'll then craft a malicious HTML page to exploit the vulnerability.


### How to Test:
Run app.py with python app.py.
Open http://127.0.0.1:5000/ in your browser and manually change the email.
Open exploit.html in your browser. The CSRF attack will automatically submit the form.
Check the Flask app logs—you should see that the email has been changed without user interaction.