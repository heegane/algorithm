import sys

def solution(s):
    s = list(map(int,s.rstrip().split()))
    result = str(min(s))+" "+str(max(s))
    return result