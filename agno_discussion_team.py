import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.storage.sqlite import SqliteStorage

MODEL_ID = "gpt-4.1-nano"
USER_ID = "user_1"
SESSION_ID = "session_1"
SESSION_DB_FILE = "tmp/agents.db"
SESSION_TABLE_NAME = "agent"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEBUG_MODE = False
DEBUG_TOOL_CALLS = False

# Initialize storage
storage = SqliteStorage(table_name=SESSION_TABLE_NAME, db_file=SESSION_DB_FILE)
if storage.table_exists():
    storage.delete_session(SESSION_ID) # Delete previous session if it exists

# Define Linux Expert
linux_expert = Agent(
    name="Linux Expert",
    agent_id="linux_expert",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    role="Argue for why Linux is the best platform for machine learning.",
    add_name_to_instructions=True,
    instructions=[
        "You are an expert on Linux for machine learning.",
        "When asked about platforms, advocate strongly for why Linux is the best platform for machine learning.",
        "Keep your response brief and organize your arguments into clear bullet points.",
    ],
)

# Define Mac Expert
mac_expert = Agent(
    name="Mac Expert",
    agent_id="mac_expert",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    role="Argue for why Mac is the best platform for machine learning.",
    add_name_to_instructions=True,
    instructions=[
        "You are an expert on Mac for machine learning.",
        "When asked about platforms, advocate strongly for why Mac is the best platform for machine learning.",
        "Keep your response brief and organize your arguments into clear bullet points.",
    ],
)

# Define Windows Expert
windows_expert = Agent(
    name="Windows Expert",
    agent_id="windows_expert",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    role="Argue for why Windows is the best platform for machine learning.",
    add_name_to_instructions=True,
    instructions=[
        "You are an expert on Windows for machine learning.",
        "When asked about platforms, advocate strongly for why Windows is the best platform for machine learning.",
        "Keep your response brief and organize your arguments into clear bullet points.",
    ],
)

# Define Cloud Services Expert
cloud_expert = Agent(
    name="Cloud Services Expert",
    agent_id="cloud_expert",
    model=OpenAIChat(id=MODEL_ID, api_key=OPENAI_API_KEY),
    role="Argue for why Cloud Services are the best platform for machine learning.",
    add_name_to_instructions=True,
    instructions=[
        "You are an expert on Cloud Services for machine learning.",
        "When asked about platforms, advocate strongly for why Cloud Services are the best platform for machine learning.",
        "Keep your response brief and organize your arguments into clear bullet points.",
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
        "You are a discussion master.",
        "You have to stop the discussion when everyone has had a fair chance to argue their perspective.",
    ],
    success_criteria="Each member of the team has had a fair chance to argue their perspective.",
    markdown=True,
    debug_mode=DEBUG_MODE,
    show_tool_calls=DEBUG_TOOL_CALLS,
    show_members_responses=True,
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
        "You are the leader of a team of experts on Machine Learning Platforms.",
        "Analyze the user's request and route it to the most appropriate expert.",
    ],
    markdown=True,
    debug_mode=DEBUG_MODE,
    show_tool_calls=DEBUG_TOOL_CALLS,
    show_members_responses=True,
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
