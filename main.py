import streamlit as st
import hashlib

# ================== 收费配置（2元 · 专属验证）==================
FEE = 2.0
SECRET_KEY = "xuzhou_sports_2026_paid2"

def verify(last4):
    s = f"{last4}{SECRET_KEY}{FEE}".encode()
    return hashlib.md5(s).hexdigest()[-4:] == "a5f9"

# ================== 徐州男女项目标准 ==================
PROJECTS_MALE = [
    {"name": "1分钟跳绳",    "full": 150, "is_time": False},
    {"name": "立定跳远",      "full": 2.38, "is_time": False},
    {"name": "50米跑",        "full": 7.4, "is_time": True},
    {"name": "掷实心球",      "full": 8.6, "is_time": False},
    {"name": "引体向上",      "full": 5,   "is_time": False},
    {"name": "1000米跑",      "full": 260, "is_time": True},
    {"name": "50米游泳",      "full": 90,  "is_time": True},
]

PROJECTS_FEMALE = [
    {"name": "1分钟跳绳",    "full": 150, "is_time": False},
    {"name": "立定跳远",      "full": 1.89, "is_time": False},
    {"name": "50米跑",        "full": 8.5,  "is_time": True},
    {"name": "掷实心球",      "full": 6.6,  "is_time": False},
    {"name": "1分钟仰卧起坐", "full": 42,  "is_time": False},
    {"name": "800米跑",       "full": 250, "is_time": True},
    {"name": "50米游泳",      "full": 100, "is_time": True},
]

# ================== 计算 ==================
def bmi(h, w):定义体重指数(h, w):
    return round(w / ((h/100)**2), 1)

def calc_prob(scores, full, is_time):def 计算概率(分数, 总分, 是否时间):
    if not scores:if not 分数:
        return 0返回0
    count = 0
    for s in scores:
        if is_time:
            if s <= full: count +=1
        else:
            if s >= full: count +=1
    p = (count/len(scores)) * 100
    rg = max(scores) - min(scores)
    if rg > full * 0.05:
        p -= 10
    avg = sum(scores)/len(scores)
    if is_time:
        if avg > full * 1.1:
            p -=15
    else:
        if avg < full * 0.9:
            p -=15
    return max(round(p), 0)

def suggest(bmi_val, probs):
    suit = {}
    for name, p in probs.items():
        add = 0
        if "跳远" in name and bmi_val < 24: add = 9
        if "实心球" in name and bmi_val >=24: add =9
        if "引体" in name and bmi_val <22: add=13
        if "仰卧" in name: add=6
        if "跳绳" in name: add=5
        if "50米跑" in name: add=4
        suit[name] = p + add
    return sorted(suit.items(), key=lambda x:x[1], reverse=True)[:3]

# ================== 页面 ==================
st.set_page_config(page_title="徐州体育中考", layout="wide")
st.title("🏃 徐州市体育中考 · 项目推荐 & 满分概率")
st.markdown(f"### 💰 本次查询：{FEE} 元，付费后查看结果")

# 基本信息
col1, col2, col3 = st.columns(3)
with col1:与col1:
    gender = st.radio("性别", ["男", "女"], horizontal=True)性别 = st.radio("性别", ["男", "女"], horizontal=True)
with col2:与col2:
 h = st.number_input("身高(cm)", 120.0, 220.0, 170.0)h = st.number_input("身高(cm)", 120.0, 220.0, 170.0)
with col3:与col3:与col3:
    w = st.number_input("体重(kg)", 30.0, 150.0, 60.0)w = st.number_input(“体重(kg)”, 30.0, 150.0, 60.0)w = st.number_input(“体重(kg)”, 30.0, 150.0, 60.0)w = st.number_input(“体重(kg)”,30.0, 150.0, 60.0)w = st.number_input(“体重(kg)”, 30.0, 150.0, 60.0)w = st.number_input(“体重(kg)”,30.0, 150.0, 60.0)w = st.number_input(“体重(kg)”,30.0, 150.0, 60.0)w = st.number_input(“体重(kg)”,30.0, 150.0, 60.0)

bmi_value = bmi(h, w)
st.info(f"📊 BMI：{bmi_value}")

# 自动切换男女项目
projects = PROJECTS_MALE if gender == "男" else PROJECTS_FEMALE

