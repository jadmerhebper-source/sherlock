# Visual Storyteller

A creative writing interface where users upload an initial image, and the AI analyzes the mood and scene to ghostwrite an opening paragraph to a story set in that world. It also includes a "Read Aloud" feature.

## Setup

1.  Navigate to the project root.
2.  Install dependencies:
    ```bash
    pip install flask pillow gTTS
    ```

## Usage

1.  Run the Flask application:
    ```bash
    python creative_writing/app.py
    ```
2.  Open your browser and navigate to `http://localhost:5000`.
3.  Upload an image to generate a story.

## Features

*   **Image Analysis**: Analyzes image brightness and mood.
*   **Story Generation**: Generates a thematic story opening based on the analyzed mood.
*   **Text-to-Speech**: Narrates the generated story using an AI voice.
