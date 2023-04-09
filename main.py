import click
import time
from TTS.api import TTS


@click.command()
@click.option(
    "--target_file",
    default="/target/speaker.wav",
    prompt="Path to target speaker file",
    help="The path to the target speaker file.",
)
@click.option(
    "--output_file",
    default="/output/output.wav",
    prompt="Path to output audio file",
    help="The path to the audio file to output.",
)
@click.option(
    "--model",
    default="tts_models/en/ljspeech/glow-tts",
    prompt="tts model to use. See help for valid options.",
    help="Defaults to tts_models/en/ljspeech/glow-tts. Options can be found via tts --list_models",
)
@click.option(
    "--speech",
    default="Who is your daddy, and what does he do?",
    prompt="Speech to synthesize",
    help="This is what you want your voice clone to say.",
)
def run(target_file, output_file, model, speech):
    tts = TTS(model)
    print(
        f"The text {speech} will be synthesized using target speaker file {target_file} to {output_file}, using model {model}"
    )
    start = time.perf_counter()
    tts.tts_with_vc_to_file(
        speech,
        speaker_wav=target_file,
        file_path=output_file,
    )
    end = time.perf_counter()
    elapsed_time = end - start
    print("Total elapsed time:", elapsed_time, "seconds")


if __name__ == "__main__":
    run()