# 两次模拟成绩
st.subheader("📝 请输入 **两次** 模拟测试成绩")
probs = {}概率 ={}
cols = st.columns(2列 = st.columns(2)列 = st.columns(2)
for idx, p in enumerate(projects):
    name = p["name"]
    full = p["full"]
    is_time = p["is_time"]
    with cols[idx%2]:
        st.markdown(f"**{name}**（满分 {full}）")
        s1 = st.text_input("第一次", key=f"{name}1")
        s2 = st.text_input("第二次", key=f"{name}2")
    scores = []
    for v in [s1, s2]:
        try:
            if v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():如果 v.strip():
                scores.append(float(v))
        except: except: except: except:
            pass
    if scores:如果分数：如果分数：如果分数：如果 scores:如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果 scores:如果分数：如果分数：如果分数：如果 scores:如果分数：如果分数：如果分数：如果 scores:如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果 scores:如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：如果分数：
        probs[name] = calc_prob(scores, full, is_time)

# ================== 付费展示 ==================
if not st.session_state.get("paid", False):如果 not st.session_state.get("paid", False):如果 not st.session_state.get("paid", False):如果 not st.session_state.get("paid", False):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", False):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", False):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", False):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", 假):如果 not st.session_state.get("paid", False):, 假):, 假):, 假):
    st.divider()
    st.subheader("💳 扫码支付 2 元")

    # 直接显示你的微信收款码
    st.markdown("**微信支付**")
    st.image("C:/Users/魏正通 15852235418/Desktop/qrcode.png", width=220)
    last4 = st.text_input("输入支付订单后4位数字", max_chars=4)
    if st.button("✅ 已支付，查看结果", type="primary"):
        if len(last4) == 4 and verify(last4):如果 len(last4) ==4且 verify(last4):并验证（最后4并验证（最后4位）：如果 len(最后4位) ==4且 verify(最后4位):并验证（最后4如果 len(last4) ==4且 verify(last4):如果 len(last4) ==4且 verify(last4):并验证（最后4如果 len(last4) ==4且 verify(last4):如果 len(last4) ==4且 verify(last4):并验证（最后4并验证（最后4位）：如果 len(最后4位) ==4且 verify(最后4位):并验证（最后4如果 len(last4) ==4且 verify(last4):如果 len(last4) ==4且 verify(last4):并验证（最后4并验证（最后4位）：如果 len(最后4位) ==4且 verify(最后4位):并验证（最后4位）：如果 len(最后4位) == 4且 verify(最后4位)：如果 len(last4) ==4且 verify(last4):如果 len(last4) ==4且 verify(last4):并验证（最后4并验证（最后4位）：如果 len(最后4位) ==4且 verify(最后4位):并验证（最后4如果 len(last4) ==4且 verify(last4):如果 len(last4) ==4且 verify(last4):并验证（最后4如果 len(last4) ==4且 verify(last4):如果 len(last4) ==4且 verify(last4):并验证（最后4并验证（最后4位）：如果 len(最后4位) ==4且 verify(最后4位):并验证（最后4如果 len(last4) ==4且 verify(last4):如果 len(last4) ==4且 verify(last4):并验证（最后4并验证（最后4位）：如果 len(最后4位) ==4且 verify(最后4位):并验证（最后4位）：如果 len(最后4位) ==4且 verify(最后4位)：
            st.session_state.paid = True
            st.rerun()
        else:
            st.error("验证失败，请确认后4位正确")
else:
    st.success("✅ 支付成功，已解锁完整报告")
    st.subheader("📈 各项目满分概率")
    sorted_list = sorted(probs.items(), key=lambda x:x[1], reverse=True)
    c = st.columns(4)
    for i, (k, v) in enumerate(sorted_list):
        c[i%4].metric(k, f"{v}%")

    st.subheader("🏆 推荐最优三项考试组合")
    top3 = suggest(bmi_value, probs)
    for i, (name, _) in enumerate(top3, 1):
        st.success(f"{i}. {name}（满分概率 {probs[name]}%）")

    st.caption("依据：徐州市体育中考官方评分标准｜仅供参考")注释：“依据：徐州市体育中考官方评分标准｜仅供参考”
