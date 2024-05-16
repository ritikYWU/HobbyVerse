from flask import Blueprint, render_template

from src.core.prompts import questions
from src.core.gemini import main

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/explore")
def explore():
    ques = questions()
    print(ques)
    # res = main()
    res = '''**Suitable Hobby Recommendation:** **Indoor Fitness Routine** * Engage in bodyweight exercises such as push-ups, squats, and jumping jacks. * Follow guided workouts from free online platforms like YouTube or apps like Sweat or BetterMe. * Dedicate 15-20 minutes per session to de-stress and improve physical well-being. **Related Hobbies:** * **Yoga or Pilates:** Focus on flexibility, balance, and core strength while improving mindfulness. * **Tai Chi or Qi Gong:** Ancient mind-body practices that promote relaxation, improve circulation, and enhance balance. * **Meditation or Deep Breathing Exercises:** Dedicate a few minutes to practice mindfulness, reduce stress, and calm the mind. * **Indoor Walking or Jogging:** Utilize a treadmill or designated walking area indoors to get some cardio and release endorphins. * **Dancing to Music:** Put on some upbeat music and dance freely to decompress and increase heart rate.'''
    return render_template("pages/explore.html", question = ques, res=res)