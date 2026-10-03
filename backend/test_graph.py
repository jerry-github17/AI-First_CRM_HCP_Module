from app.ai.graph import graph
from langchain_core.messages import HumanMessage


response = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="Update interaction id 5 summary to discussed contract details with the HCP"
            )
        ]
    }
)


print(response["messages"][-1].content) 