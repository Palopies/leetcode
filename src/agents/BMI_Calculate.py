from typing import TypedDict, Optional
from unicodedata import category

from langgraph.graph import StateGraph, END

class BMIState(TypedDict):
    name: str
    height_cm:float
    weight_kg: float
    bmi: float
    category: str
    advice: str
    report: str
    error: Optional[str]

def validate_input(state: BMIState)-> dict:
    height=state["height_cm"]
    weight=state["weight_kg"]

    if height<=0 or height>300:
        return {"error": f"身高数据异常：{height}cm"}
    if weight<=0 or weight >500:
        return {"error": f"体重数据异常:{weight}kg"}
    return {"error": "没有错误"}
def calculate_bmi(state: BMIState)-> dict:
    if state.get("error"):
        return {}
    height_m=state["height_cm"] / 100
    bmi = state["weight_kg"] / (height_m **2)
    bmi = round (bmi ,2)
    return {"bmi": bmi}
def classify_bmi(state: BMIState)->dict:
    if state.get("error"):
        return {}
    bmi = state["bmi"]
    if bmi<18.5:
        category="偏瘦"
    elif bmi<24.9:
        category="正常"
    elif bmi<29.9:
        category="过重"
    else:
        category="肥胖"
    return {"category": category}
def generate_advice(state: BMIState)-> dict:
    if state.get("error"):
        return {}
    category = state["category"]
    advice_map ={
        "偏瘦": "建议增加运动量，增加身体Weight。",
        "正常": "保持当前 lifestyle，保持Weight。",
        "超重": "建议减少运动量，减少Weight。",
        "肥胖": "建议增加运动量，增加Weight。"
    }
    return {"advice": advice_map[category]}
def format_report(state: BMIState) -> dict:
    if state.get("error"):
        report = f"错误：{state['error']}"
    else:
        report = f"""
姓名：{state["name"]}
身高：{state["height_cm"]}cm
体重：{state["weight_kg"]}kg
BMI：{state["bmi"]}
分类：{state["category"]}
建议：{state["advice"]}
""".strip()
    return {"report": report}
graph = StateGraph(BMIState)

graph.add_node("validate", validate_input)
graph.add_node("calculate", calculate_bmi)
graph.add_node("classify", classify_bmi)
graph.add_node("advice", generate_advice)
graph.add_node("format", format_report)

graph.set_entry_point("validate")
graph.add_edge("validate", "calculate")
graph.add_edge("calculate", "classify")
graph.add_edge("classify", "advice")
graph.add_edge("advice", "format")
graph.add_edge("format",END)
app = graph.compile()

for step in app.stream({
    "name": "王五",
    "height_cm": 160.0,
    "weight_kg": 80.0,
    "bmi": 0.0,
    "category": "",
    "advice": "",
    "report": "",
    "error": None,
}):
    node_name, state_update = list(step.items())[0]
    print(f"[{node_name}] {state_update}")