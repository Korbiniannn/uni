def hasConsecutiveDigits(n):
    """
    >>> hasConsecutiveDigits(-88)
    True
    >>> hasConsecutiveDigits(77)
    True
    >>> hasConsecutiveDigits(64)
    False
    >>> hasConsecutiveDigits(-4546)
    False
    >>> hasConsecutiveDigits(7)
    False
    >>> hasConsecutiveDigits(4556)
    True
    >>> hasConsecutiveDigits(-6477)
    True

    """
    n = str(n)
    if len(n) <= 1:
        return False
    if len(n) > 1:
        if n[0] == n[1]:
            return True
    return hasConsecutiveDigits(str(n)[1:])

         