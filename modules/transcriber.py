
from faster_whisper import WhisperModel


class Transcriber:

    def __init__(self):
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def transcribe_audio(self, audio_path):

        segments, info = self.model.transcribe(
            audio_path,
            vad_filter=True
        )

        transcript = []

        for segment in segments:
            transcript.append({
                "start": segment.start,
                "end": segment.end,
                "text": segment.text.strip()
            })

        return transcript, info.language
