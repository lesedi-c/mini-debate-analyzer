import streamlit as st
import re

st.title("🧠 Debate Prep Room Argument Generator")
st.subheader("Drop in a motion and get smart, targeted prep prompts")

# --- Motion input ---
motion = st.text_input("🎤 Motion", placeholder="e.g. This House, as the U.S., would ban private military companies")

# --- Motion classification ---
def classify_motion(motion):
    motion = motion.lower()
    if "as" in motion:
        return "Actor", re.findall(r"this house, as (.*?),", motion) or ["an unspecified actor"]
    elif "would" in motion:
        return "Policy", None
    elif "believes that" in motion or "regrets" in motion or "prefers" in motion:
        return "Evaluative", None
    else:
        return "Unknown", None

# --- Show classification ---
if motion:
    motion_type, actor = classify_motion(motion)
    st.markdown(f"### 🧾 Motion Type: `{motion_type}`")
    if actor:
        st.markdown(f"### 🎭 Actor: `{actor[0].capitalize()}`")

    st.markdown("---")
    st.markdown("## 🔍 Key Strategic Questions")

    if motion_type == "Policy":
        st.write("- What is the mechanism for this policy?")
        st.write("- What is the problem it aims to solve?")
        st.write("- Who is the stakeholder implementing it?")
        st.write("- What are short- and long-term effects?")
        st.write("- What trade-offs or harms might it create?")

    elif motion_type == "Actor":
        st.write(f"- What values or interests does `{actor[0]}` represent?")
        st.write("- What are their responsibilities or constraints?")
        st.write("- How would others perceive their action?")
        st.write("- What’s at stake in their context (domestic or global)?")

    elif motion_type == "Evaluative":
        st.write("- What does this motion value or reject?")
        st.write("- What is the standard for good/bad, better/worse?")
        st.write("- What historical or social context matters?")
        st.write("- Are you evaluating an idea, an outcome, or a narrative?")

    else:
        st.write("- What kind of motion is this?")
        st.write("- Can you clarify what “This House” represents?")
        st.write("- Are you advocating action, judgment, or perspective?")

    st.markdown("## 🧭 Possible Framing Approaches")
    if "military" in motion or "security" in motion:
        st.write("- National security vs international norms")
        st.write("- Monopoly on violence vs decentralization")
        st.write("- Professional armies vs ideological fighters")
    elif "education" in motion:
        st.write("- Access vs excellence")
        st.write("- State duty vs private innovation")
        st.write("- Future outcomes vs present equality")
    elif "climate" in motion or "environment":
        st.write("- Economic growth vs sustainability")
        st.write("- Global justice vs local responsibility")
    else:
        st.write("- Rights vs responsibilities")
        st.write("- Collective good vs individual autonomy")
        st.write("- Fairness vs effectiveness")

    st.markdown("## 🔥 Claim Starters")
    st.write("- This policy improves...")
    st.write("- It prevents harm by...")
    st.write("- It strengthens/degrades...")
    st.write("- It is justified because...")
    st.write("- It sets a dangerous/important precedent...")

    st.markdown("## 🧪 Example Prompts")
    if "military" in motion:
        st.write("- Blackwater / Wagner Group")
        st.write("- NATO operations & private contractors")
    elif "education" in motion:
        st.write("- Charter schools in U.S.")
        st.write("- Finland’s public model vs UK’s grammar schools")
    elif "climate" in motion:
        st.write("- Carbon credit systems")
        st.write("- Activist-led pipeline resistance")
    else:
        st.write("- Real-world or historical analogues")
        st.write("- Use pop culture, media, or activism when relevant")
