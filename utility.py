def reduce_left(seq):
    new_seq = [x for x in seq if x != 0]
    while(len(new_seq) < len(seq)):
        new_seq.append(0)
    seq = new_seq
    #print(seq)
    for i in range(0, len(seq) - 1):
        #print(i)
        if seq[i] == seq[i+1]:
            seq[i] = seq[i]*2
            j = i+1
            while(j < len(seq) -1):
                seq[j], seq[j+1] = seq[j+1], 0
                j = j+1
                #print(seq)            
        elif seq[i] == 0:
            j = i
            while(j < len(seq) -1):
                seq[j], seq[j+1] = seq[j+1], 0
                j = j+1
                #print(seq)
    return seq

def reduce_right(seq):
    new_seq = [x for x in seq if x != 0]
    zero_seq = [x for x in seq if x == 0]
    zero_seq.extend(new_seq)
    seq = zero_seq
    #print(seq)
    for i in range(len(seq)-1, 0, -1):
        #print(i)
        if seq[i] == seq[i-1]:
            seq[i] = seq[i]*2
            j = i-1
            while(j > 0):
                seq[j], seq[j-1] = seq[j-1], 0
                j = j-1
                #print(seq)            
        elif seq[i] == 0:
            j = i
            while(j > 0):
                seq[j], seq[j-1] = seq[j-1], 0
                j = j-1
                #print(seq)
    return seq    

def rowsToCol(row1:list, row2:list, row3:list, row4:list):
    board = [row1, row2, row3, row4]
    col1 = [x[0] for x in board]
    col2 = [x[1] for x in board]
    col3 = [x[2] for x in board]
    col4 = [x[3] for x in board]
    return col1, col2, col3, col4

def colToRows(col1:list, col2:list, col3:list, col4:list):
    board = [col1, col2, col3, col4]
    row1 = [x[0] for x in board]
    row2 = [x[1] for x in board]
    row3 = [x[2] for x in board]
    row4 = [x[3] for x in board] 
    return row1,row2,row3,row4

def strToInt(string:str):
    return int(string[0])
