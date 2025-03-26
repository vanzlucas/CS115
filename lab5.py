def ED(first, second):
    ''' Returns the edit distance between the strings first and second.'''
    if first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        return ED(first[1:], second[1:])
    else:
        substitution = 1 + ED(first[1:], second[1:])
        deletion = 1 + ED(first[1:], second)
        insertion = 1 + ED(first, second[1:])
        return min(substitution, deletion, insertion)

memo = {}
def fastED(first, second):
    if(first, second) in memo:
        return memo[(first,second)]
    if first == '':
        memo[(first,second)] = len(second)
        return len(second)
    elif second == '':
        memo[(first,second)] = len(first)
        return len(first)
    elif first[0] == second[0]:
        answer = fastED(first[1:], second[1:])
        memo[(first,second)] = answer
        return answer
    else:
        substitution = 1 + fastED(first[1:], second[1:])
        deletion = 1 + fastED(first[1:], second)
        insertion = 1 + fastED(first, second[1:])
        answer = min(substitution, deletion, insertion)
        memo[(first, second)] = answer 
        return answer

getSuggestions():
    return list(map(lambda x : (fastED(
