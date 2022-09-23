from xmlrpc.client import boolean


def areRotations(s1,s2)-> boolean:
    if len(s1) != len(s2):
        return False
    return ((s1+s1).find(s2))>0

print (areRotations("ABCD","ABAB"))
