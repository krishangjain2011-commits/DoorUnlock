import streamlit as st
import random
import time

st.set_page_config(page_title="DoorGuard Ultra", layout="centered")

# ---------------- CYBER UI CSS ----------------
st.markdown("""
<style>
html, body {
    background-color: #05070a;
    color: #dde4ef;
}

.block-container {
    padding-top: 2rem;
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg,#00e5ff,#7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Card */
.card {
    background: #0b0f14;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 25px;
    margin-top: 20px;
}

/* Buttons */
.stButton button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #00e5ff;
    background: transparent;
    color: #00e5ff;
    font-weight: 700;
    padding: 12px;
}

.stButton button:hover {
    background: rgba(0,229,255,0.1);
}

/* Step bar */
.step {
    display: inline-block;
    padding: 8px 10px;
    margin: 3px;
    border-radius: 8px;
    font-size: 10px;
    border: 1px solid #222;
}

.active { border-color: #ffc843; color:#ffc843;}
.done { border-color:#00ffa3; color:#00ffa3;}
</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "otp" not in st.session_state:
    st.session_state.otp = str(random.randint(100000, 999999))

# ---------------- HEADER ----------------
st.markdown("<div class='title'>DoorGuard Ultra™</div>", unsafe_allow_html=True)
st.write("### One Door. Seven Checks.")

# ---------------- STEP TRACKER ----------------
steps = ["Captcha","OTP","Vibe","Face","Terms","Timer","Access"]

tracker = ""
for i,s in enumerate(steps):
    if i < st.session_state.step:
        tracker += f"<span class='step done'>{s}</span>"
    elif i == st.session_state.step:
        tracker += f"<span class='step active'>{s}</span>"
    else:
        tracker += f"<span class='step'>{s}</span>"

st.markdown(tracker, unsafe_allow_html=True)

# ---------------- STEP 1 ----------------
if st.session_state.step == 0:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🤖 CAPTCHA")

    choice = st.radio("Select 🐶:", ["🐶","🐱","🍎","🚗"])

    if st.button("Verify"):
        if choice == "🐶":
            st.session_state.step += 1
            st.rerun()
        else:
            st.error("Robot detected 🤖")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- STEP 2 ----------------
elif st.session_state.step == 1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📠 Fax OTP")
    st.info(f"Hint: {st.session_state.otp}")

    otp = st.text_input("Enter OTP")

    if st.button("Submit"):
        if otp == st.session_state.otp:
            st.session_state.step += 1
            st.rerun()
        else:
            st.error("Wrong OTP 💀")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- STEP 3 (FIXED) ----------------
elif st.session_state.step == 2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🧠 Vibe Check")

    if "vibe" not in st.session_state:
        st.session_state.vibe = random.randint(0,100)

    st.progress(st.session_state.vibe/100)
    st.write(f"Vibe Score: {st.session_state.vibe}")

    if st.button("Accept Vibe"):
        if st.session_state.vibe > 40:
            st.session_state.step += 1
            del st.session_state.vibe
            st.rerun()
        else:
            st.error("Bad vibes 🚫")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- STEP 4 ----------------
elif st.session_state.step == 3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("👁 Face Scan")

    if "face" not in st.session_state:
        time.sleep(1)
        st.session_state.face = random.choice(["ok","no"])

    if st.session_state.face == "ok":
        st.success("Face accepted 😎")
        if st.button("Proceed"):
            st.session_state.step += 1
            del st.session_state.face
            st.rerun()
    else:
        st.error("Face rejected 💀")
        if st.button("Retry"):
            del st.session_state.face
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- STEP 5 ----------------
elif st.session_state.step == 4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📜 Terms")
    st.text_area("Terms", "Legal stuff...\n"*20)

    agree = st.checkbox("Agree")

    if st.button("Continue"):
        if agree:
            st.session_state.step += 1
            st.rerun()
        else:
            st.error("Agree first 😈")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- STEP 6 ----------------
elif st.session_state.step == 5:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("⏱ Countdown")

    ph = st.empty()
    for i in range(5,0,-1):
        ph.markdown(f"# {i}")
        time.sleep(1)

    if st.button("OPEN"):
        st.session_state.step += 1
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- STEP 7 ----------------
elif st.session_state.step == 6:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🔓 ACCESS GRANTED")
    st.success("Door was open all along 😂")

    if st.button("Restart"):
        st.session_state.step = 0
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
