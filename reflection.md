# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

The answer is keeping changing, and also out of bound. When it showing Guess a number between 1 and 100, the result is -35.
It's showing Out of attempts! while it still have attempts.
It also keep showing Game over. Start a new game to try again. after I press New Game.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude suggested that the attempts counters was initialized to 1 instead of 0. I ran the pytest test suite after the fix and confirmed the attempts counter behaved correctly. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I added the # FIXME: Logic breaks here comments, I placed them on lines that were already fixed. The FIXME tag conventionally means "this code still needs fixing," so putting it on corrected lines is misleading.

I verified it by re-read the commented lines after they were added and noticed the comment contradicts the code.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I run pytest, if they all pass, and my manually check and try are all good, I believe that bug was really fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
pytest: test_game_logic.py
The test test_too_high_message_says_go_lower failed on the original code because check_guess(80, 50) was returning "Go HIGHER!" when the guess was too high, which is the opposite of what it should say.

- Did AI help you design or understand any tests? How?
Yes, AI helpp me design and understand. I read them carefully.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
It wasn't actually changing. It stayed the same in session_state. What was changing was the type it was being compared as. In the old code, every even-numbered attempt would convert the secret to a string, which cased Python to fall into the TypeError handler and do string comparison.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you click a button in Streamlit, the entire Python script reruns. All your variables reset to 0. Session state is how you save things across those runs; the game stores the secret number, score, and attemps there.

- What change did you make that finally gave the game a stable secret number?
Change the secret = str(st.session_state.secret) to secret = st.session_state.secret

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One habit from this project is testing habit; I learned new things about pytest.
- What is one thing you would do differently next time you work with AI on a coding task?
I will think more of the bugs before asking AI.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code is fast, but they are not 100% right; you always have to check it, and make sure you fully understand them.