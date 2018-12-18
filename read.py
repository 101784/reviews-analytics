data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('總共有', len(data), '筆資料')
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為',sum_len / len(data))

new = []
fff = []
sss = []
for d in data:
	if len(d) < 100:
		new.append(d) 
	elif len(d) > 100 < 200:
		fff.append(d)
	else:
		sss.append(d)
print('總共有', len(new), '筆留言小於100')
print('總共有', len(fff), '筆留言大於100,小於200')
print('總共有', len(sss), '筆留言大於200')
print(new[2])