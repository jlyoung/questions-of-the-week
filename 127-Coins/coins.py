import sys

# Beware of the following situation!
# python 2015wk39.py <<< "1 17 33 40"
# 6 [40, 40, 17, 1, 1, 1]

def main(origdenoms):
	currdenoms = sorted(origdenoms, reverse=True)
	coinlist = []
	continuewithcurrdenoms = True
	candidates = []
	while True:
		if not currdenoms:
			return candidates
		if not continuewithcurrdenoms:
			dequeuedcurrdenom = currdenoms.pop(0)
			continuewithcurrdenoms = True
		for coin in currdenoms:
			repeatcoin = True
			while repeatcoin:
				coinlist.append(coin)
				if sum(coinlist) == 100:
					repeatcoin = False
				if sum(coinlist) > 100:
					repeatcoin = False
			if sum(coinlist) == 100:
				continuewithcurrdenoms = False
				candidates.append(coinlist)
				coinlist = []
				break
			if sum(coinlist) > 100:
				poppedcoin = coinlist.pop()
				continue
		if sum(coinlist) != 100:
			continuewithcurrdenoms = False
			coinlist = []
	return candidates

if __name__ == "__main__":
	input = sys.stdin.readline().strip()
	origdenoms = [int(i) for i in input.split()]
	candidates = main(origdenoms)
	sizesortedcandidates = sorted(candidates, key=lambda x: len(x))
	results = sizesortedcandidates[0] if sizesortedcandidates else sizesortedcandidates
	numcoins = len(results)
	print numcoins
