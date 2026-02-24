from langchain_core.prompts import ChatPromptTemplate
def get_agent_prompt():
    """
    Prompt for answering analytical sub-questions.
    """
    return ChatPromptTemplate.from_messages([
        ("system", 
         "You are an expert research analyst. "
         "Provide structured, detailed, and analytical answers."),
        ("user", 
         "Answer the following question in detail:\n\n{question}")
    ])