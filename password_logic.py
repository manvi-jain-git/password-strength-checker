def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_num = False
    has_spch = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_num = True
        if ch in "@#$&*":
            has_spch = True

    feedback = []

    if len(password) < 8:
        feedback.append("Password must be at least 8 characters")

    if not has_upper:
        feedback.append("Add an uppercase letter")
    if not has_lower:
        feedback.append("Add a lowercase letter")
    if not has_num:
        feedback.append("Add a number")
    if not has_spch:
        feedback.append("Add a special character (@#$&*)")

    score = has_upper + has_lower + has_num + has_spch

    if len(password) < 8 or score <= 1:
        strength = "WEAK"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "MEDIUM"

    return strength, feedback
