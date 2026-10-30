import streamlit as st
import google.generativeai as genai

# Check if the ESP32 is sending a direct query via URL parameter (e.g., ?prompt=hello)
query_params = st.query_params
if "prompt" in query_params:
    user_query = query_params["prompt"]
    api_key = query_params.get("key", "AQ.Ab8RN6KQiH7njq2u-Q4A_afXGdqOzZ8GENIPwg63r6ymHjYZZg")
    try:
        genai.configure(api_key=api_key)
        system_instruction = (
            "You are a 0.96-inch OLED micro-display layout text format engine. "
            "You must structure the raw answer directly into short lines of maximum 15 characters each. "
            "Break lines explicitly using '\\n'. Max 6 total lines output. Be concise. "
            "Do not use opening introductions, markdown asterisks, or structural headers."
        )
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=system_instruction)
        response = model.generate_content(user_query)
        # Output clean plain text for the ESP32 to read easily
        st.text(response.text)
    except Exception as e:
        st.text(f"Error: {e}")
    st.stop()  # Stop rendering the heavy UI when the ESP32 is just fetching data

# --- Standard Visual UI for Your Browser ---
st.set_page_config(page_title="Project AeroNode AI", page_icon="🖥️", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTextInput > div > div > input { background-color: #161b22; color: white; border-radius: 8px; }
    .stButton>button { width: 100%; background-color: #238636; color: white; border-radius: 8px; font-weight: bold; }
    .stButton>button:hover { background-color: #2ea043; }
    </style>
""", unsafe_allow_html=True)

st.title("🖥️ Project AeroNode AI Hub")
st.caption("Cloud AI Engine optimized for your 0.96-inch OLED micro-display.")

with st.sidebar:
    st.header("⚙️ Settings")
    api_key_input = st.text_input("Gemini API Key", type="password", value="AQ.Ab8RN6KQiH7njq2u-Q4A_afXGdqOzZ8GENIPwg63r6ymHjYZZg")
    st.info("Formatted specifically for 15 characters per line and max 6 lines.")

user_prompt = st.text_input("Enter your prompt for the ESP32 terminal:", "Give a system status update for AeroNode.")

if st.button("🚀 Generate Formatted OLED Output"):
    if not api_key_input:
        st.error("Please enter your Gemini API Key.")
    else:
        try:
            genai.configure(api_key=api_key_input)
            system_instruction = (
                "You are a 0.96-inch OLED micro-display layout text format engine. "
                "You must structure the raw answer directly into short lines of maximum 15 characters each. "
                "Break lines explicitly using '\\n'. Max 6 total lines output. Be concise. "
                "Do not use opening introductions, markdown asterisks, or structural headers."
            )
            model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=system_instruction)
            
            with st.spinner("Formatting response for your OLED screen..."):
                response = model.generate_content(user_prompt)
                ai_output = response.text

            st.success("Success! Here is how it looks on your device:")
            st.markdown("### 📺 OLED Display Simulation Box:")
            st.code(ai_output, language="text")

        except Exception as e:
            st.error(f"An error occurred: {e}")
