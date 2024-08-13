import streamlit as st
import re
from src.helper import voice_input, text_to_speech, llm_model_object

st.set_page_config(page_title="AI Voice Assistant", page_icon="🎙️", layout="centered")

def main():
    st.markdown("<h1 style='text-align: center; font-size: 3em;'>AI Voice Assistant 🎙️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.3em;'>Ask me anything and get a response in text and voice. The audio response can also be downloaded...</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.3em;'>Genrating response takes time, please wait</p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<h3 style='text-align: center; font-size: 1.5em;'>Tips for Better Interaction</h3>", unsafe_allow_html=True)
    st.markdown("""
    - Speak clearly and at a moderate pace.
    - Use the text input if you're in a noisy environment.
    - Ensure your microphone is working properly before starting.
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    response_placeholder = st.empty()
    audio_placeholder = st.empty()
    
    if st.button("🎤 Ask me anything"):
        with st.spinner("Listening..."):
            text = voice_input() 
        if not text:
            st.warning("I couldn't hear you. Please try again.")
            return
        
        with st.spinner("Generating Text..."):
            response = llm_model_object(text)
            response_placeholder.markdown(f"**Response:** {response}")
        
        with st.spinner("Generating Audio..."):
            response = re.sub(r'[^\w\s.,!?]', '', response)
            text_to_speech(response)
            
            audio_file = open("Speech.mp3", "rb")
            audio_bytes = audio_file.read()
            audio_placeholder.audio(audio_bytes, format="audio/mp3")
            
            st.download_button(
                label="💾 Download Speech",
                data=audio_bytes,
                file_name="Speech.mp3",
                mime="audio/mp3"
            )

if __name__ == "__main__":
    main()
