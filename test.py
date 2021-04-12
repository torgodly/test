data = open('./testdata.txt','r')
def spit(data, cols_before_addr=8, cols_after_addr=1):    
    raw_cols = data.split(',')
    return  raw_cols[:cols_before_addr] \
          + [" ".join(raw_cols[cols_before_addr:-cols_after_addr])] \
          + raw_cols[-cols_after_addr:]

for line in data:
    a = spit(line)
    print(a)

