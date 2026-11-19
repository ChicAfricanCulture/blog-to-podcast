import asyncio
import edge_tts
import os

# ==========================================
# EDIT THIS PART: Paste your article text here
# ==========================================
ARTICLE_TEXT = """
Paste the full text of your blog post here.
You can paste multiple paragraphs.
edge-tts will handle the entire text at once.
"""
# ==========================================

OUTPUT_FILE = "podcast.mp3"
VOICE = "en-US-GuyNeural"  # US English male voice. Change to "en-US-AvaNeural" for female.

async def main():
    print(f"Generating audio using voice: {VOICE}")
    communicate = edge_tts.Communicate(ARTICLE_TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    
    # Simple check to ensure the file is not empty
    if os.path.exists(OUTPUT_FILE) and os.path.getsize(OUTPUT_FILE) > 1000:
        print(f"Success! Audio saved to {OUTPUT_FILE} ({os.path.getsize(OUTPUT_FILE)} bytes)")
    else:
        print("Error: Audio file is missing or too small. Check the text or try again.")
        exit(1)

if __name__ == "__main__":
    asyncio.run(main())
