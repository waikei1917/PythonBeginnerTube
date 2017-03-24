from struct import *

packed_data = pack('iif',6,19,4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('lif'))

#to get bytes data back to normal
original_data = unpack('iif',packed_data)
print(original_data)
print(unpack('iif',b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))

'''
x	pad byte	no value	1
c	char	string of length 1	1
b	signed char	integer	1
B	unsigned char	integer	1
?	_Bool	bool	1
h	short	integer	2
H	unsigned short	integer	2
i	int	integer	4
I	unsigned int	integer or long	4
l	long	integer	4
L	unsigned long	long	4
q	long long	long	8
Q	unsigned long long	long	8
f	float	float	4
d	double	float	8
s	char[]	string	1
p	char[]	string	1
P	void *	long

'''