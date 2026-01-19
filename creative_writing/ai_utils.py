from PIL import Image
from gtts import gTTS
import os
import random

def analyze_image(image_path):
    """
    Analyzes the image to determine its mood based on brightness and dominant colors.
    Returns a string describing the mood.
    """
    try:
        img = Image.open(image_path)
        img = img.resize((150, 150))  # Resize for faster processing

        # Calculate average brightness
        # Convert to grayscale
        gray = img.convert('L')
        # Get histogram
        hist = gray.histogram()
        # Calculate mean brightness
        pixels = sum(hist)
        brightness = sum([i * h for i, h in enumerate(hist)]) / pixels

        # Determine mood based on brightness
        if brightness < 60:
            mood = "Dark and Mysterious"
        elif brightness < 120:
            mood = "Melancholic and Serene"
        elif brightness < 180:
            mood = "Calm and Neutral"
        else:
            mood = "Bright and Cheerful"

        # We could also analyze color (warm vs cold) but brightness is a good start
        return mood
    except Exception as e:
        print(f"Error analyzing image: {e}")
        return "Neutral"

def generate_story(mood):
    """
    Generates a story opening based on the detected mood.
    In a production system, this would call an LLM.
    Here we use a sophisticated template system.
    """

    templates = {
        "Dark and Mysterious": [
            "The shadows lengthened across the cobblestones as the clock struck midnight. A thick fog rolled in from the harbor, obscuring the gas lamps and muffling the sound of distant footsteps. Detective Thorne adjusted his collar against the chill, feeling the weight of the unsolved case pressing down on him. Something in the alleyway shifted, a silhouette darker than the night itself.",
            "Silence hung heavy in the abandoned manor, broken only by the rhythmic dripping of water somewhere deep within the walls. The air tasted of dust and decay. Elena pushed open the heavy oak door, her flashlight beam cutting through the gloom to reveal a grand staircase that had not seen a living soul in decades. Why had the letter brought her here?",
        ],
        "Melancholic and Serene": [
            "Rain tapped a gentle rhythm against the windowpane, blurring the city lights into abstract smears of gold and silver. James sat by the fireplace, the old photograph in his hand worn at the edges. The memories were fading, just like the embers in the hearth, leaving behind a quiet ache that felt strangely comforting in the solitude of the evening.",
            "The autumn leaves drifted slowly to the ground, creating a rust-colored carpet that crunched softly underfoot. The park was empty, save for a lone figure on a bench watching the swans glide across the glassy lake. It was a day for reflection, for looking back at the paths not taken and making peace with the journey.",
        ],
        "Calm and Neutral": [
            "The coffee shop hummed with the low murmur of conversation and the clinking of porcelain. Sunlight filtered through the blinds, casting striped patterns on the wooden tables. Sarah opened her laptop, the blank screen staring back at her. Today was the day she would finally start writing her novel, right after one more sip of her latte.",
            "The train rattled rhythmically along the tracks, a steady lullaby for the commuters heading home. Outside, the landscape shifted from urban sprawl to rolling green hills. Mark watched the world go by, his mind drifting between the meeting he just left and the dinner plans that awaited him. It was just another ordinary Tuesday.",
        ],
        "Bright and Cheerful": [
            "The morning sun burst through the curtains, filling the room with a golden glow that made dust motes dance in the air. Birds were singing a chaotic, joyful chorus in the garden. Lily jumped out of bed with a smile that she couldn't suppress; the day held a promise of adventure, and she wasn't going to waste a single second of it.",
            "Laughter rang out across the beach as waves crashed against the shore, spraying cool mist into the warm air. The scent of salt and sunscreen was everywhere. A group of friends raced towards the water, leaving a trail of footprints in the wet sand. Summer had finally arrived, and with it, the feeling that anything was possible."
        ],
        "Neutral": [
             "The room was quiet. A book lay open on the table.",
        ]
    }

    options = templates.get(mood, templates["Neutral"])
    return random.choice(options)

def text_to_speech(text, output_path):
    """
    Converts text to speech using gTTS and saves it to output_path.
    """
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_path)
        return True
    except Exception as e:
        print(f"Error generating TTS: {e}")
        return False
