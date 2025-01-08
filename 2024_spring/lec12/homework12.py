from gtts import gTTS

def synthesize(text, lang, filename):
    """
    Use gtts.gTTs(text=text, lang=lang) to synthesize speech, then write it to filename.
    
    @params:
    text (str) - the text you want to synthesize
    lang (str) - the language in which you want to synthesize it
    filename (str) - the filename in which it should be saved
    """
    try:
        tts = gTTS(text=text, lang=lang)  # Create a gTTS object
        tts.save(filename)               # Save the speech to the specified file
    except Exception as e:
        raise RuntimeError(f"Failed to synthesize speech: {e}")
