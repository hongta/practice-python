# Bitwise Operation


### Find complement
set leftmost digit of negative number to 0
```python
def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    mask = 1 << (len(bin(num)) - 2)
    return (mask - 1) ^ num

# or

def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    i = 1
    while i <= num:
        i = i << 1
    return (i - 1) ^ num



```
