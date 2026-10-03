import json

from fastapi import APIRouter
from pydantic import BaseModel
from langchain_core.messages import ToolMessage

from ..ai.graph import graph


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    message: str


@router.post("/")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.message
                }
            ]
        }
    )

    final_response = result["messages"][-1].content

    interaction = None

    for message in result["messages"]:

        if isinstance(message, ToolMessage):

            try:
                tool_data = json.loads(message.content)

            except (json.JSONDecodeError, TypeError):
                continue


            # Case 1:
            # get_interaction returns directly
            if (
                isinstance(tool_data, dict)
                and "id" in tool_data
            ):
                interaction = tool_data


            # Case 2:
            # edit/log/schedule return inside interaction key
            elif (
                isinstance(tool_data, dict)
                and "interaction" in tool_data
                and isinstance(tool_data["interaction"], dict)
            ):
                interaction = tool_data["interaction"]


    return {
        "response": final_response,
        "interaction": interaction
    }