import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Function to generate a closed envelope image with text
def generate_closed_envelope():
    img = Image.new("RGB", (400, 300), color="white")
    draw = ImageDraw.Draw(img)

    # Envelope body
    draw.rectangle([(50, 100), (350, 250)], fill="#e0c097", outline="black", width=2)
    # Envelope flap (triangle)
    draw.polygon([(50, 100), (200, 200), (350, 100)], fill="#c89f74", outline="black")

    # Add "Dear Dad" text on the envelope
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    text = "Dear Dad"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (400 - text_width) // 2
    text_y = 220
    draw.text((text_x, text_y), text, fill="black", font=font)

    return img

# Streamlit app setup
st.set_page_config(page_title="Father's Day Surprise", page_icon="💌", layout="centered")

# Add background color (light, warm tone)
st.markdown(
    """
    <style>
    body {
        background-color: #fffaf0;
    }
    .centered-content {
        max-width: 500px;
        margin: auto;
        text-align: center;
    }
    .blink-button {
        font-size: 18px;
        color: #d4af37;
        font-weight: bold;
        animation: blink 1.5s infinite;
        padding: 10px 20px;
        background-color: #fff8dc;
        border: 2px solid #d4af37;
        border-radius: 10px;
        cursor: pointer;
        display: inline-block;
        margin-top: 20px;
    }
    @keyframes blink {
        0%, 100% {opacity: 1;}
        50% {opacity: 0.4;}
    }
    .blink-button:hover {
        background-color: #ffe4b5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Top title remains at the top
st.markdown("""
    <h2 style='text-align: center;'>
        💌 Happy Father's Day 💌
    </h2>
    """, unsafe_allow_html=True)

# Session state to control reveal
if "opened" not in st.session_state:
    st.session_state.opened = False

# Display envelope based on state
if not st.session_state.opened:
    with st.container():
        st.image(generate_closed_envelope(), use_container_width=True)
        # Blinking button in the center
        clicked = st.button("✨📬 Click to Open Envelope ✨")
        if clicked:
            st.session_state.opened = True
            st.rerun()
else:
    st.markdown("---")
    st.markdown("""
        <div class='centered-content' style='font-size: 20px;'>
            <strong>Dear Dad,</strong><br><br>
            Father’s Day is coming soon,<br>
            and I want to thank you for driving me to the train station every day,<br>
            making sure I get to school safely.<br><br>
            Though I’m not very good at expressing my feelings,<br>
            please know that I truly appreciate all the little things you do for me.<br><br>
            By the way, this is a little coding project I learned in my AI & Digital Literacy Workshop at Sunway University.<br>
            I hope it brings you a pleasant surprise!<br><br>
            Wishing you health, happiness, and a wonderful Father’s Day.<br><br>
            With love,<br>
            <em>Jing Xuan</em>
        </div>
        """, unsafe_allow_html=True)
    st.balloons()
