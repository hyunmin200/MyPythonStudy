str = "Hello goorm!!!"
print(str, type(str))

s0 = set(str) 
print(s0, type(s0))

l = ['a', 'a', 'c', "goorm", "hello", 10, 30, 30]
print(l, type(l))

s1 = set(l) 
print(s1, type(s1))

d = {"Anna":25, "Bob": 23}
print(d, type(d))

s2 = set(d)
print(s2, type(s2))

t = (190,)
print(t, type(t))

s3 = set(t)
print(s3, type(s3))