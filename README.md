Make an output and target folder in your working path. In the target folder, put a recording of your own voice, or sample audio of someone talking, of whose voice you want to synthesize. Use the output directory for your generated speech. Both directories will be mounted as volumes to the running container.

Build:
```
docker build -t mytts .
```

Run with unique output file (You can also pass the flags in the progam at the end of the docker command in to avoid the prompts, otherwise each option is prompted):
```
docker run --rm -it -v "$(pwd)\target:/target" -v "$(pwd)\output:/output" --name=mytts mytts
```

Debug:
```
docker run --rm -it -v "$(pwd)\target:/target" -v "$(pwd)\output:/output" --entrypoint /bin/bash --name=mytts mytts --target_file /target/speaker.wav
```

models:
```
[
    "tts_models/multilingual/multi-dataset/your_tts",
    "tts_models/bg/cv/vits",
    "tts_models/cs/cv/vits",
    "tts_models/da/cv/vits",
    "tts_models/et/cv/vits",
    "tts_models/ga/cv/vits",
    "tts_models/en/ek1/tacotron2",
    "tts_models/en/ljspeech/tacotron2-DDC",
    "tts_models/en/ljspeech/tacotron2-DDC_ph",
    "tts_models/en/ljspeech/glow-tts",
    "tts_models/en/ljspeech/speedy-speech",
    "tts_models/en/ljspeech/tacotron2-DCA",
    "tts_models/en/ljspeech/vits",
    "tts_models/en/ljspeech/vits--neon",
    "tts_models/en/ljspeech/fast_pitch",
    "tts_models/en/ljspeech/overflow",
    "tts_models/en/ljspeech/neural_hmm",
    "tts_models/en/vctk/vits",
    "tts_models/en/vctk/fast_pitch",
    "tts_models/en/sam/tacotron-DDC",
    "tts_models/en/blizzard2013/capacitron-t2-c50",
    "tts_models/en/blizzard2013/capacitron-t2-c150_v2",
    "tts_models/es/mai/tacotron2-DDC",
    "tts_models/es/css10/vits",
    "tts_models/fr/mai/tacotron2-DDC",
    "tts_models/fr/css10/vits",
    "tts_models/uk/mai/glow-tts",
    "tts_models/uk/mai/vits",
    "tts_models/zh-CN/baker/tacotron2-DDC-GST",
    "tts_models/nl/mai/tacotron2-DDC",
    "tts_models/nl/css10/vits",
    "tts_models/de/thorsten/tacotron2-DCA",
    "tts_models/de/thorsten/vits",
    "tts_models/de/thorsten/tacotron2-DDC",
    "tts_models/de/css10/vits-neon",
    "tts_models/ja/kokoro/tacotron2-DDC",
    "tts_models/tr/common-voice/glow-tts",
    "tts_models/it/mai_female/glow-tts",
    "tts_models/it/mai_female/vits",
    "tts_models/it/mai_male/glow-tts",
    "tts_models/it/mai_male/vits",
    "tts_models/ewe/openbible/vits",
    "tts_models/hau/openbible/vits",
    "tts_models/lin/openbible/vits",
    "tts_models/tw_akuapem/openbible/vits",
    "tts_models/tw_asante/openbible/vits",
    "tts_models/yor/openbible/vits",
    "tts_models/hu/css10/vits",
    "tts_models/el/cv/vits",
    "tts_models/fi/css10/vits",
    "tts_models/hr/cv/vits",
    "tts_models/lt/cv/vits",
    "tts_models/lv/cv/vits",
    "tts_models/mt/cv/vits",
    "tts_models/pl/mai_female/vits",
    "tts_models/pt/cv/vits",
    "tts_models/ro/cv/vits",
    "tts_models/sk/cv/vits",
    "tts_models/sl/cv/vits",
    "tts_models/sv/cv/vits",
    "tts_models/ca/custom/vits",
    "tts_models/fa/custom/glow-tts",
]
```

speakers:
```
[
    'female-en-5',
    'female-en-5\n',
    'female-pt-4\n',
    'male-en-2',
    'male-en-2\n',
    'male-pt-3\n'
]
```

languages:
```
[
    'en', 
    'fr-fr',
    'pt-br'
]
```