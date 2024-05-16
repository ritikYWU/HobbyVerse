

def prompt(user_answer: list) -> str:
    gemini_prompt = f'''Given someone who enjoys {user_answer[0]} activities, has {user_answer[1]} a week to dedicate, and wants to {user_answer[2]}, prefers to do activities {user_answer[3]}, and has a preference for {user_answer[4]} hobbies, what is a suitable hobby recommendation? Additionally, suggest 3-5 related hobbies.
    '''

    return gemini_prompt


def questions() -> list:
    """Returns list of questions"""
    questions_options = [
        {
            "question": "What kind of activity are you most interested in?",
            "options": [
                "Physical activity that gets me moving (e.g., running, dancing)",
                "Creative or artistic activities that allow me to express myself (e.g., painting, writing)",
                "Intellectual activities that challenge my mind (e.g., learning a new language, coding)",
                "Social activities that involve connecting with others (e.g., board games, book clubs)"
            ]
        },
        {
            "question": "How much time are you realistically willing to dedicate to a hobby each week?",
            "options": [
                "Less than 30 minutes",
                "30 minutes to 1 hour",
                "1-2 hours",
                "2+ hours"
            ]
        },
        {
            "question": "What is your primary goal for taking up a new hobby?",
            "options": [
                "To relax and de-stress after work",
                "To learn a new skill or gain knowledge",
                "To meet new people and socialize",
                "To improve my physical health and fitness"
            ]
        },
        {
            "question": "Where would you prefer to do your hobbies?",
            "options": [
                "Indoors",
                "Outdoors",
                "No preference"
            ]
        },
        {
            "question": "What is your budget preference for hobbies?",
            "options": [
                "Free (no cost involved)",
                "Low-cost (requires minimal spending)",
                "Open to any cost"
            ]
        }
    ]

    return questions_options
