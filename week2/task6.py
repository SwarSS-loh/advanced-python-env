def all_eq(lst):
    max = max(len(s) for s in lst) if lst else 0
    return [s + "_" * (max - len(s)) for s in lst]