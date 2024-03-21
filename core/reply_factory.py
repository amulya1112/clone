
from .constants import BOT_WELCOME_MESSAGE, PYTHON_QUESTION_LIST


def generate_bot_responses(message, session):
    bot_responses = []

    current_question_id = session.get("current_question_id")
    if not current_question_id:
        bot_responses.append(BOT_WELCOME_MESSAGE)

    success, error = record_current_answer(message, current_question_id, session)

    if not success:
        return [error]

    next_question, next_question_id = get_next_question(current_question_id)

    if next_question:
        bot_responses.append(next_question)
    else:
        final_response = generate_final_response(session)
        bot_responses.append(final_response)

    session["current_question_id"] = next_question_id
    session.save()

    return bot_responses


def record_current_answer(answer, current_question_id, session):
    '''
    Validates and stores the answer for the current question to django session.
    '''
  
    if answer:
        
        session["answers"][current_question_id] = answer
        return True, ""
    else:
        return False, "Invalid answer provided."


def get_next_question(current_question_id):
    '''
    Get the next question based on the current question ID.
    '''

    next_question = "What is your favorite programming language?"
    next_question_id = 2
    return next_question, next_question_id

def generate_final_response(session):
    '''
    Generate final response based on all the answers.
    '''
   
    final_response = "Thank you for answering all the questions!"
    return final_response
