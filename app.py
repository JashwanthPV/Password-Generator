from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, uppercase, lowercase, digits, special_chars):
    """Generate a random password based on user preferences."""
    char_pool = ""
    if uppercase:
        char_pool += string.ascii_uppercase
    if lowercase:
        char_pool += string.ascii_lowercase
    if digits:
        char_pool += string.digits 
    if special_chars:
        char_pool += string.punctuation
    if char_pool =="":
        return "Error: Please select at least one character type."
    password = ''.join(random.choices(char_pool,k=length))
    return password

@app.route("/", methods=["GET","POST"])
def index():
    password =""
    if request.method=="POST":
        length=int(request.form.get("length",8))
        uppercase = "uppercase" in request.form
        lowercase ="lowercase" in request.form
        digits = "digits" in request.form
        special_chars="special_chars" in request.form

        password=generate_password(length, uppercase,lowercase,digits,special_chars)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)