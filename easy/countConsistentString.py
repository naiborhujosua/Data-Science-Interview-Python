def countConsistentString(words,allowed):
    return [sum(w.issubset(a) for w in map(set, words)) for a in [set(allowed)]][0]