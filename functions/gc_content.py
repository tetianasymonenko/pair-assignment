def gc_content(seq):
    """Calculate the GC content of a DNA sequence."""
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    gc_percentage = (gc_count / len(seq)) * 100
    return round(gc_percentage,2)

def gc_content1(seq):
    """Calculate GC content of our DNA sequence."""

    gc_count = 0
    seq = seq.upper()
    for x in seq:
        if x == "G" or x == "C":
            gc_count += 1

    gc_percentage = (gc_count / len(seq)) * 100
    return round(gc_percentage, 1)

