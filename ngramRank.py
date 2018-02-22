import kenlm
import sys
import pdb

outfile = open(sys.argv[3], 'w')

print("Loading language model")
lm = kenlm.LanguageModel(sys.argv[1])
on = 0
for line in open(sys.argv[2], 'r').readlines():
    on += 1
    if on % 100 == 0:
        print("Currently on", on)
    line = line.strip()
    line = line.split('\t')
    score = str(lm.score(line[6]))
    perp = str(lm.perplexity(line[6]))
    line += [score, perp]
    outfile.write('\t'.join(line) + '\n')
    # pdb.set_trace()