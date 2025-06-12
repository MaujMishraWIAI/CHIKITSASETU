import pickle
import Levenshtein

def load_common_meds():
    with open("/Users/maujmishra/Desktop/AskWadhwani/media/common_meds.pkl", "rb") as f:
        common_meds = f.load()

    return common_meds

def correct_name(name, common_meds):
    best = name
    best_dist = float('inf')
    for ref in common_meds:
        d = Levenshtein.distance(name.lower(), ref.lower())
        if d < best_dist:
            best_dist = d
            best = ref
    return best if best_dist <= 3 else name