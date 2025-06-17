import json
import textwrap
import random

def wrap_text(text):
    return textwrap.fill(text, width=70)

def ask_question(q):
    print("=" * 70)
    print(f"Question {q['id']}")
    print(wrap_text(q['question']))
    print()

    if q.get("type") == "order":
        items = list(q['options'].items())
        random.shuffle(items)
        shuffled_keys = [chr(65 + i) for i in range(len(items))]
        option_map = {new_k: old_k for new_k, (old_k, _) in zip(shuffled_keys, items)}
        display_options = {new_k: v for new_k, (_, v) in zip(shuffled_keys, items)}

        for key in shuffled_keys:
            print(f"  {key}. {display_options[key]}")

        user_input = input("\nEnter the steps in order (e.g., A,B,C,D): ").strip().upper().split(",")
        mapped_user_input = [option_map.get(choice) for choice in user_input if choice in option_map]
        if mapped_user_input == q['correct']:
            print("\n✅ Correct sequence!")
            print(wrap_text(q['explanation_correct']))
        else:
            print("\n❌ Incorrect sequence.")
            print(wrap_text(q['explanation_incorrect']))
            print("\nCorrect Order:")
            reverse_map = {v: k for k, v in option_map.items()}
            for step in q['correct']:
                label = reverse_map.get(step, '?')
                print(f"  {label} - {q['options'][step]}")

    elif q.get("type") == "match":
        print("\nMatch each option with its function (format: A=1, B=2, ...)")
        options_items = list(q['options'].items())
        matches_items = list(q['matches'].items())
        random.shuffle(options_items)
        random.shuffle(matches_items)

        shuffled_option_keys = [chr(65 + i) for i in range(len(options_items))]
        option_map = {new_k: old_k for new_k, (old_k, _) in zip(shuffled_option_keys, options_items)}
        display_options = {new_k: v for new_k, (_, v) in zip(shuffled_option_keys, options_items)}

        shuffled_match_keys = [str(i + 1) for i in range(len(matches_items))]
        match_map = {new_k: old_k for new_k, (old_k, _) in zip(shuffled_match_keys, matches_items)}
        display_matches = {new_k: v for new_k, (_, v) in zip(shuffled_match_keys, matches_items)}

        for k in shuffled_option_keys:
            print(f"  {k}. {display_options[k]}")
        for k in shuffled_match_keys:
            print(f"  {k}. {display_matches[k]}")

        user_input = input("\nYour matches: ").strip().upper()
        try:
            user_pairs = [pair.split("=") for pair in user_input.split(",") if "=" in pair]
            user_matches = {option_map[k.strip()]: match_map[v.strip()] for k, v in user_pairs}
            correct_matches = {k: str(v) for k, v in q['correct'].items()}

            if user_matches == correct_matches:
                print("\n✅ Correct match!")
                print(wrap_text(q['explanation_correct']))
            else:
                print("\n❌ Incorrect match.")
                print(wrap_text(q['explanation_incorrect']))
                print("\nCorrect Matches:")
                reverse_option_map = {v: k for k, v in option_map.items()}
                reverse_match_map = {v: k for k, v in match_map.items()}
                for k, v in correct_matches.items():
                    option_label = reverse_option_map.get(k, '?')
                    match_label = reverse_match_map.get(v, '?')
                    print(f"  {option_label} = {match_label}")
        except Exception:
            print("\n❌ Invalid match input format. Please use format A=1,B=2,...")

    elif q.get("type") == "multiple":
        items = list(q['options'].items())
        random.shuffle(items)
        key_map = {chr(65 + i): k for i, (k, _) in enumerate(items)}
        reverse_key_map = {v: k for k, v in key_map.items()}
        for i, (key, value) in enumerate(items):
            label = chr(65 + i)
            print(f"  {label}. {value}")

        user_input = input("\nYour answers (e.g., A,C): ").strip().upper()
        user_answers = set(key_map[ans.strip()] for ans in user_input.split(",") if ans.strip() in key_map)
        correct_answers = set(q['correct'])
        if user_answers == correct_answers:
            print("\n✅ Correct!")
            print(wrap_text(q['explanation_correct']))
        else:
            print("\n❌ Incorrect.")
            print(wrap_text(q['explanation_incorrect']))
            correct_str = ", ".join(f"{reverse_key_map[k]} - {q['options'][k]}" for k in q['correct'])
            print(f"\nCorrect Answers: {correct_str}")

    else:
        items = list(q['options'].items())
        random.shuffle(items)
        option_map = {}
        keys = [chr(65 + i) for i in range(len(items))]
        reverse_option_map = {}
        for key, (original_key, value) in zip(keys, items):
            print(f"  {key}. {value}")
            option_map[key] = original_key
            reverse_option_map[original_key] = key

        user_input = input("\nYour answer (A/B/C/D): ").strip().upper()
        while user_input not in option_map:
            user_input = input("Invalid input. Please enter A, B, C, or D: ").strip().upper()

        selected = option_map[user_input]
        if selected == q['correct']:
            print("\n✅ Correct!")
            print(wrap_text(q['explanation_correct']))
        else:
            print("\n❌ Incorrect.")
            if isinstance(q['explanation_incorrect'], dict):
                feedback = q['explanation_incorrect'].get(selected, "That option is incorrect.")
            else:
                feedback = q['explanation_incorrect']
            print(wrap_text(feedback))
            print(f"\nCorrect Answer: {reverse_option_map[q['correct']]} - {q['options'][q['correct']]}")

    print(f"\n📘 Module: {q['module']}")
    print(f"Learn more: {q['link']}")
    print("=" * 70 + "\n")

def run_quiz():
    print("#" * 70)
    print("SC-200 ASCII Quiz App")
    print("Answer each question and get immediate feedback.")
    print("#" * 70)
    with open("questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
    for q in questions:
        ask_question(q)
        input("\nPress Enter to continue to the next question...")

if __name__ == "__main__":
    run_quiz()
