import RPi.GPIO as GPIO
import time

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)
# 设置GPIO17和GPIO18为输出模式
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def quiz():
    print("Welcome to the Python Knowledge Quiz!")
    print("Answer the following questions:")
    # Questions and Answers
    questions = ["1) Which of the following is NOT a python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool",
                 "2) Which of the following is NOT a built-in operation in Python?\na) +\nb) %\nc) abs()\nd) sqto",
                 "3) In a mixed-type expression involving ints and floats, Python will convert:\na) floats to ints\nb) ints to strings\nc) floats and ints to strings\nd) ints to floats",
                 "4)The best structure for implementing a multi-way decision in Python is:\na) if\nb) if-else\nc) if-elif-else\nd) try",
                 "5)What statement can be executed in the body of a loop to cause it to terminate?\na) if\nb) exit\nc) continue\nd) break"]
    answers = ["c", "d", "d", "c", "d"]
    score = 0

    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            # 点亮绿灯表示回答正确
            GPIO.output(17, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(17, GPIO.LOW)
            score += 1
        else:
            print("Incorrect!")
            # 点亮红灯表示回答错误
            GPIO.output(18, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18, GPIO.LOW)

    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")
    # 清理GPIO资源
    GPIO.cleanup()


# Run the quiz function
quiz()
