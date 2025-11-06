# Simple math quiz
import random

questions = ["5 + 3", "9 - 4", "6 x 2"]
for q in questions:
    print(f"What is {q}?")
    ans = input("Answer: ")
    print("✅ Correct!" if eval(q.replace('x','*')) == int(ans) else "❌ Wrong")