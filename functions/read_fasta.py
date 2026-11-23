def read_fasta(path):
    """
    Reads a FASTA file and returns a dictionary mapping sequence names to sequences.

    Parameters:
        path (str): The path to the FASTA file.

    Returns:
        dict: A dictionary where keys are sequence names and values are sequences as strings.
        Empty sequences are removed from the dictionary. Empty sequence names (no text after ">") are ignored. 
        For a duplicate sequence names one last sequence from the file is kept in the dictionary.
    """

    sequences = {}
    name = None

    """Read the FASTA file line by line, extracting sequence names and sequences."""
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                name = line[1:]
                sequences[name] = ""
            else:
                sequences[name] += line
        
    """Check for empty sequences and remove them from the dictionary."""
    empty_sequences = []
    for name, sequence in list(sequences.items()):
        if not sequence:
            empty_sequences.append(name)
            del sequences[name]
    if empty_sequences:
        print(f"Empty sequences found and removed from the dictionary: {empty_sequences}")

    """Check for sequences with no name defined and remove them from the dictionary."""
    for name, sequence in list(sequences.items()):
        if name == "":
            print(f"Sequence(s) with no name defined is in the file and is removed from the dictionary")
            del sequences[name]
    
    return sequences


