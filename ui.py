from tkinter import *
from quiz_brain import QuizBrain

FONT = ("Arial", 20, "italic")
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, font=("Arial", 20, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.ques_text = self.canvas.create_text(150, 125, text="Quizler", font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, command=self.true_pressed, highlightthickness=0)
        self.true_button.grid(row=2, column=1)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, command=self.false_pressed, highlightthickness=0)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.ques_text, text="Thanks for playing!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
