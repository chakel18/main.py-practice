"""
DNA Translation
Ella Chakravarty

Program transcribes DNA sequence to mRNA to amino acids.
"""

#First start with DNA to mRNA
def transcription(dna_sequence): #define the transcription function
    mrna = dna_sequence.replace('T','U') #Reaplce T with U
    complement = '' #base pair complement
    base_pairs = {'A':'U', 'U':'A', 'C':'G', 'G':'C'} 

#Swap RNA base pairs
    for nucleotide in mrna:
        complement += base_pairs[nucleotide]
    return complement #returns string after replace method

#Translate mRNA sequence into protein sequence using codons
def translate(mrna):
    protein_list = [] #create an empty list to store amino acids
#create amino_acids dictionary for mRNA to codons
    amino_acids = {
    'UUU': 'Phe',
    'UUC': 'Phe',

    'UUA': 'Leu',
    'UUG': 'Leu',
    'CUU': 'Leu',
    'CUC': 'Leu',
    'CUA': 'Leu',
    'CUG': 'Leu',

    'AUU': 'Ile',
    'AUC': 'Ile',
    'AUA': 'Ile',

    'AUG': 'Met',

    'GUU': 'Val',
    'GUC': 'Val',
    'GUA': 'Val',
    'GUG': 'Val',

    'UCU': 'Ser',
    'UCC': 'Ser',
    'UCA': 'Ser',
    'UCG': 'Ser',
    'AGU': 'Ser',
    'AGC': 'Ser',

    'CCU': 'Pro',
    'CCC': 'Pro',
    'CCA': 'Pro',
    'CCG': 'Pro',

    'ACU': 'Thr',
    'ACC': 'Thr',
    'ACA': 'Thr',
    'ACG': 'Thr',

    'GCU': 'Ala',
    'GCC': 'Ala',
    'GCA': 'Ala',
    'GCG': 'Ala',

    'UAU': 'Tyr',
    'UAC': 'Tyr',

    'UAA': 'STOP',
    'UAG': 'STOP',

    'CAU': 'His',
    'CAC': 'His',

    'CAA': 'Gln',
    'CAG': 'Gln',

    'AAU': 'Asn',
    'AAC': 'Asn',

    'AAA': 'Lys',
    'AAG': 'Lys',

    'GAU': 'Asp',
    'GAC': 'Asp',

    'GAA': 'Glu',
    'GAG': 'Glu',

    'UGU': 'Cys',
    'UGC': 'Cys',

    'UGA': 'STOP',

    'UGG': 'Trp',

    'CGU': 'Arg',
    'CGC': 'Arg',
    'CGA': 'Arg',
    'CGG': 'Arg',
    'AGA': 'Arg',
    'AGG': 'Arg',

    'GGU': 'Gly',
    'GGC': 'Gly',
    'GGA': 'Gly',
    'GGG': 'Gly',
}
#Step 2: Iterate over mRNA string
    triplets = [] #empty list to store codons
    for i in range (0, len(mrna), 3): #Break up string into increments of 3
        triplet = mrna[(i): i + (3)] #extract codons
        triplets.append(triplet) #add codons to triplets list

    for codon in triplets:

        protein_list.append(amino_acids[codon]) #add amino acid to protein_list
    return protein_list 

#predefined DNA from example output 
dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'

#call functions to get the proper sequences
mrna = transcription(dna)
protein = translate(mrna)

#Format the output
print('DNA Sequence')
print(dna)
print('mRNA Sequence')
print(mrna)
print('Protein Sequence')
print(' '.join(protein))