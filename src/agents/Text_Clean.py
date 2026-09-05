from typing import TypedDict
from langgraph.graph import StateGraph, END

# 文本处理管道的共享状态
# 所有节点从这个 State 读数据，修改后写回来
class TextState(TypedDict):
    raw_text: str       # 用户输入的原始文本
    cleaned: str        # 清理后的文本（去掉首尾空格）
    word_count: int     # 单词数量
    summary: str        # 文本摘要


def clean_node(state: TextState) -> dict:
    """清理文本：去掉首尾多余空格"""
    # 从 state 中取出原始文本，用 strip() 去掉首尾空格
    text = state["raw_text"].strip()
    # 只返回要更新的字段，LangGraph 会自动合并进 state
    return {"cleaned": text}


def count_node(state: TextState) -> dict:
    """统计单词数：用 split() 将文本切分为单词列表，再用 len() 计数"""
    # split() 默认按空格切分字符串为列表，len() 计算列表长度即单词数
    count = len(state["cleaned"].split())
    return {"word_count": count}

def summary_node(state: TextState)-> dict:
    """生成摘要（这里简化为截断）"""
    text=state["cleaned"]
    summary=text[:50] + "..." if len(text)>50 else text
    return {"summary" :summary}

graph = StateGraph(TextState)  # type: ignore[arg-type]
graph.add_node("clean", clean_node)  # type: ignore[arg-type]
graph.add_node("count", count_node)  # type: ignore[arg-type]
graph.add_node("summarize", summary_node)  # type: ignore[arg-type]

graph.set_entry_point("clean")
graph.add_edge("clean", "count")
graph.add_edge("count", "summarize")
graph.add_edge("summarize", END)
app = graph.compile()

# 4. 运行
result = app.invoke({
    "raw_text": "  LangGraph 是一个用于构建有状态 Agent 应用的框架，基于图结构描述执行流。  ",
    "cleaned": "",
    "word_count": 0,
    "summary": ""
})

print("清理后:", result["cleaned"])
print("词数:", result["word_count"])
print("摘要:", result["summary"])


