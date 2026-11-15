
import streamlit as st
import tempfile
import os
import re
import shutil

from modules.transcriber import Transcriber
from modules.summarizer import summarize_text
from modules.action_extractor import extract_action_items
from modules.audio_extractor import download_audio


# PAGE CONFIGURATION

st.set_page_config(
    page_title="Deep Dive AI",
    page_icon="🎬",
    layout="wide"
)


# HEADER

st.title("🎬 Deep Dive AI")

st.subheader("Turn long recordings into intelligent notes.")

st.write(
    "Transform lectures, videos and recordings "
    "into transcripts, summaries and action items."
)

st.divider()


# INPUT OPTIONS

st.subheader("Choose your input")

upload_tab, url_tab = st.tabs([
    "📁 Upload File",
    "🔗 YouTube URL"
])


uploaded_file = None
youtube_url = ""
process_url = False

with upload_tab:

    uploaded_file = st.file_uploader(
        "Upload your audio or video",
        type=["mp3", "wav", "m4a", "mp4", "webm"]
    )


with url_tab:

    youtube_url = st.text_input(
        "Paste your YouTube URL",
        placeholder="https://www.youtube.com/watch?v=..."
    )

    process_url = st.button("Process YouTube URL")


# TRANSCRIPTION FUNCTION

def process_media(media_path):

    with st.spinner("AI is listening to your recording..."):

        transcriber = Transcriber()

        transcript, language = (
            transcriber.transcribe_audio(media_path)
        )

    full_text = " ".join(
        item["text"] for item in transcript
    )

    return transcript, language, full_text


# DISPLAY RESULTS

def display_results(transcript, language, full_text):

    st.divider()

    st.subheader("📝 Generated Transcript")

    st.caption(f"Detected language: {language}")

    for item in transcript:

        minutes = int(item["start"]) // 60
        seconds = int(item["start"]) % 60

        timestamp = f"{minutes:02}:{seconds:02}"

        st.markdown(
            f"**{timestamp}** — {item['text']}"
        )

    st.divider()

    st.subheader("📚 Summary")

    summary = summarize_text(full_text)

    st.write(summary)

    st.divider()

    st.subheader("✅ Action Items")

    actions = extract_action_items(full_text)

    if actions:

        for action in actions:
            st.write("•", action)

    else:

        st.info("No action items found.")

    st.download_button(
        label="⬇️ Download Transcript",
        data=full_text,
        file_name="deep_dive_transcript.txt",
        mime="text/plain"
    )


# PROCESS UPLOADED FILE

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    st.write("File name:", uploaded_file.name)

    if st.button("Generate Notes"):

        temp_path = None

        try:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=os.path.splitext(uploaded_file.name)[1]
            ) as temp_file:

                temp_file.write(uploaded_file.getvalue())
                temp_path = temp_file.name

            transcript, language, full_text = (
                process_media(temp_path)
            )

            display_results(
                transcript,
                language,
                full_text
            )

        except Exception as error:

            st.error(f"Something went wrong: {error}")

        finally:

            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)


# PROCESS YOUTUBE URL

if process_url:

    if not youtube_url.strip():

        st.warning("Please paste a YouTube URL.")

    elif not re.match(
        r"^https?://(www\.)?(youtube\.com|youtu\.be)/",
        youtube_url.strip()
    ):

        st.error("Please enter a valid YouTube URL.")

    else:

        output_folder = os.path.join(
            tempfile.gettempdir(),
            "deep_dive_ai"
        )

        audio_path = None

        try:

            with st.spinner("Processing supported YouTube media..."):

                audio_path = download_audio(
                    youtube_url.strip(),
                    output_folder
                )

            transcript, language, full_text = (
                process_media(audio_path)
            )

            display_results(
                transcript,
                language,
                full_text
            )

        except Exception as error:

            st.error(f"Something went wrong: {error}")

        finally:

            if os.path.exists(output_folder):
                shutil.rmtree(output_folder)


# FOOTER

st.divider()

st.caption("Deep Dive AI | Build. Learn. Launch.")
