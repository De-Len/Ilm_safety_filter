def make_decision(scores, thresholds):
    risk = max(scores.values(), default=0)

    if risk >= thresholds["block"]:
        return "block"
    elif risk >= thresholds["review"]:
        return "llm_check"
    return "allow"