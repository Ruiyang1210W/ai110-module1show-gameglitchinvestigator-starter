from logic_utils import check_guess, get_range_for_difficulty, parse_guess


# --- Existing tests (fixed: check_guess returns a tuple) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug #1: Secret was alternating int/string, causing wrong comparisons ---

def test_check_guess_uses_int_secret():
    # Bug: secret was cast to str on even attempts, making "51" < "9" (string sort)
    outcome, _ = check_guess(51, 9)
    assert outcome == "Too High"  # would wrongly return "Too Low" with string secret "9"

def test_check_guess_correct_with_int_secret():
    # Bug: str(50) compared to int 50 would fail equality check
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


# --- Bug #2: Hint directions were backwards ---

def test_too_high_message_says_go_lower():
    # Bug: "Too High" was returning "Go HIGHER!" instead of "Go LOWER!"
    _, message = check_guess(80, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # Bug: "Too Low" was returning "Go LOWER!" instead of "Go HIGHER!"
    _, message = check_guess(20, 50)
    assert "HIGHER" in message


# --- Bug #6: Hard difficulty range was 1-50 (easier than Normal's 1-100) ---

def test_hard_range_is_harder_than_normal():
    # Bug: Hard returned (1, 50) which is a smaller range than Normal (1, 100)
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high

def test_hard_range_upper_bound():
    # Bug: Hard range was capped at 50 instead of a larger number
    _, high = get_range_for_difficulty("Hard")
    assert high == 200


# --- Bug #7: Info message range (parse_guess sanity check per difficulty) ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100
