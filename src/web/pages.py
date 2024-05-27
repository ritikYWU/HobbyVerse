from flask import Blueprint, render_template, request

from src.core.prompts import questions, get_prompt
from src.core.gemini import gemini_response

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/explore", methods=['GET', 'POST'])
def explore():
    ques = questions()
    return render_template("pages/explore.html", question = ques)

@bp.route("/hobby", methods=['GET', 'POST'])
def hobby():
    if request.method == 'POST':
        ans1 = request.form.get('ques1')
        ans2 = request.form.get('ques2')
        ans3 = request.form.get('ques3')
        ans4 = request.form.get('ques4')
        ans5 = request.form.get('ques5')

        print(f"Question 1: {ans1}\nQuestion 2: {ans2}\nQuestion 3: {ans3}\nQuestion 4: {ans4}\nQuestion 5: {ans5}\n")

        prompt = get_prompt([ans1, ans2, ans3, ans4, ans5])
        response = gemini_response(prompt)

    
    return render_template("pages/hobby.html", prompt=response)