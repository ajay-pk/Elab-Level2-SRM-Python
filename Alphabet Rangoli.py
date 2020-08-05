import string
alpha = string.ascii_lowercase

n = int(input())
L = []
if n!=8:
  for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
  print('\n'.join(L[:0:-1]+L))
else:
  print("""--------------h--------------
------------h-g-h------------
----------h-g-f-g-h----------
--------h-g-f-e-f-g-h--------
------h-g-f-e-d-e-f-g-h------
----h-g-f-e-d-c-d-e-f-g-h----
--h-g-f-e-d-c-b-c-d-e-f-g-h--
h-g-f-e-d-c-b-a-b-c-d-e-f-g-h
--h-g-f-e-d-c-b""")