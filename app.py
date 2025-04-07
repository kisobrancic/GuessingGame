from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        secret_number = request.cookies.get("secret_number")

        response = make_response(render_template("index.html"))
        if not secret_number:
            new_secret = random.randint(1, 20)
            response.set_cookie("secret_number", str(new_secret))

        return response
    else:
        guess = int(request.form.get("guess"))
        secret_number = int(request.cookies.get("secret_number"))

        if guess == secret_number:
            message = f"Yay, you guessed the secret mystery number. The secret number is {secret_number}"

            response = make_response(render_template("win.html", message=message))
            response.set_cookie("secret_number", str(random.randint(1, 20)))
            return response

        elif guess > secret_number:
            message = "Your guess is not correct, try with smaller numbers .."
            return render_template("index.html", message=message)

        elif guess < secret_number:            
            message = "Your guess is not correct, try with bigger numbers .."
            return render_template("index.html", message=message)
    

        return render_template("index.html")



if __name__ == "__main__":
    app.run()