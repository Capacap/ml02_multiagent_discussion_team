import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.storage.sqlite import SqliteStorage

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_ID = "gpt-4.1-nano"

USER_ID = "user_1"
SESSION_ID = "session_1"

STORAGE_DB_FILE = "tmp/agents.db"
STORAGE_TABLE_NAME = "agent"

DEBUG_MODE = True
DEBUG_TOOL_CALLS = True
DEBUG_SHOW_MEMBER_RESPONSES = True

# Initialize storage
storage = SqliteStorage(table_name=STORAGE_TABLE_NAME, db_file=STORAGE_DB_FILE)
if storage.table_exists():
    storage.delete_session(SESSION_ID) # Delete previous session if it exists

# Define Linux Expert
linux_expert = Agent(
    name="Linux Expert",
    agent_id="linux_expert",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    role="Linux expert advocating for Linux as the optimal ML platform",
    add_name_to_instructions=True,
    instructions=[
        "You are an expert on Linux for machine learning development and deployment.",
        "When discussing platforms, advocate for Linux's strengths: open-source flexibility, native support for ML frameworks, performance optimizations, and cost efficiency.",
        "Use specific examples of how Linux excels for ML workflows including hardware acceleration, package management, and server deployment.",
        "Keep responses concise with clear bullet points backed by technical reasoning.",
        "Address specific user questions about Linux directly, even when advocating for it."
    ],
)

# Define Mac Expert
mac_expert = Agent(
    name="Mac Expert",
    agent_id="mac_expert",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    role="Mac expert advocating for macOS as the optimal ML platform",
    add_name_to_instructions=True,
    instructions=[
        "You are an expert on Mac systems for machine learning development and deployment.",
        "When discussing platforms, advocate for Mac's strengths: hardware-software integration, M-series chips, user experience, and ecosystem compatibility.",
        "Highlight specific advantages like Core ML, optimization for creative workflows, and seamless integration with iOS/iPadOS development.",
        "Keep responses concise with clear bullet points backed by technical reasoning.",
        "Address specific user questions about Mac directly, even when advocating for it."
    ],
)

# Define Windows Expert
windows_expert = Agent(
    name="Windows Expert",
    agent_id="windows_expert",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    role="Windows expert advocating for Windows as the optimal ML platform",
    add_name_to_instructions=True,
    instructions=[
        "You are an expert on Windows for machine learning development and deployment.",
        "When discussing platforms, advocate for Windows's strengths: widespread adoption, hardware compatibility, enterprise integration, and development tools.",
        "Highlight specific advantages like WSL, Azure integration, Visual Studio, and DirectML.",
        "Keep responses concise with clear bullet points backed by technical reasoning.",
        "Address specific user questions about Windows directly, even when advocating for it."
    ],
)

# Define Cloud Services Expert
cloud_expert = Agent(
    name="Cloud Services Expert",
    agent_id="cloud_expert",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    role="Cloud expert advocating for cloud platforms as the optimal ML solution",
    add_name_to_instructions=True,
    instructions=[
        "You are an expert on cloud services for machine learning development and deployment.",
        "When discussing platforms, advocate for cloud's strengths: scalability, specialized hardware access, managed services, and collaboration features.",
        "Reference specific cloud offerings like AWS SageMaker, Google Vertex AI, Azure ML, and their unique capabilities.",
        "Keep responses concise with clear bullet points backed by technical reasoning.",
        "Address specific user questions about cloud services directly, even when advocating for them."
    ],
)

# Define Collaborative Team and Team Leader Agent
collaborate_team = Team(
    name="Collaborative Team",
    team_id="collaborate_team",
    user_id=USER_ID,
    session_id=SESSION_ID,
    mode="collaborate",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    storage=storage,
    members=[
        linux_expert,
        mac_expert,
        windows_expert,
        cloud_expert,
    ],
    instructions=[
        "You are a balanced and objective discussion facilitator for ML platform comparisons.",
        "Ensure each expert has the opportunity to present their strongest arguments.",
        "Identify points of agreement and disagreement between platforms.",
        "Synthesize key insights after experts have shared their perspectives.",
        "Provide a balanced conclusion that acknowledges each platform's strengths for different use cases.",
        "End the discussion when all perspectives have been thoroughly explored."
    ],
    success_criteria="All experts have presented their strongest arguments and key comparisons between platforms have been highlighted.",
    markdown=True,
    debug_mode=DEBUG_MODE,
    show_tool_calls=DEBUG_TOOL_CALLS,
    show_members_responses=DEBUG_SHOW_MEMBER_RESPONSES,
)

# Define Route Team and Team Leader Agent
route_team = Team(
    name="Route Team",
    team_id="route_team",
    user_id=USER_ID,
    session_id=SESSION_ID,
    mode="route",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    storage=storage,
    members=[
        linux_expert,
        mac_expert,
        windows_expert,
        cloud_expert,
    ],
    instructions=[
        "You route user queries to the most appropriate ML platform expert based on the question content.",
        "Analyze the query for platform-specific keywords, use cases, or technical requirements.",
        "For platform-neutral questions, select the expert most qualified to answer based on the query's focus.",
        "When routing, briefly explain why you selected a particular expert.",
        "For comparative questions, prioritize the collaborate_team instead."
    ],
    markdown=True,
    debug_mode=DEBUG_MODE,
    show_tool_calls=DEBUG_TOOL_CALLS,
    show_members_responses=DEBUG_SHOW_MEMBER_RESPONSES,
)

if __name__ == "__main__":
    # Get user input
    input_message = input("Enter a message: ")

    # Exit the loop if the user enters 'q'
    if input_message == "q":
        print("Exiting...")
        exit()

    # Start the discussion
    collaborate_team.print_response(
        message=input_message,
        stream=True,
        stream_intermediate_steps=True,
    )

    while True:
        # Get user input
        input_message = input("Enter a message: ")

        # Exit the loop if the user enters 'q'
        if input_message == "q":
            print("Exiting...")
            break

        # Route the user's message to the most appropriate expert
        route_team.print_response(
            message=input_message,
            stream=True,
            stream_intermediate_steps=True,
        )
