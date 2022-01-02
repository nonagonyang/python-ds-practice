def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if parens[0]=="(" and len(parens)%2==0:
        for parent in parens:
            if parent!=parens[parens.index(parent)+1] or parent!=parens[parens.index(parent)-1]:
                return True
    else:
        return False