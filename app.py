import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuration
# Securely fetch the key from Streamlit's hidden secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. UI Styling (The "Financial Fortress" Theme)
st.set_page_config(page_title="ImpulseGuard", page_icon="🛡️")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    .stButton>button { background-color: #38bdf8; color: white; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ImpulseGuard")
st.write("Your AI-Powered Financial Fortress.")

# 3. App Logic
uploaded_file = st.file_uploader("Upload your shopping cart screenshot...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Impulse Detected!", use_container_width=True)
    
    if st.button("ACTIVATE SHIELD"):
        with st.spinner("Analyzing financial traps..."):
            # This is your Golden Prompt
            prompt = """
            Act as ImpulseGuard, my Financial Fortress. 
            1. Scan for Dark Patterns/Marketing Traps.
            2. Convert total cost to Laundry Loads (₹100) and Campus Meals (₹150).
            3. Give a RED/YELLOW/GREEN shield verdict.
            4. If RED, give a 15-minute mindfulness task.
            Output in bold, structured bullet points.
            """
            response = model.generate_content([prompt, image])
            st.markdown("---")
            st.success("Analysis Complete")
            st.markdown(response.text)