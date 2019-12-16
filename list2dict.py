"""
Esta es la documentación de list2dict.py.
"""

def list2dict(lista):
    """
    Esta función convierte una lista en un diccionario.
    >>> list2dict([9, 14, 31])
    {0: 9, -3: 9, 1: 14, -2: 14, 2: 31, -1: 31}
    >>> list2dict([])
    {}
    """
    dic = {}
    lon = len(lista)
    for i, e in enumerate(lista):
        dic[i] = e
        dic[i - lon] = e
    return dic

def dict2list(dic):
    """
    >>> dict2list({2: 'c', 1: 'b', 0: 'a'})
    ['a', 'b', 'c']
    >>> dict2list({0: 'a', 2: 'c'})
    ['a', None, 'c']
    """
    lista = []
    for i in range(max(dic.keys()) + 1):
        lista.append(dic.get(i))
    return lista

