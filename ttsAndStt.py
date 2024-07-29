import os
from deepgram import DeepgramClient, SpeakOptions
import asyncio
import json

# Replace with your Deepgram API key
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

# Initialize the Deepgram client
dg_client = DeepgramClient(DEEPGRAM_API_KEY)


# Speech-to-Text (STT) function
async def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = await dg_client.transcription.prerecorded(source, {'punctuate': True})
        return response['results']['channels'][0]['alternatives'][0]['transcript']


# Text-to-Speech (TTS) function
async def generate_speech(text, voice_id='11Labs-v2-cond'):
    response = await dg_client.speak({
        "text": text,
        "model": "nova-2",
        "voice": voice_id
    })

    # Save the audio to a file
    with open('output.wav', 'wb') as audio_file:
        audio_file.write(response)

    print("Audio saved as output.wav")


# Example usage
async def main():
    # STT example
    # transcript = await transcribe_audio('path/to/your/audio/file.wav')
    # print(f"Transcription: {transcript}")

    # TTS example
    await generate_speech('''### Formal Conversation between an Interviewer and a Candidate

#### Scene: Office Interview Room

**Interviewer:** Good morning, Emily Johnson. Thank you for coming in today. How are you?

**Candidate:** Good morning. I’m doing well, thank you. I appreciate the opportunity to be here.

**Interviewer:** Excellent. Let’s start with you telling me a little about yourself and your background.

**Candidate:** Certainly. My name is Emily Johnson, and I recently graduated from Stanford University with a degree in Computer Science. Over the past few years, I have gained experience in software development through internships at Google and Microsoft. I am particularly interested in artificial intelligence and have developed skills in machine learning and data analysis.

**Interviewer:** That’s great to hear. Could you elaborate on your role at Google and what you learned from that experience?

**Candidate:** Of course. At Google, I worked as a Software Engineering Intern where I was responsible for developing new features for Google Maps. One significant project I was involved in was the enhancement of the real-time traffic prediction algorithm, where I optimized data processing speed. This experience taught me how to handle large datasets efficiently and the importance of user-centric design.

**Interviewer:** It sounds like you had a substantial impact there. Can you describe a challenge you faced during that project and how you overcame it?

**Candidate:** Absolutely. During the traffic prediction project, we encountered significant latency issues. To address this, I restructured the data pipeline and implemented more efficient algorithms, which reduced processing time by 30%. As a result, we were able to improve the user experience significantly. This situation helped me develop my problem-solving and teamwork skills.

**Interviewer:** That’s very insightful. Moving on, why are you interested in working at Tech Innovators Inc.?

**Candidate:** I have always admired Tech Innovators Inc. for its commitment to pioneering new technologies and its collaborative culture. Your commitment to innovation and sustainability aligns with my professional values and career goals. Additionally, I am excited about the opportunity to contribute to your cutting-edge AI projects at Tech Innovators Inc.

**Interviewer:** We appreciate your enthusiasm. How do you see yourself contributing to our team if you were to join us?

**Candidate:** With my background in software development and machine learning, I am confident I can bring technical expertise and innovative thinking to the team. I am particularly eager to work on your AI-driven initiatives and believe my experience in optimizing algorithms and handling big data will allow me to make meaningful contributions.

**Interviewer:** It’s great to see how well your goals align with what we’re looking for. Do you have any questions for us about the role or the company?

**Candidate:** Yes, I do. I am interested in learning more about the mentorship opportunities available within the company. Can you tell me about how Tech Innovators Inc. supports the professional development of its employees?

**Interviewer:** Certainly. At Tech Innovators Inc., we have a robust mentorship program where each new employee is paired with a senior team member who provides guidance and support. Additionally, we offer various professional development workshops and encourage attendance at industry conferences. Does that answer your question?

**Candidate:** Yes, it does. Thank you for the detailed explanation. It’s very helpful.

**Interviewer:** Excellent. We’re nearing the end of our time. Is there anything else you would like to add or any other questions you have?

**Candidate:** I believe we’ve covered the major points. I just want to reiterate my enthusiasm for the role and appreciation for the opportunity to interview today.

**Interviewer:** Thank you, Emily. We appreciate your time and interest in Tech Innovators Inc. We will be in touch soon regarding the next steps. Have a great day.

**Candidate:** Thank you very much. I look forward to hearing from you. Have a great day as well.''')


# Run the async main function
asyncio.run(main())