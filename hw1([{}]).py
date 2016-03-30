def check(example):
    left = '([{'
    right = ')]}'
    pair_round = '()'
    pair_square = '[]'
    pair_curly = '{}'
    l_bracket = []
    for i in example:
        if i in left:
            l_bracket.append(i)
        if i in right:
            if not l_bracket: return False
            elif i in pair_round and l_bracket[-1] in pair_round:
                del l_bracket[-1]
            elif i in pair_square and l_bracket[-1] in pair_square:
                del l_bracket[-1]
            elif i in pair_curly and l_bracket[-1] in pair_curly:
                del l_bracket[-1]
            else: return False
    if not l_bracket: return True
    return False

print (check('(((((((((((((2, 3)))))))))))))'))

