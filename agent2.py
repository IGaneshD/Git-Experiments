from langchain_core.messages import SystemMessage, AIMessage, HumanMessage


messages = [
    SystemMessage(content="dummy AI"),
    HumanMessage(content="Hi, Who Are you?"),
    AIMessage(content="Hi, I am an large language model built by OpenAI"),
]

print("Hi I am Ganesh, Your Python Buddy. I am an expert python developer. This is PR3")


for m in messages:
    m.pretty_print()