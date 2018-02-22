import sys

lines = open(sys.argv[1], 'r').readlines()
outfile = open(sys.argv[2], 'w')

p_vals = []
n_vals = []

def normal(x, min, max):
    return (x - min)/(max - min)

for l in lines:
    l = l.strip().split('\t')
    neg = float(l[0])
    pos = float(l[1])
    p_vals.append(pos)
    n_vals.append(neg)

p_max = max(p_vals)
p_min = min(p_vals)
n_max = max(n_vals)
n_min = min(n_vals)

for l in lines:
    l = l.strip().split('\t')
    l.append(str(normal(float(l[0]), n_min, n_max)))
    l.append(str(normal(float(l[1]), p_min, p_max)))
    outfile.write('\t'.join(l) + '\n')