def gc_content(seq):
    """Calculate the GC content of a DNA sequence."""
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    gc_percentage = (gc_count / len(seq)) * 100
    return round(gc_percentage,2)