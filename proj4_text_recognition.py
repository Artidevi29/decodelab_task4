"""
Project 4: Image or Text Recognition (Basic)
-----------------------------------------------
Goal: implement a basic recognition task using an available library,
run it on sample input, and display the output clearly.

This version does text recognition (OCR) using pytesseract, a Python
wrapper around the open-source Tesseract OCR engine -- a good fit for
"use a pre-trained model or simple library" since Tesseract ships with
its own trained character-recognition models; we're not training
anything ourselves, just calling into it.

Since we don't have a scanned document handy, the script first
*generates* a small sample image containing text (using Pillow), then
runs OCR on that generated image. This keeps the demo fully
self-contained -- no external image needs to be downloaded for it to
run end-to-end.

Run it with: python proj4_text_recognition.py
Requires: Pillow, pytesseract, and the tesseract-ocr system binary.
"""

from PIL import Image, ImageDraw, ImageFont
import pytesseract
import os


SAMPLE_IMAGE_PATH = "sample_text.png"
SAMPLE_TEXT = "AI Internship Project 4\nBasic Text Recognition Demo\nAccuracy matters!"


def create_sample_image(path=SAMPLE_IMAGE_PATH, text=SAMPLE_TEXT):
    """
    Build a simple white-background image with black text on it, so
    there's something concrete to run OCR against without needing an
    external file. Falls back to the default PIL font if no truetype
    font is found on the system, so this doesn't break in a bare
    environment.
    """
    width, height = 500, 200
    image = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
    except OSError:
        font = ImageFont.load_default()

    draw.multiline_text((20, 30), text, fill="black", font=font, spacing=12)
    image.save(path)
    print(f"Sample image created: {path}")
    return path


def run_ocr(image_path):
    """
    Hand the image to Tesseract and get plain text back. image_to_string
    does all the heavy lifting (detecting characters, decoding them into
    text) -- this is the "use a pre-trained model" part of the task,
    since Tesseract's character models are already trained.
    """
    image = Image.open(image_path)
    recognized_text = pytesseract.image_to_string(image)
    return recognized_text.strip()


def run_ocr_with_confidence(image_path):
    """
    Bonus: pytesseract can also return per-word confidence scores, not
    just raw text. Useful for showing the model isn't a black box --
    we can see how sure it was about each word it detected.
    """
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    words_with_confidence = [
        (word, conf)
        for word, conf in zip(data["text"], data["conf"])
        if word.strip() and conf != "-1"
    ]
    return words_with_confidence


def compare_original_vs_recognized(original, recognized):
    """
    Simple accuracy sanity-check: what fraction of the original words
    were actually recovered by OCR, ignoring line breaks and case.
    """
    original_words = original.lower().split()
    recognized_words = recognized.lower().split()

    matched = sum(1 for w in original_words if w in recognized_words)
    accuracy = matched / len(original_words) if original_words else 0

    print(f"\nWord-level match: {matched}/{len(original_words)} ({accuracy:.0%})")


def main():
    print("=== Basic Text Recognition (OCR) ===\n")

    image_path = create_sample_image()

    print("\nRunning OCR on the sample image...")
    recognized_text = run_ocr(image_path)

    print("\n--- Recognized text ---")
    print(recognized_text if recognized_text else "(nothing recognized)")
    print("-----------------------")

    compare_original_vs_recognized(SAMPLE_TEXT, recognized_text)

    print("\n--- Per-word confidence ---")
    for word, conf in run_ocr_with_confidence(image_path):
        print(f"  '{word}'  confidence: {conf}%")

    # Clean up the generated sample so repeat runs start fresh.
    if os.path.exists(image_path):
        os.remove(image_path)


if __name__ == "__main__":
    main()
