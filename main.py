import click
import time
from TTS.api import TTS

ts = time.time()

@click.command()
@click.option(
    "--target_file",
    default="",
    prompt="Path to target speaker file, optional",
    help="The path to the target speaker file. If empty - will just use the default speaker",
)
@click.option(
    "--speaker",
    default="female-en-5",
    prompt="Speaker for default multilingual model: 'female-en-5', 'female-en-5', 'female-pt-4', 'male-en-2', 'male-en-2', 'male-pt-3'",
    help="Speakers for default multilingual model. Only used when target_file is empty. Valid options: 'female-en-5', 'female-en-5', 'female-pt-4', 'male-en-2', 'male-en-2', 'male-pt-3'",
)
@click.option(
    "--language",
    default="en",
    prompt="Language for default multiingual model: 'en', 'fr-fr', 'pt-br'",
    help="Languages for default multiingual model. Only used when target_file is empty. Valid options: 'en', 'fr-fr', 'pt-br'",
)
@click.option(
    "--output_file",
    default=f"/output/output-{ts}.wav",
    prompt="Path to output audio file",
    help="The path to the audio file to output.",
)
@click.option(
    "--model",
    default="tts_models/multilingual/multi-dataset/your_tts",
    prompt="tts model to use. See help for valid options.",
    help="Defaults to tts_models/multilingual/multi-dataset/your_tts. Options can be found via tts --list_models",
)
@click.option(
    "--speech",
    default="This is a test. This voice was generated using text to speech models.",
    prompt="Speech to synthesize",
    help="This is what you want your voice clone to say.",
)
def run(target_file, speaker, language, output_file, model, speech):
    start = time.perf_counter()
    tts = set_model(model)
    if not target_file:
        text_to_speech(tts, model, speaker, language, output_file, speech)
    else:
        synthesize_speech(tts, model, target_file, output_file, speech)
    end = time.perf_counter()
    elapsed_time = end - start
    print("Total elapsed time:", elapsed_time, "seconds")

def set_model(model):
    model_index = 0
    if model:
        model_index = TTS.list_models().index(model)
    model_name = TTS.list_models()[model_index]
    return TTS(model_name)


def text_to_speech(tts, model, speaker, language, output_file, speech):
    print(f'Speakers and Languages available for {model}:')
    print('Speakers:', tts.speakers)
    print('Languages:', tts.languages)

    speaker_index = 0
    if speaker:
        speaker_index = tts.speakers.index(speaker)
    speaker_name = tts.speakers[speaker_index]

    language_index = 0
    if language:
        language_name = tts.languages.index(language)
    language_name = tts.languages[language_index]

    print(
        f"The text \"{speech}\" will be synthesized to \"{output_file}\", using model \"{model}\", speaker \"{speaker}\", language \"{language}\""
    )
    start_tts_to_file = time.perf_counter()
    tts.tts_to_file(text=speech, speaker=speaker_name, language=language_name, file_path=output_file)
    end_tts_to_file = time.perf_counter()
    elapsed_time_for_tts_to_file = end_tts_to_file - start_tts_to_file
    print("Elapsed time for tts_to_file:", elapsed_time_for_tts_to_file, "seconds")

def synthesize_speech(tts, model, target_file, output_file, speech):
    print(
        f"The text \"{speech}\" will be synthesized using target speaker file \"{target_file}\" to \"{output_file}\", using model \"{model}\""
    )
    start_tts_with_vc_to_file = time.perf_counter()
    tts.tts_with_vc_to_file(
        speech,
        speaker_wav=target_file,
        file_path=output_file,
    )
    end_tts_with_vc_to_file = time.perf_counter()
    elapsed_time_for_tts_with_vc_to_file = end_tts_with_vc_to_file - start_tts_with_vc_to_file
    print("Elapsed time for tts_with_vc_to_file:", elapsed_time_for_tts_with_vc_to_file, "seconds")


if __name__ == "__main__":
    run()
