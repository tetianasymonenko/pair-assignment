import pandas as pd
from gc_content import gc_content

def fasta_statistics(sequences):
	"""Return sequence length, N count, and GC percentage for each sequence."""
	rows = []
	for name, sequence in sequences.items():
		sequence = str(sequence).upper()
		length = len(sequence)
		rows.append(
			{
				"name": name,
				"length": length,
				"N_count": sequence.count("N"),
				"N_share_%": round(sequence.count("N") / length * 100, 2),
				"GC_content_%": gc_content(sequence)
			}
		)

	stats = pd.DataFrame(rows).set_index("name")
	return stats

