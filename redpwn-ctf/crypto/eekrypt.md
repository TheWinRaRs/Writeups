# eekrypt

the xor process leeks info on the flag. we can get upper and lower bits of p and q. here is good resource

[https://github.com/ubuntor/coppersmith-algorithm](https://github.com/ubuntor/coppersmith-algorithm)

* sage go brrr \(turned out my X,Y vals were too high ; has to not be bigger than actual prime \[we dont know this\] but big enough to reduce computation time\)
* get primes
* unxor the original
* get "r3ts.....th3\_fl4g\_1ts3lf!!!!}"

apply root \(raise to power phi / 4 \) if its 1 its square \(has more roots - x prevents this if multiplied in\)

* retrieve bits
* "flag{y0u\_f0und\_m0re\_th4n\_s3c"

full flag

## Flag:flag{y0u\_f0und\_m0re\_th4n\_s3cr3ts.....th3\_fl4g\_1ts3lf!!!!}

```python
def coron(pol, X, Y, k=2, debug=False):
    """
    Returns all small roots of pol.
    Applies Coron's reformulation of Coppersmith's algorithm for finding small
    integer roots of bivariate polynomials modulo an integer.
    Args:
        pol: The polynomial to find small integer roots of.
        X: Upper limit on x.
        Y: Upper limit on y.
        k: Determines size of lattice. Increase if the algorithm fails.
        debug: Turn on for debug print stuff.
    Returns:
        A list of successfully found roots [(x0,y0), ...].
    Raises:
        ValueError: If pol is not bivariate
    """

    if pol.nvariables() != 2:
        raise ValueError("pol is not bivariate")

    P.<x,y> = PolynomialRing(ZZ)
    pol = pol(x,y)

    # Handle case where pol(0,0) == 0
    xoffset = 0

    while pol(xoffset,0) == 0:
        xoffset += 1

    pol = pol(x+xoffset,y)

    # Handle case where gcd(pol(0,0),X*Y) != 1
    while gcd(pol(0,0), X) != 1:
        X = next_prime(X, proof=False)

    while gcd(pol(0,0), Y) != 1:
        Y = next_prime(Y, proof=False)

    pol = P(pol/gcd(pol.coefficients())) # seems to be helpful
    p00 = pol(0,0)
    delta = max(pol.degree(x),pol.degree(y)) # maximum degree of any variable

    W = max(abs(i) for i in pol(x*X,y*Y).coefficients())
    u = W + ((1-W) % abs(p00))
    N = u*(X*Y)^k # modulus for polynomials

    # Construct polynomials
    p00inv = inverse_mod(p00,N)
    polq = P(sum((i*p00inv % N)*j for i,j in zip(pol.coefficients(),
                                                 pol.monomials())))
    polynomials = []
    for i in range(delta+k+1):
        for j in range(delta+k+1):
            if 0 <= i <= k and 0 <= j <= k:
                polynomials.append(polq * x^i * y^j * X^(k-i) * Y^(k-j))
            else:
                polynomials.append(x^i * y^j * N)

    # Make list of monomials for matrix indices
    monomials = []
    for i in polynomials:
        for j in i.monomials():
            if j not in monomials:
                monomials.append(j)
    monomials.sort()

    # Construct lattice spanned by polynomials with xX and yY
    L = matrix(ZZ,len(monomials))
    for i in range(len(monomials)):
        for j in range(len(monomials)):
            L[i,j] = polynomials[i](X*x,Y*y).monomial_coefficient(monomials[j])

    # makes lattice upper triangular
    # probably not needed, but it makes debug output pretty
    L = matrix(ZZ,sorted(L,reverse=True))

    if debug:
        print("Bitlengths of matrix elements (before reduction):")
        print(L.apply_map(lambda x: x.nbits()).str())

    L = L.LLL()

    if debug:
        print("Bitlengths of matrix elements (after reduction):")
        print(L.apply_map(lambda x: x.nbits()).str())

    roots = []

    for i in range(L.nrows()):
        if debug:
            print("Trying row %d" % i)

        # i'th row converted to polynomial dividing out X and Y
        pol2 = P(sum(map(mul, zip(L[i],monomials)))(x/X,y/Y))

        r = pol.resultant(pol2, y)

        if r.is_constant(): # not independent
            continue

        for x0, _ in r.univariate_polynomial().roots():
            if x0-xoffset in [i[0] for i in roots]:
                continue
            if debug:
                print("Potential x0:",x0)
            for y0, _ in pol(x0,y).univariate_polynomial().roots():
                if debug:
                    print("Potential y0:",y0)
                if (x0-xoffset,y0) not in roots and pol(x0,y0) == 0:
                    roots.append((x0-xoffset,y0))
    return roots

size = 1024
low = 496
mid = 400
high = 128


X = Y = 2**(mid-1)

n = 15208002172852064705513549049156125156229213752159018163825621612365155017442357321243997240694068589814280403280924059115680689958405528673283969584726875025903837971544565855345730100919461985993701827484692130096087415066915297046298354141978649627535608324891962634115164448150854962245168416609362554295547467846154568712738134639516660184864893586000423886731114509172379025554849606702807764604046562890333894888196970691461892191718079065215120535321387122435702257687877333759869565354852332910433540118176537491958544695956496612702255403127864825597702515541366203734967406176296928067151309367243599261047

c0 = int("c24b08080224327e3e5c92c9fc01a796",16)
c2 = int("28c7b802e5fd4ed05138cc51adb622bdd2c5eaa3676bc1f4f6fd6f95df7306d33ad44f89d46edc0ae0d2615a4b96ff6a57b6e01bdc1ff0ba7b17690721a1",16)

d0 = int("9ebb4f84833afa3fa4145957bfcaf50b",16)
d2 = int("9968f62b5af28332134fbd88a52db031d4573353acff68f800dfea6a4b97d1f5ca9d999aac7954df3bdf268b216cadf6a9198340ce404e075fef05772817",16)

P.<x,y> = PolynomialRing(ZZ)
pol = ((c0 * (2**(mid+low))) + c2 + (x * (2**low)))*((d0 * (2**(mid+low))) + d2 + (y * (2**low))) - n
print("pol generated")
res = coron(pol, X, Y)
print("ok should give output")
if len(res) > 0:
    p = (c0 * 2**(mid+low) + c2 + res[0][0] * 2**low)
    q = (d0 * 2**(mid+low) + d2 + res[0][1] * 2**low)
    #print(res)
    print('%d, %d' % (p,q))

print(res)
```

Script for doing this

Script to get the output:

```python
def coron(pol, X, Y, k=2, debug=False):
    """
    Returns all small roots of pol.
    Applies Coron's reformulation of Coppersmith's algorithm for finding small
    integer roots of bivariate polynomials modulo an integer.
    Args:
        pol: The polynomial to find small integer roots of.
        X: Upper limit on x.
        Y: Upper limit on y.
        k: Determines size of lattice. Increase if the algorithm fails.
        debug: Turn on for debug print stuff.
    Returns:
        A list of successfully found roots [(x0,y0), ...].
    Raises:
        ValueError: If pol is not bivariate
    """

    if pol.nvariables() != 2:
        raise ValueError("pol is not bivariate")

    P.<x,y> = PolynomialRing(ZZ)
    pol = pol(x,y)

    # Handle case where pol(0,0) == 0
    xoffset = 0

    while pol(xoffset,0) == 0:
        xoffset += 1

    pol = pol(x+xoffset,y)

    # Handle case where gcd(pol(0,0),X*Y) != 1
    while gcd(pol(0,0), X) != 1:
        X = next_prime(X, proof=False)

    while gcd(pol(0,0), Y) != 1:
        Y = next_prime(Y, proof=False)

    pol = P(pol/gcd(pol.coefficients())) # seems to be helpful
    p00 = pol(0,0)
    delta = max(pol.degree(x),pol.degree(y)) # maximum degree of any variable

    W = max(abs(i) for i in pol(x*X,y*Y).coefficients())
    u = W + ((1-W) % abs(p00))
    N = u*(X*Y)^k # modulus for polynomials

    # Construct polynomials
    p00inv = inverse_mod(p00,N)
    polq = P(sum((i*p00inv % N)*j for i,j in zip(pol.coefficients(),
                                                 pol.monomials())))
    polynomials = []
    for i in range(delta+k+1):
        for j in range(delta+k+1):
            if 0 <= i <= k and 0 <= j <= k:
                polynomials.append(polq * x^i * y^j * X^(k-i) * Y^(k-j))
            else:
                polynomials.append(x^i * y^j * N)

    # Make list of monomials for matrix indices
    monomials = []
    for i in polynomials:
        for j in i.monomials():
            if j not in monomials:
                monomials.append(j)
    monomials.sort()

    # Construct lattice spanned by polynomials with xX and yY
    L = matrix(ZZ,len(monomials))
    for i in range(len(monomials)):
        for j in range(len(monomials)):
            L[i,j] = polynomials[i](X*x,Y*y).monomial_coefficient(monomials[j])

    # makes lattice upper triangular
    # probably not needed, but it makes debug output pretty
    L = matrix(ZZ,sorted(L,reverse=True))

    if debug:
        print("Bitlengths of matrix elements (before reduction):")
        print(L.apply_map(lambda x: x.nbits()).str())

    L = L.LLL()

    if debug:
        print("Bitlengths of matrix elements (after reduction):")
        print(L.apply_map(lambda x: x.nbits()).str())

    roots = []

    for i in range(L.nrows()):
        if debug:
            print("Trying row %d" % i)

        # i'th row converted to polynomial dividing out X and Y
        pol2 = P(sum(map(mul, zip(L[i],monomials)))(x/X,y/Y))

        r = pol.resultant(pol2, y)

        if r.is_constant(): # not independent
            continue

        for x0, _ in r.univariate_polynomial().roots():
            if x0-xoffset in [i[0] for i in roots]:
                continue
            if debug:
                print("Potential x0:",x0)
            for y0, _ in pol(x0,y).univariate_polynomial().roots():
                if debug:
                    print("Potential y0:",y0)
                if (x0-xoffset,y0) not in roots and pol(x0,y0) == 0:
                    roots.append((x0-xoffset,y0))
    return roots

size = 1024
low = 496
mid = 400
high = 128


X = Y = 2**(mid-1)

n = 15208002172852064705513549049156125156229213752159018163825621612365155017442357321243997240694068589814280403280924059115680689958405528673283969584726875025903837971544565855345730100919461985993701827484692130096087415066915297046298354141978649627535608324891962634115164448150854962245168416609362554295547467846154568712738134639516660184864893586000423886731114509172379025554849606702807764604046562890333894888196970691461892191718079065215120535321387122435702257687877333759869565354852332910433540118176537491958544695956496612702255403127864825597702515541366203734967406176296928067151309367243599261047

c0 = int("c24b08080224327e3e5c92c9fc01a796",16)
c2 = int("28c7b802e5fd4ed05138cc51adb622bdd2c5eaa3676bc1f4f6fd6f95df7306d33ad44f89d46edc0ae0d2615a4b96ff6a57b6e01bdc1ff0ba7b17690721a1",16)

d0 = int("9ebb4f84833afa3fa4145957bfcaf50b",16)
d2 = int("9968f62b5af28332134fbd88a52db031d4573353acff68f800dfea6a4b97d1f5ca9d999aac7954df3bdf268b216cadf6a9198340ce404e075fef05772817",16)

P.<x,y> = PolynomialRing(ZZ)
pol = ((c0 * (2**(mid+low))) + c2 + (x * (2**low)))*((d0 * (2**(mid+low))) + d2 + (y * (2**low))) - n
print("pol generated")
res = coron(pol, X, Y)
print("ok should give output")
if len(res) > 0:
    p = (c0 * 2**(mid+low) + c2 + res[0][0] * 2**low)
    q = (d0 * 2**(mid+low) + d2 + res[0][1] * 2**low)
    #print(res)
    print('%d, %d' % (p,q))

print(res)
```

