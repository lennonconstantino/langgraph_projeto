from pyasn1_modules.rfc2315 import EncryptedDigest
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langgraph.graph import START, END, StateGraph
from langgraph. types import Send

from schemas import *
from prompts import *
from dotenv import load_dotenv
import os

load_dotenv()
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

# Modelos
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPEN_API_KEY)
reasoning_llm = ChatOpenAI(model="o4-mini", api_key=OPEN_API_KEY)

# Nos
def build_first_queries(state: ReportState):
    user_input = state.user_input
    prompt =  build_queries.format(user_input=user_input)
    return {""}

# Edges


# Grafo
builder = StateGraph(ReportState)
graph = builder.compile()

# execuçao
if __name__ == "__main__":
    user_input = """
    Quero que você me explicque o processo
    total para construir um agente de IA
    """
    graph.invoke({"user_input": user_input})

