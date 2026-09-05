from langgraph.constants import END
from langgraph.graph import StateGraph
from typing import TypedDict


class FeedbackState(TypedDict):
    user_input: str
    sentiment: str
    response: str
    final_output: str


def analyze_sentiment(state: FeedbackState)-> dict:
    text=state["user_input"].lower()
    positive_words = ["好", "棒", "满意", "喜欢", "excellent"]
    negative_words=["不好","不","不满意","不喜欢","bad"]
    pos_count = sum(1 for w in positive_words if w in text)
    neg_count = sum(1 for w in negative_words if w in text)

    if pos_count > neg_count:
        sentiment = "positive"
    elif neg_count>pos_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {"sentiment": sentiment}
def handle_positive(state: FeedbackState) -> dict:
    """处理正面反馈"""
    response = f"感谢您的好评！很高兴我们的服务让您满意。您的反馈：'{state['user_input']}'"
    return {"response": response}

def handle_negative(state: FeedbackState) -> dict:
    """处理负面反馈"""
    response = (
        f"非常抱歉给您带来了不好的体验！"
        f"您的反馈已记录：'{state['user_input']}'。"
        f"我们的高级客服将在 24 小时内联系您。"
    )
    return {"response": response}

def handle_neutral(state: FeedbackState) -> dict:
    """处理中性反馈"""
    response = f"感谢您的反馈：'{state['user_input']}'。我们会继续改进服务。"
    return {"response": response}
def format_output(state: FeedbackState)->dict:
    output = f"[情绪]: {state['sentiment']}\n[回复]: {state['response']}\n[最终输出]: {state['final_output']}\n"
    return {"final_output": output}

def route_by_sentiment(state: FeedbackState)-> str:
    return state["sentiment"]

graph = StateGraph(FeedbackState)

graph.add_node("analyze", analyze_sentiment)
graph.add_node("positive_handler", handle_positive)
graph.add_node("negative_handler",handle_negative)
graph.add_node("neutral_handler",handle_neutral)
graph.add_node("format",format_output)

graph.set_entry_point("analyze")

graph.add_conditional_edges(
    "analyze",
    route_by_sentiment,
    {
        "positive": "positive_handler",
        "negative": "negative_handler",
        "neutral": "neutral_handler",
    }
)

graph.add_edge("positive_handler", "format")
graph.add_edge("negative_handler", "format")
graph.add_edge("neutral_handler", "format")
graph.add_edge("format",END)

app = graph.compile()


r = app.invoke({
    "user_input": "产品很棒，服务也很满意！",
    "sentiment": "",
    "response": "",
    "final_output": ""
})
print(r["final_output"])
# [情绪：positive]
# 感谢您的好评！很高兴我们的服务让您满意。...

# 负面反馈
r = app.invoke({
    "user_input": "太差了，完全不满意，要投诉！",
    "sentiment": "",
    "response": "",
    "final_output": ""
})
print(r["final_output"])



















