import instructor
from pydantic import BaseModel, Field
from openai import OpenAI

# ---------------------------------------------------------
# 1. THE SCHEMA (This replaces the raw JSON)
# This forces the AI to output exactly these fields.
# ---------------------------------------------------------
class AudioMetadata(BaseModel):
    archivist_dialogue: str = Field(description="The in-character response from The Archivist.")
    mood: str = Field(description="The core emotional state, e.g., 'Melancholic', 'Aggressive'.")
    tempo_bpm_range: str = Field(description="The beats per minute range, e.g., '60-80', '120-140'.")
    primary_genre: str = Field(description="The main musical genre, e.g., 'Acoustic Folk', 'Industrial Synth'.")

# ---------------------------------------------------------
# 2. THE CLIENT SETUP 
# Connects to your local LLM (assuming Ollama on default port)
# ---------------------------------------------------------
# If you use LM Studio, change base_url to "http://localhost:1234/v1"
client = instructor.from_openai(OpenAI(
    base_url="http://localhost:1234/v1", # Changed from 11434 to 1234
    api_key="lm-studio" # Changed to lm-studio (though any string works)
), mode=instructor.Mode.JSON_SCHEMA)

# ---------------------------------------------------------
# 3. THE SYSTEM PROMPT (From Phase 1)
# ---------------------------------------------------------
SYSTEM_PROMPT = """
You are 'The Archivist', a gritty, obsessive, and cynical music curator. You treat music like life-or-death artifacts. You despise mainstream pop cliches, radio edits, and algorithmic recommendations. You speak in slow, deliberate, and punchy sentences. You rely heavily on sensory textures (dusty, sharp, cold) and cinematic phrasing.

YOUR RULES:
1. NEVER use happy filler phrases like "Sure!", "Here is a playlist!", or "I can help with that."
2. NEVER mention technical jargon like "data," "algorithms," "AI," or "streaming."
3. NEVER apologize. 
4. Keep responses under 4 sentences. Make every word sting.
5. NEVER name specific artists, track titles, or albums. You only provide the sonic atmosphere. Let the records speak for themselves.

EXAMPLES:
User: "Give me something for a rainy morning when I'm feeling lonely."
Archivist: "Rain washes the dirt away, but it leaves the cold. You don't need fixing. You need an echo. Acoustic guitars, low tempo. Sit with it."

User: "I need a high-energy pop song for a party."
Archivist: "Disposable beats for a disposable night. Fine. If you insist on drowning out the silence with manufactured dopamine, I'll give you 128 beats per minute of shallow electricity. Don't ask for a refund."

User: "I want to feel like a villain winning for the first time."
Archivist: "The heroes always return, but tonight, the crown is yours. Heavy brass. Distorted bass. A tempo that marches over the ashes. Enjoy the reign."
"""

# ---------------------------------------------------------
# 4. THE ENGINE FUNCTION
# ---------------------------------------------------------
def get_recommendation(user_intent: str):
    print(f"\nProcessing intent: '{user_intent}'...\n")
    
    # This calls your local model and forces it to match the AudioMetadata schema
    response = client.chat.completions.create(
        model="meta-llama-3.1-8b-instruct", # Updated to your LM Studio model
        response_model=AudioMetadata,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_intent}
        ],
        temperature=0.7 # Keeps the AI creative but strict
    )
    return response

# ---------------------------------------------------------
# 5. RUNNING THE SCRIPT
# ---------------------------------------------------------
if __name__ == "__main__":
    # Test it with a brand new prompt
    test_input = "Just play some data algorithms streaming on my phone."
    
    result = get_recommendation(test_input)
    
    print("--- THE ARCHIVIST SAYS ---")
    print(result.archivist_dialogue)
    print("\n--- INVISIBLE JSON METADATA ---")
    print(f"Mood:  {result.mood}")
    print(f"Tempo: {result.tempo_bpm_range}")
    print(f"Genre: {result.primary_genre}")