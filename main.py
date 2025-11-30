from chatbot.model import CollegeChatbot
from chatbot.small_talk import handle_small_talk

FAQ_FILE = "data/faq_data.json"


def main():
    print("==============================================")
    print("     College Query Chatbot - NLP Project      ")
    print("==============================================")
    print("Type your question below. Type 'exit' to quit.\n")

    bot = CollegeChatbot(FAQ_FILE)

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break

        small = handle_small_talk(user_input)
        if small:
            print("Bot:", small)
            continue

        answer = bot.get_answer(user_input)
        print("Bot:", answer)


if __name__ == "__main__":
    main()
