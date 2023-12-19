def we(n,m,w_a,w_b,exchanges):
	for exchange in exchanges:
		w_a,w_b = exchange
		if w_a in ws_a and w_b in ws_b:
			ws_a.remove(w_a)
			ws_b.append(w_a)
			ws_b.remove(w_b)
			ws_a.append(w_b)
			
	ws_a.sort()
	result = ' '.join(ws_a)
	return result


n,m = map(int,input().split())
ws_a = input().split()
ws_b = input().split()

exchanges = [input().split() for _ in range(m)]

result = we(n,m,ws_a,ws_b,exchanges)
print(result)