from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def get_response(user_input):
    user_input = user_input.lower()

    if "admission" in user_input:
        return "Admissions are open from June to August."
    elif "deadline" in user_input:
        return "The last date to apply is 31st August."
    elif "programs" in user_input:
        return "We offer BSCS, BBA, and Engineering programs."
    elif "fee" in user_input:
        return "The average semester fee is 50,000 PKR."
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you with admissions?"
    else:
        return "Sorry, I don't understand. Please ask about admissions, programs, or deadlines."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_input = request.form["msg"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)