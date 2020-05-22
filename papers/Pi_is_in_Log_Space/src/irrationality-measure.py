#!/usr/bin/python3

import gmpy2

with gmpy2.local_context(gmpy2.context(), precision=1000) as ctx:
  x = gmpy2.atan(1)*4
  #x = gmpy2.sqrt(2)

  for q in range(1,10000000):
    r = q*x - gmpy2.floor(q*x)
    print(q, r)
