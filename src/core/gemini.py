import google.generativeai as genai
from dotenv import load_dotenv

from prompts import prompt, questions

def setup_gemini():
    load_dotenv()

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY) 
    model = genai.GenerativeModel('gemini-pro')

    return model

def gemini_response(user_answer):
    model = setup_gemini()

    gemini_prompt = prompt(user_answer)

    print(gemini_prompt)
    
    response = model.generate_content(gemini_prompt)
    print('\n\n\n')

    print(response.text)


def ask_questiosn():
    user_answer = []
    questions_options = questions()

    for index, question in enumerate(questions_options, start=1):
        print(f"{index}. {question['question']}")
        for index, option in enumerate(question['options'], start=1):
            print(f'\t{index}. {option}')
        
        answer = int(input())
        user_answer.append(question['options'][answer-1])

    return user_answer

def main():
    qa = ask_questiosn()
    gemini_response(qa)

if __name__ == "__main__":
    main()