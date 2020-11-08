def partitionLabels(labels):
    end = 0
    end_i = 0
    if(len(labels)==1):
        return [1]
    if(len(labels)==0):
        return []
    for i in range(len(labels)):
        try:
            end_i = len(labels)-labels[::-1].index(labels[i])-1
            end = max(end,end_i)
        except:
            None
        if i == end:
            return [i + 1] + partitionLabels(labels[i+1:])



s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))
# try:
#     print(len(s)-s[::-1].index('i')-1)
# finally:
#     print("error")
