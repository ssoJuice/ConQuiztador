# ConQuiztador

ConQuiztador is a terminal-based quiz engine for technical certification practice and self-study. It supports a variety of question types, realistic answer randomization, and contextual feedback with links to supporting material.

## Features

- Supports single-answer, multi-select, ordered steps, and match-type questions
- Randomized option ordering to avoid guess bias
- Clear feedback and module links to reinforce learning
- JSON-driven structure for flexibility and version control

## Requirements

- Python 3.7 or later
- A structured `questions.json` file

## Running the App

```bash
python ascii_quiz_app.py
```

You'll be walked through questions in sequence. After each response, you'll receive immediate feedback along with an explanation and a reference link.

## Question Format

Questions are stored in a JSON array. Example format for a single-answer question:

```json
{
  "id": "Q001",
  "type": "single",
  "question": "Which service provides X?",
  "options": {
    "A": "Option one",
    "B": "Option two",
    "C": "Option three",
    "D": "Option four"
  },
  "correct": "C",
  "explanation_correct": "Option C is correct because...",
  "explanation_incorrect": {
    "A": "Option A is incorrect because...",
    "B": "Option B is incorrect because...",
    "D": "Option D is incorrect because..."
  },
  "module": "Module name",
  "link": "https://learn.microsoft.com/..."
}
```

Other types (multi, order, match) follow similar structure with type-specific fields.

## Suggested Use

Use this app to drill on certification content, practice retention under test conditions, or review weak areas by updating the question pool. Works well as a personal study tool or part of a collaborative prep group.

## Future Enhancements

- CLI flags to filter by module, tag, or difficulty
- Score tracking
- Session review mode
