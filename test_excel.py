import csv
 
# .tsv 쓰기    
# f = open('test.tsv', 'w', encoding='utf-8', newline='')
# wr = csv.writer(f, delimiter='\t')
# wr.writerow([1, "김정수", False])
# wr.writerow([2, "박상미", True])
# f.close()
 
# .tsv 읽기
f = open('test.tsv', 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)
# print("Id=%s : Name=%s" % (r[0][0], r[0][1]))
 
print(r)
f.close()