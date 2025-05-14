# ML Platform Discussion Agent

An interactive discussion system built with the Agno framework that facilitates debates between AI experts on different machine learning platforms.

## Overview

This project demonstrates the use of multi-agent interactions to compare different platforms for machine learning:

- Linux
- Mac
- Windows
- Cloud Services

The system operates in two modes:
- **Collaborative Mode**: All experts participate in a discussion
- **Routing Mode**: The system routes questions to the most appropriate expert

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd ml02

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

Run the main script:

```bash
python agno_discussion_team.py
```

The script will prompt you to enter a message. You can ask about machine learning platforms, and the agents will respond according to their expertise.

Example questions:
- "What's the best platform for running large language models?"
- "How do the different platforms compare for data scientists?"
- "What are the advantages of Linux for machine learning?"

Enter `q` at any prompt to exit the program.

## Project Structure

- `agno_discussion_team.py`: Main script containing agent and team definitions
- `tmp/`: Directory for SQLite database storage
- `requirements.txt`: Python dependencies

## Dependencies

The project requires the following key packages:
- agno==1.4.3
- openai==1.76.2
- SQLAlchemy==2.0.40

## License

[Your license information] 