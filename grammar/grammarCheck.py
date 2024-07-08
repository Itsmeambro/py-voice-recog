
# pip install language_tool_python

import language_tool_python

def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)

    if len(matches) == 0:
        print("No grammar mistakes found!")
    else:
        print(f"Total grammar mistakes found: {len(matches)}")

        for match in matches:
            print(f"Type: {match.ruleId}")
            print(f"Message: {match.message}")
            print(f"Correction: {match.replacements}")
            print(f"Context: {match.context}\n")


check_grammar("Hello all good morning")