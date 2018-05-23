def count_substring(string, sub_string):
    count = 0
    n = len(string)
    m = len(sub_string)
    for i in xrange(0,n-m+1):
        #print string[i:i+m], sub_string
        if string[i:i+m] == sub_string:
            count = count + 1
    return count