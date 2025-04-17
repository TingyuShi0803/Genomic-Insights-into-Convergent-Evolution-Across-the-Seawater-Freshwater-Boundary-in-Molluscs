ctl.py Script Documentation
Purpose: This script generates control files (.ctl) for PAML analysis.

Input File Requirements
Sequence File
Filename: filename.fa (Original FASTA file containing 800 orthologs)
Processed Format: Converted to PHYLIP format with the naming convention OG{number}.phy (e.g., OG001.phy, OG002.phy).
The first line must specify the number of taxa and sequence length (e.g., 12 1989 for 12 species and 1989 nucleotides) .
Ensure sequences are codon-aligned, length is a multiple of three, and termination codons are removed .
Tree File
Format: Newick format (.treefile), named as OG{number}_mulber.treefile (e.g., OG001_mulber.treefile).
Tree structure must match the species in the corresponding .phy file .
