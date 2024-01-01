
f = open('data/Stock-Portfolio-Diversification - BBCA.csv', 'r')

fsec = open('data/clean.csv', 'w')
for line in f:
    line = line.strip('\n')
    line = line.split('\t')
    fsec.write(','.join(line) + '\n')

f.close()
fsec.close()