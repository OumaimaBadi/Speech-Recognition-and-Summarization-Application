
## Connect to google drive colab


from google.colab import drive
drive.mount('/content/drive')

"""***Installation of dependencies***"""

!pip install assemblyai

!pip install deep_translator

"""***Display audio***"""

from IPython.display import Audio

# Function to handle audio playback
def play_audio(file_path):
    audio = Audio(file_path)
    display(audio)

# Example usage
audio_file = "/content/drive/MyDrive/marketplace_full.mp3"
play_audio(audio_file)

"""***Speech recognation***"""

import requests
import json
import time

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def upload_file(api_token, path):
    """
    Upload a file to the AssemblyAI API.

    Args:
        api_token (str): Your API token for AssemblyAI.
        path (str): Path to the local file.

    Returns:
        str: The upload URL.
    """
    headers = {'authorization': api_token}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(path))

    if response.status_code == 200:
        return response.json()["upload_url"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def create_transcript(api_token, audio_url):
    """
    Create a transcript using AssemblyAI API.

    Args:
        api_token (str): Your API token for AssemblyAI.
        audio_url (str): URL of the audio file to be transcribed.

    Returns:
        dict: Completed transcript object.
    """
    # Set the API endpoint for creating a new transcript
    url = "https://api.assemblyai.com/v2/transcript"

    # Set the headers for the request, including the API token and content type
    headers = {
        "authorization": api_token,
        "content-type": "application/json"
    }

    # Set the data for the request, including the URL of the audio file to be transcribed
    data = {
        "audio_url": audio_url
    }

    # Send a POST request to the API to create a new transcript, passing in the headers and data
    response = requests.post(url, json=data, headers=headers)

    # Get the transcript ID from the response JSON data
    transcript_id = response.json()['id']

    # Set the polling endpoint URL by appending the transcript ID to the API endpoint
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

    # Keep polling the API until the transcription is complete
    while True:
        # Send a GET request to the polling endpoint, passing in the headers
        transcription_result = requests.get(polling_endpoint, headers=headers).json()

        # If the status of the transcription is 'completed', exit the loop
        if transcription_result['status'] == 'completed':
            break

        # If the status of the transcription is 'error', raise a runtime error with the error message
        elif transcription_result['status'] == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

        # If the status of the transcription is not 'completed' or 'error', wait for 3 seconds and poll again
        else:
            time.sleep(3)

    return transcription_result

your_api_token = "bc7e213c3d14435d9f1e198ce37badb2"

# Upload a local file
filename = "/content/drive/MyDrive/marketplace_full.mp3"
upload_url = upload_file(your_api_token, filename)

# Transcribe it
transcript = create_transcript(your_api_token, upload_url)

# Print the completed transcript object
result=transcript['text']
print(result)

print(transcript)

# Split the transcript into chunks of maximum length 80 characters
chunks = [transcript['text'][i:i+110] for i in range(0, len(transcript['text']), 110)]

# Join the chunks with line breaks
formatted_text = "\n".join(chunks)

print(formatted_text)

"""***Speaker recognation(not completed yet)***"""

import requests
import json
import time

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def upload_file(api_token, path):
    """
    Upload a file to the AssemblyAI API.

    Args:
        api_token (str): Your API token for AssemblyAI.
        path (str): Path to the local file.

    Returns:
        str: The upload URL.
    """
    headers = {'authorization': api_token}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(path))

    if response.status_code == 200:
        return response.json()["upload_url"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def create_transcript(api_token, audio_url):
    """
    Create a transcript using AssemblyAI API.

    Args:
        api_token (str): Your API token for AssemblyAI.
        audio_url (str): URL of the audio file to be transcribed.

    Returns:
        dict: Completed transcript object.
    """
    # Set the API endpoint for creating a new transcript
    url = "https://api.assemblyai.com/v2/transcript"

    # Set the headers for the request, including the API token and content type
    headers = {
        "authorization": api_token,
        "content-type": "application/json"
    }

    # Set the data for the request, including the URL of the audio file to be transcribed
    data = {
        "audio_url": audio_url,
        "speaker_labels": True
    }

    # Send a POST request to the API to create a new transcript, passing in the headers and data
    response = requests.post(url, json=data, headers=headers)

    # Get the transcript ID from the response JSON data
    transcript_id = response.json()['id']

    # Set the polling endpoint URL by appending the transcript ID to the API endpoint
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

    # Keep polling the API until the transcription is complete
    while True:
        # Send a GET request to the polling endpoint, passing in the headers
        transcription_result = requests.get(polling_endpoint, headers=headers).json()

        # If the status of the transcription is 'completed', exit the loop
        if transcription_result['status'] == 'completed':
            break

        # If the status of the transcription is 'error', raise a runtime error with the error message
        elif transcription_result['status'] == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

        # If the status of the transcription is not 'completed' or 'error', wait for 3 seconds and poll again
        else:
            time.sleep(3)

    return transcription_result

your_api_token = "bc7e213c3d14435d9f1e198ce37badb2"

# Upload a local file
filename = "/content/drive/MyDrive/marketplace_full.mp3"
upload_url = upload_file(your_api_token, filename)

# Transcribe it
transcrSpeaker = create_transcript(your_api_token, upload_url)

# Iterate through the utterances and print speaker information
print("\nSpeakers' Information:\n\n")

for utterance in transcrSpeaker['utterances']:
    speaker = utterance['speaker']
    text = utterance['text']
    confidence = utterance['confidence']

    print(f"Speaker {speaker}: {text}\nConfidence: {confidence}\n")

print(transcrSpeaker['utterances'])

"""***Summarization***"""

import requests
import json
import time

def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

def upload_file(api_token, path):
    """
    Upload a file to the AssemblyAI API.

    Args:
        api_token (str): Your API token for AssemblyAI.
        path (str): Path to the local file.

    Returns:
        str: The upload URL.
    """
    headers = {'authorization': api_token}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(path))

    if response.status_code == 200:
        return response.json()["upload_url"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def create_transcript(api_token, audio_url):
    """
    Create a transcript using AssemblyAI API.

    Args:
        api_token (str): Your API token for AssemblyAI.
        audio_url (str): URL of the audio file to be transcribed.

    Returns:
        dict: Completed transcript object.
    """
    # Set the API endpoint for creating a new transcript
    url = "https://api.assemblyai.com/v2/transcript"

    # Set the headers for the request, including the API token and content type
    headers = {
        "authorization": api_token,
        "content-type": "application/json"
    }

    # Set the data for the request, including the URL of the audio file to be transcribed
    data = {
        "audio_url": audio_url,
        "summarization": True,
        "summary_model": "informative",
        "summary_type": "bullets"
    }

    # Send a POST request to the API to create a new transcript, passing in the headers and data
    response = requests.post(url, json=data, headers=headers)

    # Get the transcript ID from the response JSON data
    transcript_id = response.json()['id']

    # Set the polling endpoint URL by appending the transcript ID to the API endpoint
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

    # Keep polling the API until the transcription is complete
    while True:
        # Send a GET request to the polling endpoint, passing in the headers
        transcription_result = requests.get(polling_endpoint, headers=headers).json()

        # If the status of the transcription is 'completed', exit the loop
        if transcription_result['status'] == 'completed':
            break

        # If the status of the transcription is 'error', raise a runtime error with the error message
        elif transcription_result['status'] == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

        # If the status of the transcription is not 'completed' or 'error', wait for 3 seconds and poll again
        else:
            time.sleep(3)

    return transcription_result

your_api_token = "bc7e213c3d14435d9f1e198ce37badb2"

# Upload a local file
filename = "/content/drive/MyDrive/marketplace_full.mp3"
upload_url = upload_file(your_api_token, filename)

# Transcribe it
transcript = create_transcript(your_api_token, upload_url)

# Print the summary
print(transcript["summary"])

"""***Translate the text from english to any language the user want***"""

from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='ar')


