import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import StateGraph, START, MessagesState
from langchain_core.messages import SystemMessage

from .tools import (
    log_interaction,
    get_interaction,
    edit_interaction,
    schedule_follow_up,
    get_hcp_interaction_history
)


load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


tools = [
    log_interaction,
    get_interaction,
    edit_interaction,
    schedule_follow_up,
    get_hcp_interaction_history
]


llm_with_tools = llm.bind_tools(
    tools,
    tool_choice="auto"
)


SYSTEM_PROMPT = """
You are an AI assistant for an HCP CRM system.

Use available tools whenever the user requests CRM actions.

Rules:

- For a specific numeric interaction ID, use get_interaction.
- For HCP names or history questions, use get_hcp_interaction_history.
- To create a new interaction, use log_interaction.
- To modify an existing interaction, use edit_interaction.
- To schedule follow-ups, use schedule_follow_up.

IMPORTANT TOOL RULES:

- Interaction IDs must always be real numeric IDs.
- Never pass phrases such as:
  "result of previous function call"
  "previous result"
  "tool output"
  as a parameter value.
- When using edit_interaction or schedule_follow_up,
  use only the numeric interaction ID returned by a previous tool.
- If you do not have an interaction ID, ask the user.
- Never invent CRM fields.
- Only report information returned by tools.
- If a field is empty, say it is not recorded.

After receiving tool results, explain them clearly.
"""


def chatbot(state: MessagesState):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"]
    ]

    response = llm_with_tools.invoke(messages)

    return {
        "messages": [response]
    }


graph_builder = StateGraph(MessagesState)

graph_builder.add_node(
    "chatbot",
    chatbot
)

graph_builder.add_node(
    "tools",
    ToolNode(tools)
)

graph_builder.add_edge(
    START,
    "chatbot"
)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

graph_builder.add_edge(
    "tools",
    "chatbot"
)

graph = graph_builder.compile()