$K>0$ is the irrationality measure for $\alpha$ (1):

$$
0 < |\alpha - \frac{p}{q}| \le \frac{1}{q^K}
$$

$|\{ (p,q) : p,q \in \mathbb{Z}\}|<\infty$ 

$M\subset\mathbb{Z}\times\mathbb{Z}$, where M is the set of pairs $p$,$q$ that satisfy (1), if $M$ is finite then the infimum of all such $K$ is called the irrationality measure $\mu$

Alternative form:

$$
\exists C(\alpha) < \infty, \forall p,q > 0, \\
| \alpha - \frac{p}{q} | > \frac{C(\alpha)}{q^n}
$$

Goal

- Figure out irrationality measure

```python=
#!/usr/bin/python3
import gmpy2
with gmpy2.local_context(gmpy2.context(), precision=100) as ctx:
  x = gmpy2.sqrt(2)
  for q in range(1,10000):
    r = q*x - gmpy2.floor(q*x)
    print(q, r)
```

![](img/upload_7784f257744114cc320ca17389b4899f.png)


```python=
#!/usr/bin/python3
import gmpy2
with gmpy2.local_context(gmpy2.context(), precision=1000) as ctx:
  x = gmpy2.atan(1)*4 #pi
  for q in range(1,10000000):
    r = q*x - gmpy2.floor(q*x)
    print(q, r)
```

![](img/upload_7000b3dc5fa7cb1e915e804e010ea4ff.png)
