from langchain_core.messages import SystemMessage, AIMessage, HumanMessage


messages = [
    SystemMessage(content="dummy AI"),
    HumanMessage(content="Hi, Who Are you?"),
    AIMessage(content="Hi, I am an large language model built by OpenAI"),
]

print("Hi I am Ganesh, Your Python Buddy. I'm writing PR4. which is going to merge before PR3.")