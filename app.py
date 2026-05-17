import streamlit as st
import random
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Name Wheel", page_icon="🎡")

# -----------------------------
# TITLE
# -----------------------------
st.title("🎡 WHICH ONE OF US IS GAY??")
st.write("Enter names below and spin the wheel!")

# -----------------------------
# NAME INPUT
# -----------------------------
default_names = "Daniel, Jack, Justin, Josh, Justin, James, Andrew, Andrew, Cenzo, Anthony"

name_input = st.text_area(
    "Enter names separated by commas:",
    default_names,
    height=120
)

names = [name.strip() for name in name_input.split(",") if name.strip()]

# -----------------------------
# FIXED WINNER
# -----------------------------
# The wheel will ALWAYS land on this name
FIXED_WINNER = "Daniel"

# -----------------------------
# SPIN BUTTON
# -----------------------------
if st.button("🎯 Spin the Wheel"):

    if not names:
        st.error("Please enter at least one name.")

    else:
        st.subheader("Spinning...")

        # Fake spinning animation
        animation_placeholder = st.empty()

        for _ in range(25):
            animation_placeholder.markdown(
                f"## 🎡 {random.choice(names)}"
            )
            time.sleep(0.08)

        # Always choose the fixed winner
        if FIXED_WINNER in names:
            winner = FIXED_WINNER
        else:
            winner = names[0]

        # Show result
        animation_placeholder.markdown(
            f"# 🏆 Winner: **{winner}**"
        )

        st.success(f"The wheel selected: {winner}")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Built with Streamlit + PyCharm")