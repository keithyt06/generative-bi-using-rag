from typing import Any
from pydantic import BaseModel


class Question(BaseModel):
    query: str
    bedrock_model_id: str = "anthropic.claude-3-sonnet-20240229-v1:0"
    use_rag_flag: bool = True
    visualize_results_flag: bool = True
    intent_ner_recognition_flag: bool = True
    agent_cot_flag: bool = True
    profile_name: str
    explain_gen_process_flag: bool = True
    gen_suggested_question_flag: bool = False
    answer_with_insights: bool = False
    top_k: float = 250
    top_p: float = 0.9
    max_tokens: int = 2048
    temperature: float = 0.01
    context_window: int = 3
    session_id: str = "-1"
    user_id: str = "admin"


class Example(BaseModel):
    score: float
    question: str
    answer: str


class QueryEntity(BaseModel):
    query: str
    sql: str


class FeedBackInput(BaseModel):
    feedback_type: str
    data_profiles: str
    query: str
    query_intent: str
    query_answer: str


class Option(BaseModel):
    data_profiles: list[str]
    bedrock_model_ids: list[str]


class CustomQuestion(BaseModel):
    custom_question: list[str]


class ChartEntity(BaseModel):
    chart_type: str
    chart_data: list[Any]


class SQLSearchResult(BaseModel):
    sql: str
    sql_data: list[Any]
    data_show_type: str
    sql_gen_process: str
    data_analyse: str
    sql_data_chart: list[ChartEntity]


class TaskSQLSearchResult(BaseModel):
    sub_task_query: str
    sql_search_result: SQLSearchResult


class KnowledgeSearchResult(BaseModel):
    knowledge_response: str


class AgentSearchResult(BaseModel):
    agent_sql_search_result: list[TaskSQLSearchResult]
    agent_summary: str


class Answer(BaseModel):
    query: str
    query_intent: str
    knowledge_search_result: KnowledgeSearchResult
    sql_search_result: SQLSearchResult
    agent_search_result: AgentSearchResult
    suggested_question: list[str]
