import streamlit as st
import google.generativeai as genai

# Page configuration for a clean UI
st.set_page_config(page_title="Project AeroNode AI", page_icon="🖥️", layout="centered")

# Custom UI Styling for a sleek, modern look optimized for your project
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #161b22;
        color: white;
        border-radius: 8px;
    }
    .stButton>button {
        width: 100%;
        background-color: #238636;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2ea043;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🖥️ Project AeroNode AI Hub")
st.caption("Cloud AI Engine optimized for your 0.96-inch OLED micro-display.")

# Sidebar for configuration and secret API key input
with st.sidebar:
    st.header("⚙️ Settings")
    api_key_input = st.text_input("Gemini API Key", type="password", value="AQ.Ab8RN6KQiH7njq2u-Q4A_afXGdqOzZ8GENIPwg63r6ymHjYZZg")
    st.info("Your AI is pre-configured to format outputs specifically for 15 characters per line and max 6 lines.")

# Main interactive user prompt section
user_prompt = st.text_input("Enter your prompt for the ESP32 terminal:", "Give a system status update for AeroNode.")

if st.button("🚀 Generate Formatted OLED Output"):
    if not api_key_input:
        st.error("Please enter your Gemini API Key.")
    else:
        try:
            # Configure Gemini API
            genai.configure(api_key=api_key_input)
            
            # Strict formatting instructions for your 0.96-inch OLED screen
            system_instruction = (
                "You are a 0.96-inch OLED micro-display layout text format engine. "
                "You must structure the raw answer directly into short lines of maximum 15 characters each. "
                "Break lines explicitly using '\\n'. Max 6 total lines output. Be concise. "
                "Do not use opening introductions, markdown asterisks, or structural headers."
            )

            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=system_instruction
            )

            with st.spinner("Formatting response for your OLED screen..."):
                response = model.generate_content(user_prompt)
                ai_output = response.text

            st.success("Success! Here is how it will look on your device:")
            
            # Display UI Preview box mimicking the tiny screen layout
            st.markdown("### 📺 OLED Display Simulation Box:")
            st.code(ai_output, language="text")

        except Exception as e:
            st.error(f"An error occurred: {e}")
