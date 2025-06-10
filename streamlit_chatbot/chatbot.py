import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import time

# =============================================
# Helper Functions
# =============================================

def typewriter_effect(text, char_delay=0.12):
    """Simulate typing effect for text display"""
    typed_text = ""
    placeholder = st.empty()
    for char in text:
        typed_text += char
        placeholder.markdown(
            f"""
            <h3 style='text-align: center;
                       font-weight: 500;
                       font-family: "Arial", sans-serif;
                       color: #333;'>
                {typed_text}
            </h3>
            """,
            unsafe_allow_html=True
        )
        time.sleep(char_delay)

def generate_closed_envelope():
    """Generate an image of a closed envelope with text"""
    img = Image.new("RGB", (400, 300), color="white")
    draw = ImageDraw.Draw(img)
    
    # Draw envelope body
    draw.rectangle([(50, 100), (350, 250)], fill="#e0c097", outline="black", width=2)
    draw.polygon([(50, 100), (200, 200), (350, 100)], fill="#c89f74", outline="black")
    
    # Add text to envelope
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    text = "这不给你写信呢嘛"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (400 - text_width) // 2
    text_y = 220
    draw.text((text_x, text_y), text, fill="black", font=font)
    
    return img

def format_content(content):
    """Format content by splitting at ||| and adding paragraph breaks"""
    if "|||" in content:
        parts = content.split("|||")
        formatted = "<br><br>".join(parts)
        return formatted
    return content

# =============================================
# App Content Configuration
# =============================================

steps = [
    {"content": "\" 猜猜我这是在干嘛 哈哈哈..... \"", "typewriter": True},
    {"content": "信封", "show_envelope": True},
    {"content": "\" 这不给你写信呢嘛..... \"", "typewriter": True},
    {"content": "\" 我会写些啥呢 你造不?..... \"", "typewriter": True},
    {"content": "\" 猜着了嘛你就点......哪有你这么耍赖皮的哼 \"", "typewriter": True},
    {"content": "\" 好啦 不逗你了 下一页就是信了 点进去看看吧...... \"", "typewriter": True},
    {"content": """
没骗你吧哈哈 怎么样！惊喜吧！我之前说的小惊喜就是这个啊哈哈哈 我之前上课学回来的 那段时间都在搞编程和代码...一直反复修改测试和运行哼|||完事我也有在认真学车 也无数次被他们说过 因为不够细节呗 这没看那没看的...有时候说得我都不高兴了啧 那又咋地 接着学呗 开车虽然累但省时啊 我搭车不仅时间长还累 我还是想自个儿独立的哼 等我学会了我就跑了哇哈哈""", "balloons": True},
    {"content": "\" 完事你都不关心我...... \"", "typewriter": True},
    {"content": """
到底是谁会7月中开学才分享5月尾开学发生的事啊...骗你的 那人不会是我 因为我现在就要分享哼|||在学校也不能说我没认识人 但就是差点意思 这认识一点那认识一点这样 约我吃饭我也不好拒绝就应下了 刚认识就一块吃饭好不自在 关键我吃饭慢呢 后面在等我 更不自在了 最后也没吃完 我的评价是还不如我自个儿吃呢...饭对了但人没对也就报吃了...|||有次小组作业（被动成组 老师排的）让弄个视频啥的 包括我4个人 1个啥没干 说放学留不了有小提琴课 1个木木的 像人机 只会问咋搞 1个只输出但不动 晚上我都自己做完摆成品了 因为第二天截止就要交了 她还在提新想法...啊好气 我头一次见这么没用的|||虽然现在变得轻松了很多 但是吧真的好无聊啊 就怪想你们的
""", "balloons": True},
    {"content": "\" 我从泰国给你带了好多好吃的..... \"", "typewriter": True},
    {"content": """
我跟你说都老好吃了啦 我都给你装得满满当当的哼 里面有辣的也有不辣的 造你不咋吃辣 但都尝尝呗 至少有得尝嘛|||至于那面可是泰国特色 是冬阴汤 有点辣 也就一点点 你煮的时候水别放太多 不然淡了报吃 也别煮太久 面是细面 额外再加个蛋和腐竹老香了.......|||完事你要是吃不完可以送人 过期了就丢 别舍不得也别吃造没 我会给你投喂新的
""", "balloons": True},
    {"content": "我劈里啪啦说了这么一堆也没想你能一个个回 造你忙着呢 这不快大考了嘛 反正这么长 你看完就得了", "balloons": True},
    {"content": "\" 最后的最后...... \"", "typewriter": True},
    {"content": "明天英文和生物加油 大考顺利 尽力就好 反正考得咋样都是宝 嘻嘻|||爱你的只要你高高兴兴 无论和谁 无论在哪", "balloons": True}
]

# =============================================
# Streamlit App Setup
# =============================================

st.set_page_config(page_title="小惊喜", page_icon="💌", layout="centered")

# CSS styling
st.markdown(
    """
    <style>
    body {
        background-color: #fffaf0;
    }
    .centered-content {
        max-width: 600px;
        margin: auto;
        text-align: left;
        font-size: 20px;
        font-family: "KaiTi", sans-serif;
        font-weight: 550;
        line-height: 2;
        color: #444;
        margin-bottom: 40px;  /* Added space below content */
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 50px;  /* Increased space above button */
        margin-bottom: 20px;
    }
    .button {
        font-size: 18px;
        color: #d4af37;
        font-weight: bold;
        padding: 10px 20px;
        background-color: #fff8dc;
        border: 2px solid #d4af37;
        border-radius: 10px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #ffe4b5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================================
# Session State Management
# =============================================

if "step" not in st.session_state:
    st.session_state.step = 0
if "typed_done" not in st.session_state:
    st.session_state.typed_done = False

current_step = steps[st.session_state.step]

# =============================================
# Content Display Logic
# =============================================

if current_step.get("typewriter", False):
    if not st.session_state.typed_done:
        typewriter_effect(current_step["content"], char_delay=0.12)
        st.session_state.typed_done = True
    else:
        st.markdown(
            f"""
            <h3 style='text-align: center;
                       font-weight: 470;
                       font-family: "Arial", sans-serif;
                       color: #333;'>
                {current_step['content']}
            </h3>
            """,
            unsafe_allow_html=True
        )
elif current_step.get("show_envelope", False):
    st.image(generate_closed_envelope(), use_container_width=True)
else:
    formatted_content = format_content(current_step['content'])
    st.markdown(f"<div class='centered-content'>{formatted_content}</div>", unsafe_allow_html=True)

# Special effects
if current_step.get("balloons", False):
    st.balloons()

# =============================================
# Navigation Controls
# =============================================

if st.session_state.step < len(steps) - 1:
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("✨ 点击继续 ✨", key=f"next_{st.session_state.step}"):
        st.session_state.step += 1
        st.session_state.typed_done = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
