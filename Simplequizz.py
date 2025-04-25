# Simple Quiz App (Improved)

questions = [
    {
        "question": "What is the capital of France?",
        "options": {
            "A": "Paris",
            "B": "London",
            "C": "Berlin",
            "D": "Madrid"
        },
        "answer": "A"
    },
    {
        "question": "What is 5 + 7?",
        "options": {
            "A": "10",
            "B": "11",
            "C": "12",
            "D": "13"
        },
        "answer": "C"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": {
            "A": "Charles Dickens",
            "B": "William Shakespeare",
            "C": "Mark Twain",
            "D": "Jane Austen"
        },
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "A": "Earth",
            "B": "Venus",
            "C": "Jupiter",
            "D": "Mars"
        },
        "answer": "D"
    }
]

score = 0

print("🧠 Welcome to the Quiz!\n")

for q in questions:
    print(q["question"])
    for key, value in q["options"].items():
        print(f"{key}. {value}")

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        correct_option = q["options"][q["answer"]]
        print(f"❌ Wrong! Correct answer: {q['answer']}. {correct_option}\n")

print(f"🎉 Quiz completed! You got {score} out of {len(questions)} correct.")
print("Thank you for playing!")