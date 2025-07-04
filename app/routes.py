from flask import Blueprint, render_template, request
from .gemini_api import analyze_request
import markdown

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    result = None
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            raw_result = analyze_request(user_input)
            result = markdown.markdown(raw_result)

    return render_template("index.html", result=result, user_input=user_input)
