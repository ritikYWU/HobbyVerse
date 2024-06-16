from flask import Blueprint, render_template, request
import re

from src.core.prompts import questions, get_prompt
from src.core.gemini import gemini_response

bp = Blueprint("pages", __name__)

def format_response(res):
    """Fromats gemini response in dict"""
    ans = {}
    tittle_pattern = r'\*\*(.*?)\:\*\*'
    desc_pattern = r'\:\*\*([^\n]*)'

    titles = re.findall(tittle_pattern, res)
    descriptions = re.findall(desc_pattern, res)
    ans[titles[0]] = [titles[1], descriptions[1]]
    ans[titles[2]] = [ [i, x] for i, x in zip(titles[3:], descriptions[3:])]

    return ans


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

        prompt = get_prompt([ans1, ans2, ans3, ans4, ans5])
        response = gemini_response(prompt)
        formatted_res = format_response(response)

    return render_template("pages/hobby.html", res=formatted_res)