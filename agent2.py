from langchain_core.messages import SystemMessage, AIMessage, HumanMessage


messages = [
    SystemMessage(content="dummy AI"),
    HumanMessage(content="Hi, Who Are you?"),
    AIMessage(content="Hi, I am an large language model built by OpenAI"),
]



for m in messages:
    m.pretty_print()