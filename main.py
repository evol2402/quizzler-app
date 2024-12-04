from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

def main():
    try:
        # Create a list of Question objects from the question data
        question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)

        # Instantiate QuizBrain with the list of questions
        quiz = QuizBrain(question_bank)

        # Set up the quiz interface
        quiz_ui = QuizInterface(quiz_brain=quiz)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Print the final score when the quiz is completed
        print("You've completed the quiz")
        print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if __name__ == "__main__":
    main()
