import streamlit as st
import random
import time

st.set_page_config(page_title="DoorGuard Ultra", layout="centered")

# ---------------- CUSTOM CSS (UI UPGRADE) ----------------
st.markdown("""
<style>
body {
    background-color: #05070a;
}
.main {
    background-color: #05070a;
}
.block-container {
    padding-top: 2rem;
}

h1, h2, h3, h4 {
    color: #00e5ff;
    font-family: 'Segoe UI', sans-serif;
}

.stButton>button {
    background: transparent;
    border: 1px solid #00e5ff;
    color: #00e5ff;
    padding: 10px 25px;
    border-radius: 10px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: rgba(0,229,255,0.1);
}

.card {
    background: #0b0f14;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
}

.success {
    color: #00ffa3;
}
.error {
    color: #ff4060;
}
</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "otp" not in st.session_state:
    st.session_state.otp = str(random.randint(100000, 999999))

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>🚪 DoorGuard Ultra™</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>One Door. Seven Checks.</p>", unsafe_allow_html=True)

st.progress((st.session_state.step + 1)/7)

# ---------------- STEP 1 ----------------
if st.session_state.step == 0:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🤖 CAPTCHA")

    options = ["🐶", "🐱", "🍎", "🚗"]
    choice = st.radio("Select the dog:", options)

    if st.button("Verify"):
        if choice == "🐶":
            st.success("Human verified 😎")
            st.session_state.step += 1
            st.rerun()
        else:
            st.error("Robot detected 🤖")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- STEP 2 ----------------
elif st.session_state.step == 1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📠 Fax OTP (lol)")
    st.info(f"Hint: {st.session_state.otp}")

    user_otp = st.text_input("Enter OTP")

    if st.button("Submit"):
        if user_otp == st.session_state.otp:
            st.success("OTP Verified ✅")
            st.session_state.step += 1
            st.rerun()
        else:
            st.error("Wrong OTP 💀")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- STEP 3 ----------------
elif st.session_state.step == 2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🧠 Vibe Check")

    if "vibe" not in st.session_state:
        st.session_state.vibe = random.randint(0, 100)

    st.progress(st.session_state.vibe / 100)
    st.write(f"Vibe Score: {st.session_state.vibe}")

    if st.button("Accept Vibe"):
        if st.session_state.vibe > 40:
            st.success("Good vibes 😌")
            st.session_state.step += 1
            del st.session_state.vibe
            st.rerun()
        else:
            st.error("Bad vibes 🚫")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- STEP 4 (FIXED) ----------------
elif st.session_state.step == 3:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👁 Face Scan")

    if "face_result" not in st.session_state:
        with st.spinner("Scanning face..."):
            time.sleep(2)
            st.session_state.face_result = random.choice(["approved", "rejected"])

    if st.session_state.face_result == "approved":
        st.success("Face recognized 😎")

        if st.button("Proceed"):
            st.session_state.step += 1
            del st.session_state.face_result
            st.rerun()
    else:
        st.error("Face not convincing 💀")

        if st.button("Retry"):
            del st.session_state.face_result
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- STEP 5 ----------------
elif st.session_state.step == 4:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📜 Terms & Conditions")

    st.text_area("Terms", "Very long boring legal text...\n" * 20)

    agree = st.checkbox("I agree to everything blindly")

    if st.button("Continue"):
        if agree:
            st.session_state.step += 1
            st.rerun()
        else:
            st.error("You must agree 😈")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- STEP 6 ----------------
elif st.session_state.step == 5:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("⏱ Final Countdown")

    placeholder = st.empty()

    for i in range(5, 0, -1):
        placeholder.markdown(f"<h1 style='text-align:center;color:#ff4060'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1)

    if st.button("OPEN DOOR"):
        st.session_state.step += 1
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- STEP 7 ----------------
elif st.session_state.step == 6:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🔓 ACCESS GRANTED")
    st.success("Door was open the whole time 😂")

    if st.button("Restart"):
        st.session_state.step = 0
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
