# bibtex_syncode.py

import os
from syncode import Syncode

# Ensure this points to your V15 grammar file
GRAMMAR_FILE = "bibtex.lark"
MODEL_NAME = "google/gemma-2-2b-it"

prompts = [
    "Generate a BibTeX entry for 3 recent papers on LLM security",
    "Create a BibTeX citation for a conference paper by authors Smith and Johnson",
    "Provide the BibTeX entry for the RL book by Barto and Sutton"
]

# --- Few-Shot Prompt ---
# IMPORTANT: Because we use .format(), all literal braces in the BibTeX
# examples MUST be escaped by doubling them (e.g., {{ }}).
# The {user_request} placeholder remains single braces.

FEW_SHOT_TEMPLATE = """You are a research assistant compliant with BibTeX syntax. 
You MUST generate valid BibTeX entries starting immediately with '@'.
Do not add any introduction, explanation, or markdown formatting.
CRITICAL RULES:
1. Start EVERY entry with @entrytype{{identifier,
2. Use braces {{}} for all field value
3. Each field must be on a new line with 2-space indentation
4. Field format: fieldname = {{value}},
5. End each entry with }} on its own line

User: {user_request}
Assistant:
@"""

# --- Main Execution ---

def main():
    if not os.path.exists(GRAMMAR_FILE):
        print(f"Error: Grammar file not found at '{GRAMMAR_FILE}'")
        print("Please make sure 'bibtex.lark' is in the same directory.")
        return

    print(f"Initializing SynCode with model: '{MODEL_NAME}' and grammar: '{GRAMMAR_FILE}'")
    
    try:
        syn_llm = Syncode(
            model=MODEL_NAME,
            mode="original",
            grammar=GRAMMAR_FILE,
            parser='lalr',
            parse_output_only=True,
            # INCREASED LIMIT: 2048 tokens allows for multiple, long BibTeX entries.
            max_new_tokens=2048 
        )
    except Exception as e:
        print(f"\n--- Model Loading Error ---")
        print(f"Failed to load model '{MODEL_NAME}': {e}")
        return

    print("Initialization complete. Running prompts...\n")

    for i, prompt_text in enumerate(prompts):
        print("=" * 60)
        print(f"PROMPT {i + 1}:\n{prompt_text}\n")
        
        # Format the prompt
        full_prompt = FEW_SHOT_TEMPLATE.format(user_request=prompt_text)
        
        # CRITICAL PROMPT TWEAK: Add a newline to encourage starting the first field.
        # The grammar expects WS? before field_list, and a newline is a great WS.
        full_prompt += '\n' 
        
        messages = [
            {"role": "user", "content": full_prompt},
        ]

        try:
            output = syn_llm.infer(messages)[0]
            
            print(f"SYNCODE-CONSTRAINED OUTPUT:\n")
            print(output.strip())
            
        except Exception as e:
            print(f"An error occurred during inference for this prompt: {e}")

        print("=" * 60 + "\n")

if __name__ == "__main__":
    main()