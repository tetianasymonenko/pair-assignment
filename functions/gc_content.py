def gc_content(seq):
    """Calculate the GC content of a DNA sequence."""
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    gc_percentage = (gc_count / len(seq)) * 100
    return round(gc_percentage,2)

def complementary_strand(seq):
    """Return the complementary DNA strand for our given DNA sequence."""
    complement_map = { "A": "T", "T": "A", "C": "G", "G": "C", "N": "N" }

    complement = []
    seq = seq.upper()
    for x in seq:
        if x not in complement_map:
            raise ValueError(f"Invalid DNA base: '{x}'")
        else:
            complement.append(complement_map[x])
    return "".join(complement)
