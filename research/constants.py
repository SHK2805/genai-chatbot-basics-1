from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import MessagesPlaceholder

user_message1: str = "Hello. My name is Test1"
chat_messages1 = [
        HumanMessage(content="Hello. My name is Test1"),
        HumanMessage(content="I am a Data Scientist."),
        AIMessage(content="Hello Test1. How can I help you?"),
        HumanMessage(content="I am looking for a job."),
        AIMessage(content="What type of job are you looking for?"),
        HumanMessage(content="I am looking for a data scientist job."),
        AIMessage(content="What type of data scientist job are you looking for?"),
        HumanMessage(content="I am looking for a data scientist job in the field of AI."),
        AIMessage(content="What type of AI job are you looking for?"),
        HumanMessage(content="I am looking for a Generative AI data scientist job."),
        HumanMessage(content="Can you give what is technologies I need to learn to get a Generative AI data scientist job."),
    ]

chat_messages2 = [
        HumanMessage(content="Hello. My name is Test2"),
        HumanMessage(content="I am a Chef."),
        AIMessage(content="Hello Test2. How can I help you?"),
        HumanMessage(content="I am looking to open a Indian Street Food restaurant."),
        AIMessage(content="That's exciting!  Indian street food is so flavorful and popular. \n\nTo help me give you the best advice, could you tell me a little more about what you have in mind? For example:\n\n* **What type of Indian street food are you most interested in specializing in?** (e.g., North Indian, South Indian, specific dishes like chaat or dosa)\n* **What is your target audience?** (e.g., families, young professionals, students)\n* **Do you have a location in mind?** (This can help determine the type of menu and pricing)\n* **What kind of help are you looking for?** (e.g., menu ideas, marketing tips, advice on sourcing ingredients) \n\n\nThe more details you can share, the better I can assist you. 😊  \n"),
        HumanMessage(content="I am looking to open a Indian Street Food restaurant that specializes in south indian street food including breakfasts like dosa, idli and fast foods like dosa, pani puri. It will cater to all age groups including families, young professionals and students. I am looking for help in menu ideas."),
    ]

system_prompt = [
                ("system", "You are a helpful assistant."),
                ("system", "Answer all the questions to the best of your ability."),
                ("system", "If you don't know the answer, say 'I don't know'."),
                ("system", "If you don't understand the question, say 'I don't understand'."),
                ("system", "If you need more information, ask for it."),
                ("system", "If you are not sure about something, say 'I'm not sure'."),
                (MessagesPlaceholder(variable_name="messages")),
            ]
config1 = {"configurable": {"session_id": "test1"}}