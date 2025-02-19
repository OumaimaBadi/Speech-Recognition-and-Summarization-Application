# Speech Recognition and Summarization Application

This repository contains the source code for a speech recognition and summarization application. The application allows users to import audio files, transcribe the spoken content into text, and generate concise summaries of the recorded conversations or discussions.

## Features

- **Speech Recognition:** The application utilizes advanced speech recognition technology to accurately convert spoken words into written text. It supports various audio formats and provides high accuracy in transcribing the audio content.

- **Speaker Diarization:** The application includes speaker diarization functionality, which automatically identifies and labels different speakers in the audio recordings. This allows users to attribute spoken text to specific individuals or roles.

- **Summarization:** After transcribing the audio, the application leverages sophisticated algorithms to generate concise summaries of the recorded content. These summaries capture the essential points, key takeaways, and important details from the conversation, enabling users to quickly grasp the main ideas.

- **Customization and Configuration:** The application offers options for customization and configuration based on user preferences. Users can adjust settings such as language selection, summarization length, and translation options.

- **Multilingual Support:** The application provides the ability to translate the transcribed text into different languages, offering multilingual support for diverse user needs.

## Installation

To install and run the application, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using the provided `requirements.txt` file.
3. Launch the application and access it through the provided interface.

## Usage

1. Launch the application.
2. Import an audio file containing the desired conversation or discussion.
3. Wait for the application to transcribe the audio and perform speaker diarization.
4. View the transcribed text with speaker labels and confidence scores.
5. Generate a summary of the conversation to extract the key points and important details.
6. Translate either the script or the summary into the language of your choice.

## Why AssemblyAI?

We have chosen AssemblyAI as our preferred English speech recognition and transcription solution for the following reasons:

1. **Accuracy and Reliability:** AssemblyAI offers highly accurate and reliable speech recognition, ensuring that our audio files are transcribed with precision.
   
3. **Ease of Integration:** AssemblyAI provides a user-friendly API that allows seamless integration into our application. The straightforward documentation and developer-friendly interface make it easy to implement and start transcribing audio.

3. **Support for Long Audio Files:** With AssemblyAI, we can transcribe long audio files, including recordings that span over 30 minutes, ensuring that our application can handle various audio lengths.

4. **Quality Summaries:** AssemblyAI goes beyond speech recognition by offering quality summaries directly from the transcribed text. This feature allows us to generate concise summaries of lengthy audio recordings, enhancing the user experience.

5. **Scalability and Performance:** AssemblyAI's robust infrastructure ensures scalability, allowing our application to handle multiple transcription requests simultaneously without compromising performance.

## Demo Presentation at the Hackathon, Hosted on the LabLab Platform

Experience our Soma project live: [Innovating AI Solutions - Soma on LabLab](https://lablab.me/event/innovating-ai-solutions/summa/summa)

Introducing Soma, the ultimate solution for audio-to-text conversion designed to simplify your workflows. Soma transcends traditional transcription by offering features like multi-language translation, enhancing your global reach. Moreover, its innovative summarization capabilities transform lengthy audio files into concise, actionable insights swiftly.

Engage with our AI chat feature for instant clarification on any content, making it ideal for both English and Arabic speakers, encompassing a vast potential audience of nearly 2 billion globally. Soma is offered through a flexible subscription model, ranging from basic access at no cost to premium tiers for advanced features, ensuring it's accessible to everyone.

Our team is committed to pushing the boundaries of what's possible in audio conversion and translation technology. By investing in Soma, you're joining a forward-thinking venture ready to redefine how we interact with media. Be a part of the change with Soma, where innovation meets practicality.


## Acknowledgements
1- **English speech recognation and summarization with translation**
- [AssemblyAI](https://www.assemblyai.com/): Integrated AssemblyAI's speech recognition API for audio transcription and summarization.
- [GoogleTranslator](https://pypi.org/project/deep-translator/): Utilized GoogleTranslator for language translation.

2- **Arabic speech recognation and summarization**
- SpeechRecognition: This project utilizes the SpeechRecognition library for Python, which provides speech recognition capabilities.
- Arabic Reshaper: The Arabic Reshaper library is used to reshape Arabic text to ensure proper display and rendering.
- python-bidi: The python-bidi library is used to handle bidirectional text, which is essential for displaying Arabic text correctly.
- Summa: The Summa library is used for text summarization, which helps in generating concise arabic summaries of text documents.
   
## Contributors

**AI Team:** BADI Oumaima && ALMUZAINI Rahaf

Feel free to contribute to this project by opening issues, submitting pull requests, or suggesting new features.


## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to the terms of the license.

