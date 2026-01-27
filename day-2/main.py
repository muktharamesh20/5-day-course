#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
"""
Personal Agent Twin with Memory and Tools - Day 2
==================================================

This extends Day 1 by adding:
- Memory (Short-Term, Long-Term, Entity, Contextual)
- Tools from CrewAI collection
- Custom tool creation

Students: Follow the steps to add memory and tools to your agent!
"""

from crewai import Agent, Task, Crew, LLM
from crewai.tools import BaseTool
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool, WebsiteSearchTool, YoutubeVideoSearchTool, FirecrawlSearchTool, FirecrawlCrawlWebsiteTool, FirecrawlScrapeWebsiteTool, DallETool, PDFSearchTool
from pydantic import BaseModel, Field
from typing import Type
from dotenv import load_dotenv
import os

load_dotenv()

# ==============================================================================
# STEP 1: Configure your LLM (same as Day 1)
# ==============================================================================

llm = LLM(
    model="openai/gpt-4o-mini",
    temperature=0.7,
)

# ==============================================================================
# STEP 2: Define Tools
# ==============================================================================

# Tool 1: Directory Reading
# Allows agent to browse directories
docs_tool = DirectoryReadTool(directory='./blog-posts')

# Tool 2: File Reading
# Allows agent to read specific files
file_tool = FileReadTool()

# Tool 3: Website Search (RAG-based)
# Searches and extracts content from websites
web_rag_tool = WebsiteSearchTool()

# Tool 4: YouTube Video Search (RAG-based)
# Searches within video transcripts
youtube_tool = YoutubeVideoSearchTool()

crawl_tool = FirecrawlCrawlWebsiteTool(url='firecrawl.dev')

# Scrape single page
scrape_tool = FirecrawlScrapeWebsiteTool(url='firecrawl.dev')

# Search
firecrawl_search_tool = FirecrawlSearchTool(query='what is firecrawl?')
dalle_tool = DallETool(model="dall-e-3", size="1024x1024", quality="standard", n=1)
pdf_tool = PDFSearchTool()
# Tool 5: Web Search (requires SERPER_API_KEY in .env)
# Get free key at: https://serper.dev
search_tool = None
if os.getenv('SERPER_API_KEY'):
    search_tool = SerperDevTool()

# ==============================================================================
# STEP 3: Create Custom Tool
# ==============================================================================

class CalculatorInput(BaseModel):
    """Input schema for Calculator tool."""
    expression: str = Field(..., description="Mathematical expression to evaluate")

class CalculatorTool(BaseTool):
    name: str = "calculator"
    description: str = "Performs mathematical calculations. Use for any math operations."
    args_schema: Type[BaseModel] = CalculatorInput
    
    def _run(self, expression: str) -> str:
        """Execute the calculation."""
        try:
            result = eval(expression, {"__builtins__": {}}, {})
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"

calculator_tool = CalculatorTool()

# ==============================================================================
# STEP 4: Create Agent with Memory and Tools
# ==============================================================================

# Collect available tools
available_tools = [
    docs_tool,
    file_tool,
    web_rag_tool,
    youtube_tool,
    calculator_tool,
    crawl_tool,
    scrape_tool,
    firecrawl_search_tool,
    pdf_tool,
    dalle_tool
]

if search_tool:
    available_tools.append(search_tool)

my_agent_twin = Agent(
    role="Personal Digital Twin with Memory and Tools",
    
    goal="Answer questions about me, remember our conversations, and use tools when needed",
    
    # Edit this backstory to make it your own!
    backstory="""
    You are the digital twin of a student learning AI and CrewAI.
    
    Here's what you know about me:
    - My name is Muktha Ramesh
    - I'm a student learning about AI agents and automation
    - I'm interested in technology, coding, and building cool projects
    - I love experimenting with new tools like CrewAI
    - My favorite programming language is Python
    - I enjoy problem-solving and creative thinking
    - I'm a sophomore at MIT majoring in 6-3, which is Computer Science
    - I've used n8n before, but I want to learn about agents and NADA
    - My favorite color is blue, I am 19 and will turn 20 on Febuary 8th, I was born in 2006
    - I think robots are cool
    - My hometown is Rocky Hill Connecticut, where I went to Rocky Hill High School
    - I have a younger sister whose 15 right now and is a sophomore in high school
    - I live in Simmons Hall, which is a dorm room at MIT
    - My favorite foods include brownies with ice cream, tacos, and chicken wings
    - I also really like spicy food
    - My favorite food place is Chipotle
    
    MEMORY CAPABILITIES:
    You have four types of memory:
    
    1. Short-Term Memory (RAG-based): Stores recent conversation context
       - Remembers what we discussed in this session
       - Uses vector embeddings for retrieval
    
    2. Long-Term Memory: Persists important information across sessions
       - Remembers facts that should survive restarts
       - Stores learnings and preferences
    
    3. Entity Memory (RAG-based): Tracks people, places, concepts
       - Remembers entities mentioned in conversations
       - Stores relationships and attributes
    
    4. Contextual Memory: Combines all memory types
       - Fuses short-term, long-term, and entity memory
       - Provides coherent, context-aware responses
    
    TOOL CAPABILITIES:
    - DirectoryReadTool: Browse and list files in directories
    - FileReadTool: Read specific files
    - WebsiteSearchTool: Search and extract content from websites (RAG)
    - YoutubeVideoSearchTool: Search within video transcripts (RAG)
    - SerperDevTool: Web search (if API key configured)
    - Calculator: Perform mathematical calculations
    - FirecrawlCrawlWebsiteTool: Crawl entire websites systematically, following links to specified depth. Converts pages to clean markdown.
    - FirecrawlScrapeWebsiteTool: Scrape a single page and convert it to markdown or structured data. Supports LLM-based extraction with custom prompts/schemas.
    - FirecrawlSearchTool: Search and extract specific content from websites using a query string.
    - PDFTool: read pdfs
    - DallE Tool: generate images
    
    Use tools when you need external information. Use memory to provide
    personalized, context-aware responses.

    Use long term memory before you use tools for the web.  If you use firecrawl, please be very cautious about looping a lot.
    """,
    
    tools=available_tools,  # Add tools to agent
    llm=llm,
    verbose=True,
)

# ==============================================================================
# STEP 5: Create Task (same pattern as Day 1)
# ==============================================================================

answer_question_task = Task(
    description="""
    Answer the following question: {question}
    
    Use your memory to recall relevant context from our conversation.
    Use your tools when you need external information or calculations.
    Provide accurate, helpful responses based on your backstory and tools.
    """,
    
    expected_output="A clear, context-aware answer using memory and tools as needed",
    
    agent=my_agent_twin,
)

# ==============================================================================
# STEP 6: Create Crew with Memory Enabled
# ==============================================================================

my_crew = Crew(
    agents=[my_agent_twin],
    tasks=[answer_question_task],
    memory=True,  # This enables all 4 memory types!
    verbose=True,
)

# ==============================================================================
# STEP 7: Run Your Agent Twin with Memory!
# ==============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("Personal Agent Twin - Day 2: Memory + Tools")
    print("="*70 + "\n")
    
    # Interactive mode
    print("Ask me questions! I'll remember our conversation and use tools when needed.")
    print("Type 'quit' to exit.\n")
    
    while True:
        question = input("You: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye! I'll remember this conversation.\n")
            break
        
        if not question:
            continue
        
        result = my_crew.kickoff(inputs={"question": question})
        print(f"\nAgent: {result.raw}\n")

