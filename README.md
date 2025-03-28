# 🧠 Mini Debate Analyzer

A lightweight, motion-aware debate prep tool built with Python and Streamlit.

This tool helps debaters quickly break down and prep motions by identifying:
- Motion type (policy, evaluative, actor-based)
- Strategic framing questions
- Core frameworks and tensions
- Claim starters and real-world examples

> Ideal for WSDC, BP, Worlds format, or fast prep practice rounds.

---

## 🎤 Example Motion

> This House, as the U.S., would ban private military companies.

### Output:
- **Motion Type**: Actor-based
- **Actor**: The U.S.
- **Framing Questions**: What are state responsibilities in warfare? How do private contractors affect accountability?
- **Frameworks**: Monopoly on violence vs efficiency; legitimacy vs flexibility
- **Example Prompts**: Wagner Group, Blackwater in Iraq, U.S. military contracting

---

## 🚀 Getting Started

### Requirements:
- Python 3.10+
- `streamlit`

### Run locally:

```bash
pip install streamlit
streamlit run app.py