# Split the text into smaller chunks
chunk_size = 500  # Adjust as per your needs
chunks = [result[i:i+chunk_size] for i in range(0, len(result), chunk_size)]

# Translate each chunk and store the results
translations = []
for chunk in chunks:
    translation = translator.translate(chunk)
    translations.append(translation)

# Concatenate the translations
translated_text = " ".join(translations)

print(translated_text)

from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='ar')


# Split the text into smaller chunks
chunk_size = 500  # Adjust as per your needs
chunks = [transcript["summary"][i:i+chunk_size] for i in range(0, len(transcript["summary"]), chunk_size)]

# Translate each chunk and store the results
translations = []
for chunk in chunks:
    translation = translator.translate(chunk)
    translations.append(translation)

# Concatenate the translations
translated_text = " ".join(translations)

print(translated_text)

# Split the transcript into chunks of maximum length 80 characters
chunks = [translated_text[i:i+110] for i in range(0, len(translated_text), 110)]

# Join the chunks with line breaks
formatted_text_Trans= "\n".join(chunks)

print(formatted_text_Trans)

from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='fr')

# Iterate through the utterances and print translated speaker information
print("\nInformation des intervenants:\n\n")

for utterance in transcrSpeaker['utterances']:
    speaker = utterance['speaker']
    text = utterance['text']
    confidence = utterance['confidence']

    # Translate the speaker and text
    translated_speaker = translator.translate(speaker)
    translated_text = translator.translate(text)

    print(f"Intervenant {translated_speaker}: {translated_text}\nConfiance: {confidence}\n")

from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='fr')

# Convert the transcrSpeaker object to a string
transcrSpeaker = str(transcrSpeaker)

# Split the text into smaller chunks
chunk_size = 500  # Adjust as per your needs
chunks = [transcrSpeaker[i:i+chunk_size] for i in range(0, len(transcrSpeaker), chunk_size)]

# Translate each chunk and store the results
translations = []
for chunk in chunks:
    translation = translator.translate(chunk)
    translations.append(translation)

# Concatenate the translations
translated_text = " ".join(translations)

print(translated_text)

def print_structured_dialogue(dialogue):
    lines = dialogue.split('?')
    for i in range(0, len(lines), 2):
        if i + 1 < len(lines):
            person1 = lines[i] + '?'
            person2 = lines[i + 1] + '?'
            print(f"Person 1: {person1.strip()}")
            print(f"Person 2: {person2.strip()}")
            print()

# Example usage

print_structured_dialogue(res)

def print_structured_dialogue(dialogue):
    lines = dialogue.split('?')
    for i in range(0, len(lines), 2):
        if i + 1 < len(lines):
            person1 = lines[i] + '.'
            person2 = lines[i + 1] + '.'
            print(f"Person 1: {person1.strip()}")
            print(f"Person 2: {person2.strip()}")
            print()

# Example usage
dialogue = "Salut.Comment allez-vous?Je vais bien merci.Et toi?Ne peut pas se plaindre."
print_structured_dialogue(res)

type(result)
