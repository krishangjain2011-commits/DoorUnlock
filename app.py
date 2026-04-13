import streamlit as st
import random
import time

st.set_page_config(page_title="DoorGuard Ultra", layout="centered")

# ---------------- STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "otp" not in st.session_state:
    st.session_state.otp = str(random.randint(100000, 999999))

# ---------------- HEADER ----------------
st.title("🚪 DoorGuard Ultra™")
st.subheader("One Door. Seven Checks.")

st.write(f"Current Step: {st.session_state.step + 1}/7")

# ---------------- STEP 1: CAPTCHA ----------------
if st.session_state.step == 0:
    st.header("🤖 CAPTCHA")

    options = ["🐶", "🐱", "🍎", "🚗"]
    target = "🐶"

    choice = st.radio("Select Dog:", options)

    if st.button("Verify"):
        if choice == target:
            st.success("Human verified 😎")
            st.session_state.step += 1
        else:
            st.error("Try again bro 🤖")

# ---------------- STEP 2: OTP ----------------
elif st.session_state.step == 1:
    st.header("📠 Fax OTP (lol)")

    st.info(f"Hint: {st.session_state.otp}")

    user_otp = st.text_input("Enter OTP")

    if st.button("Submit OTP"):
        if user_otp == st.session_state.otp:
            st.success("OTP Verified")
            st.session_state.step += 1
        else:
            st.error("Wrong OTP 💀")

# ---------------- STEP 3: VIBE CHECK ----------------
elif st.session_state.step == 2:
    st.header("🧠 Vibe Check")

    vibe = random.randint(0, 100)
    st.progress(vibe / 100)

    st.write(f"Your vibe score: {vibe}")

    if st.button("Accept Vibe"):
        if vibe > 40:
            st.success("Vibe acceptable 😌")
            st.session_state.step += 1
        else:
            st.error("Bad vibes detected 🚫")

# ---------------- STEP 4: FACE SCAN ----------------
elif st.session_state.step == 3:
    st.header("👁 Face Scan")

    st.write("Pretending to scan your face...")

    time.sleep(2)

    result = random.choice(["approved", "rejected"])

    if result == "approved":
        st.success("Face recognized 😎")
        if st.button("Proceed"):
            st.session_state.step += 1
    else:
        st.error("Face not convincing 💀")

# ---------------- STEP 5: TERMS ----------------
elif st.session_state.step == 4:
    st.header("📜 Terms & Conditions")

    st.text_area("Terms", "Very long boring legal stuff..." * 50)

    agree = st.checkbox("I read everything (sure you did)")

    if st.button("Continue"):
        if agree:
            st.success("Legally trapped ✅")
            st.session_state.step += 1
        else:
            st.error("You must agree 😈")

# ---------------- STEP 6: COUNTDOWN ----------------
elif st.session_state.step == 5:
    st.header("⏱ Final Countdown")

    countdown = st.empty()

    for i in range(5, 0, -1):
        countdown.write(f"{i}...")
        time.sleep(1)

    st.warning("Last chance bro")

    if st.button("OPEN DOOR"):
        st.session_state.step += 1

# ---------------- STEP 7: SUCCESS ----------------
elif st.session_state.step == 6:
    st.header("🔓 ACCESS GRANTED")

    st.success("Door was open the whole time 😂")

    if st.button("Restart"):
        st.session_state.step = 0
