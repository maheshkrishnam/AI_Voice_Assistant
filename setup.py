from setuptools import find_packages, setup

setup(
    name="AI Voice Assistant",
    version="0.0.0",
    author="Mahesh Krishnam",
    author_email="220120011@iitdh.ac.in",
    description=('An AI Voice Assistant that will answer all you wierd questions, just try it out!!'),
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)
