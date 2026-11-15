
import os
import yt_dlp


def download_audio(youtube_url, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    output_template = os.path.join(
        output_folder,
        "youtube_audio.%(ext)s"
    )

    options = {
        "format": "m4a/bestaudio/best",
        "outtmpl": output_template,
        "noplaylist": True,
        "quiet": True
    }

    try:

        with yt_dlp.YoutubeDL(options) as ydl:

            info = ydl.extract_info(
                youtube_url,
                download=True
            )

            audio_path = ydl.prepare_filename(info)

            return audio_path

    except Exception as error:

        raise RuntimeError(
            f"Unable to process this URL: {error}"
        )
