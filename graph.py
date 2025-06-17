from pyasn1_modules.rfc2315 import EncryptedDigest
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langgraph.graph import START, END, StateGraph
from langgraph. types import Send

from schemas import *
from prompts import *
from dotenv import load_dotenv
import os

from tavily import TavilyClient

load_dotenv()
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

# Modelos
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPEN_API_KEY)
reasoning_llm = ChatOpenAI(model="o4-mini", api_key=OPEN_API_KEY)

# Nos
def build_first_queries(state: ReportState):
    class QueryList(BaseModel):
        queries: List[str]

    user_input = state.user_input
    prompt =  build_queries.format(user_input=user_input)
    query_llm = llm.with_structured_output(QueryList)
    result = query_llm.invoke(prompt)
    return {"queries":result.queries}

def search_tavily(query: str):
    tavily_client = TavilyClient()
    results = tavily_client.search(query, max_results=1, include_raw_content=False)
    url = results["results"][0]["url"]
    url_extraction = tavily_client.extract(url)
    if (len(url_extraction["results"])>0):
        raw_content = url_extraction["results"][0]["raw_content"]


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

