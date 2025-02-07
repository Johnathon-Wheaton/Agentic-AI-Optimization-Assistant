# Agentic AI Optimization Team
This jupyter notebook demonstrates the use of AI agents to collaboratively interpret, model, and solve optimization problems. The team of agents, consisting of a consultant, coder, code checker, and result checker, are orchestrated using Autogen. 

Users can present a business problem to an AI consultant who will ask clarifying questions to undersatnd the problem in more detail. Then, the coder, code checker, and result checker work in the background to model, code, and solve the problem, outputting the results to an excel file.

# How It Works
The agents works in two sequential discussions. First, the user will dialogue directly with a consultant whose job is to understand the business problem, ask probing questions to ensure they have captured all requirements, and summarize the problem. Next, the coder, code checker, and result checker use this summary to iteratively code and solve the optimiazation model.

## Limitations
Tests have indicated that the agents struggle to correctly use a wide array of optimization python packages. To address this, the coding agent is directed to use ortools and pulp packages, limiting the scope of problems the team is capable of solving.

# Required Packages
- autogen
- pandas
- pulp

# Getting Started
1. Clone this repository:
```bash
git clone https://github.com/Johnathon-Wheaton/Agentic-AI-Optimization-Assistant.git
cd Agentic-AI-Optimization-Assistant
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Store your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY='your-api-key'
```

4. Run the jupyter notebook.
5. Present your problem you'd like to solve to the AI consultant agent and answer follow-up questions.
6. View the results in the output.xlsx file after the AI team finishes.