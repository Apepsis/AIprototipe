from core.agent import LocalAgent


agent = LocalAgent()


if __name__ == "__main__":

    print("Local AI Agent started")
    print("Type 'salir' to exit")

    while True:

        question = input("\nTú: ")

        if question.lower() == "salir":
            break

        response = agent.run(question)

        print("\nIA:")
        print(response)
