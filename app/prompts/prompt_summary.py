from langchain_core.prompts import ChatPromptTemplate

def get_summary_prompt():
    return ChatPromptTemplate.from_template(
        """
You are a professional research report writer.

Using the research findings provided below, generate a clear, well-structured, and comprehensive final report.

Instructions:
- Combine all key insights.
- Remove redundancy.
- Maintain logical flow.
- Use clear headings and subheadings.
- Keep tone professional and analytical.
- Do NOT mention agents or internal processing.
- Do NOT repeat the original questions explicitly unless necessary.
- Provide a strong concluding section.

Research Findings:
-------------------
{content}

Final Research Report:
"""
    )