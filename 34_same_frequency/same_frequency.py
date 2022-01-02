def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_list=[int(a) for a in str(num1)]
    num2_list=[int(a) for a in str(num2)]
    for num in num1_list:
        return num1_list.count(num)!=num2_list.count(num)
    for num in num2_list:
        return num2_list.count(num)!=num1_list.count(num)