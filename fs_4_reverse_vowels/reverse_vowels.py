def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    s_li=list(s)
    vowel_li=[letter for letter in s_li if letter in  "aeiouAEIOU"]
    reversed_vowel_li=vowel_li[::-1]
    
    for letter in s_li:
        if letter in "aeiouAEIOU":
            s_li[s_li.index(letter)]=reversed_vowel_li[vowel_li.index(letter)]
    return "".join(s_li)


