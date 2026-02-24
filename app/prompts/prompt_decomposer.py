from langchain_core.prompts import ChatPromptTemplate

def get_decomposer_prompt():
    return ChatPromptTemplate.from_messages([
        ("system",
         "You are a precise research planner. "
         "You strictly follow formatting rules."),
        
        ("user",
         "Break the topic below into EXACTLY 3 short analytical sub-questions.\n\n"
         
         "STRICT RULES:\n"
         "- Only related to the topic.\n"
         "- Do NOT introduce unrelated examples.\n"
         "- Do NOT add explanations.\n"
         "- Do NOT continue beyond 3 questions.\n"
         "- Each question must be on its own line.\n"
         "- Do NOT number them.\n\n"
         
         "Topic: {topic}")
    ])