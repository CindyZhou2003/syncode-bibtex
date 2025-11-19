# BibTeX Grammar for Constrained LLM Generation with SynCode

## Assignment Overview
Create a Lark LR grammar for BibTeX citation format and use it with SynCode to constrain LLM outputs. This demonstrates how formal grammars can be used to ensure structured output generation from LLMs.

## Timeframe
One week

## Requirements
- Lark parser (`pip install lark-parser`)
- SynCode library (https://github.com/structuredllm/syncode, `pip install syncode`)
- Python 3.8+

## Tasks

### 1. Implement BibTeX Grammar
Create a Lark LALR(1) grammar that:
- Handles all standard BibTeX entry types
- Supports nested braces in field values
- Correctly processes special characters and LaTeX commands
- Is compatible with SynCode's grammar requirements

### 2. Test Grammar
A unit test file will be provided to verify your grammar implementation. The tests include various complex BibTeX examples:

- Nested braces in field values
- Special characters and LaTeX commands
- Mixed quote/brace formatting

Please see a similar ANTLR grammar here: https://github.com/antlr/grammars-v4/tree/master/bibtex (Note: This grammar is not in the Lark format)

### 3. Integrate with SynCode
Create a script that:
- Use your grammar with 
- Tests with at least 3 different prompts asking for BibTeX citations
- Example prompts:
  - "Generate a BibTeX entry for a 3 recent paper on LLM security"
  - "Create a BibTeX citation for a conference paper by authors Smith and Johnson"
  - "Provide the BibTeX entry for RL book Barto and Sutton"

## Deliverables
- `bibtex.lark` - Your Lark grammar file
- `bibtex_syncode.py` - Script for SynCode integration


# Test
`/usr/local/bin/python3 -m unittest test.TestBibTeXGrammar.test_provided_examples`
`/usr/local/bin/python3 test.py`
`/usr/local/bin/python3 bibtex_syncode.py`
