from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from groq import Groq as _Groq


client = _Groq(api_key = "api_key")



# Web search agent
web_search_agent= Agent(
    name = "Web search Agent",
    role = "Search the web for the information",
    model =_Groq (id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions  = ["Always incluse source"],
    show_tools_calls = True,
    markdown = True 
)

##financial agent
finance_agent = Agent(
    name = "Finance AI Agent",
    model =_Groq (id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["USe tables to display the data"],
    show_tool_calls=True 
)

#multi model agent
multi_ai_agent = Agent(
    model =_Groq(id = "llama-3.3-70b-versatile"),
    team = [web_search_agent,finance_agent],
    instructions = ["Always include sources","USe tables to display the data"],
    show_tools_calls = True,
    markdown = True  
)

multi_ai_agent.print_response("Summaries analyst recommendation and share the latest news for NVDA", stream = True)