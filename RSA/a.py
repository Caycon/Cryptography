# from Crypto.Util.number import *
# from sage.all import *

# e = 65537
# # Different parameters for each team
# N = 25399834187127560616377324812370548757173195169284556539872162671604871757452519233282907652108434123327408232947024502947915469579832631518239713332708158521036624588639774579662120326998800812927107933947317391745532955703923875523455993069144280051980899548298224204528982165205045875719337496741603728894563425753482396643748308742142056199938874535481990266115881794524511870310147791476658785663480386016318423184949506222892970169272928863915576974799698888006120205995339986478217351786809420314719374045082657371833464063781814506611011452446528527462394775717822053092264531338371314173056147348383691680693
# p0 = 30690030687084539848565053327051629412800894538161597167514375082994946489553604097019123037407008578841050511681185164485110466633420466757540466128269516646299876490352434485844798968491360926923292898157483131799018230610798513878098851525346305237410921640772048609630748672
# c = 12215848338373611558115949433223015085106664261456759740008576780433664311999065884357511436672200411146812837497888539079073728643162343495653837366446647675991233150748362505889407215372364638732322069514000168398707821424920609513270834826504932951735086417988920562947118230641305207450705273726733677352838552674136015841963687736367142321138217717812691901752141988569116003461283484769042020988308040283665089094946070393711544634846189363488826570509957947993818778767480702125261100905756351392967073213998362037988847449832496253118455528796006257134060681199708012092728874586714503285151480895621186504268

# PR = PolynomialRing(Zmod(N), names='x,y')
# x, y = PR.gens()
# pol = 2**924 * x + y + p0

# def bivariate(pol, XX, YY, kk=4):
#     N = pol.parent().characteristic()

#     f = pol.change_ring(ZZ)
#     PR,(x,y) = f.parent().objgens()

#     idx = [ (k-i, i) for k in range(kk+1) for i in range(k+1) ]
#     monomials = list(map(lambda t: PR( x**t[0]*y**t[1] ), idx))  # Convert map to list
#     # collect the shift-polynomials
#     g = []
#     for h,i in idx:
#         if h == 0:
#             g.append( y**h * x**i * N )
#         else:
#             g.append( y**(h-1) * x**i * f )

#     # construct lattice basis
#     M = Matrix(ZZ, len(g))
#     for row in range( M.nrows() ):
#         for col in range( M.ncols() ):
#             h,i = idx[col]
#             M[row,col] = g[row][h,i] * XX**h * YY**i

#     # LLL
#     B = M.LLL()

#     PX = PolynomialRing(ZZ, 'xs')
#     xs = PX.gen()
#     PY = PolynomialRing(ZZ, 'ys')
#     ys = PY.gen()

#     # Transform LLL-reduced vectors to polynomials
#     H = [ ( i, PR(0) ) for i in range( B.nrows() ) ]
#     H = dict(H)
#     for i in range( B.nrows() ):
#         for j in range( B.ncols() ):
#             H[i] += PR( (monomials[j]*B[i,j]) / monomials[j](XX, YY) )

#     # Find the root
#     poly1 = H[0].resultant(H[1], y).subs(x=xs)
#     poly2 = H[0].resultant(H[2], y).subs(x=xs)
#     poly = gcd(poly1, poly2)
#     x_root = poly.roots()[0][0]
    
#     poly1 = H[0].resultant(H[1], x).subs(y=ys)
#     poly2 = H[0].resultant(H[2], x).subs(y=ys)
#     poly = gcd(poly1, poly2)
#     y_root = poly.roots()[0][0]

#     return x_root, y_root

# x, y = bivariate(pol, 2**100, 2**100)
# p = 2**924 * x + y + p0
# q = N//p
# assert p*q==N, 'factoring failed'
# d = pow( e,-1, lcm(p-1,q-1) )
# m = pow(c, d, N)
# print('flag: ', long_to_bytes(m))



from Crypto.Util.number import *

e = 65537
N = 25399834187127560616377324812370548757173195169284556539872162671604871757452519233282907652108434123327408232947024502947915469579832631518239713332708158521036624588639774579662120326998800812927107933947317391745532955703923875523455993069144280051980899548298224204528982165205045875719337496741603728894563425753482396643748308742142056199938874535481990266115881794524511870310147791476658785663480386016318423184949506222892970169272928863915576974799698888006120205995339986478217351786809420314719374045082657371833464063781814506611011452446528527462394775717822053092264531338371314173056147348383691680693
p0 = 30690030687084539848565053327051629412800894538161597167514375082994946489553604097019123037407008578841050511681185164485110466633420466757540466128269516646299876490352434485844798968491360926923292898157483131799018230610798513878098851525346305237410921640772048609630748672
c = 12215848338373611558115949433223015085106664261456759740008576780433664311999065884357511436672200411146812837497888539079073728643162343495653837366446647675991233150748362505889407215372364638732322069514000168398707821424920609513270834826504932951735086417988920562947118230641305207450705273726733677352838552674136015841963687736367142321138217717812691901752141988569116003461283484769042020988308040283665089094946070393711544634846189363488826570509957947993818778767480702125261100905756351392967073213998362037988847449832496253118455528796006257134060681199708012092728874586714503285151480895621186504268

PR = PolynomialRing(Zmod(N), names=('x', 'y'))
x, y = PR.gens()
pol = 2**924 * x + y + p0

def bivariate_attack(pol, XX, YY, degree=4):
    N = pol.parent().characteristic()
    f = pol.change_ring(ZZ)
    PR, (x, y) = f.parent().objgens()
    
    idx = [(k - i, i) for k in range(degree + 1) for i in range(k + 1)]
    monomials = [PR(x**t[0] * y**t[1]) for t in idx]
    
    g = [y**h * x**i * N if h == 0 else y**(h - 1) * x**i * f for h, i in idx]
    
    M = Matrix(ZZ, len(g))
    for row in range(M.nrows()):
        for col in range(M.ncols()):
            h, i = idx[col]
            M[row, col] = g[row][h, i] * XX**h * YY**i
    
    B = M.LLL()
    PX, PY = PolynomialRing(ZZ, 'xs'), PolynomialRing(ZZ, 'ys')
    xs, ys = PX.gen(), PY.gen()
    
    H = {i: PR(0) for i in range(B.nrows())}
    for i in range(B.nrows()):
        for j in range(B.ncols()):
            H[i] += PR((monomials[j] * B[i, j]) / monomials[j](XX, YY))
    
    poly_x = gcd(H[0].resultant(H[1], y).subs(x=xs), H[0].resultant(H[2], y).subs(x=xs))
    x_root = poly_x.roots()[0][0]
    
    poly_y = gcd(H[0].resultant(H[1], x).subs(y=ys), H[0].resultant(H[2], x).subs(y=ys))
    y_root = poly_y.roots()[0][0]
    
    return x_root, y_root

x, y = bivariate_attack(pol, 2**100, 2**100)
p = 2**924 * x + y + p0
q = N // p
assert p * q == N, 'Factoring failed'

d = pow(e, -1, lcm(p - 1, q - 1))
m = pow(c, d, N)

print('flag:', long_to_bytes(m))


from Crypto.Util.number import *
flag= b'Trieungu'
p= getPrime(512)
q= getPrime(512)
n= p*q
e= 65537
m= bytes_to_long(flag)
c= pow(m, e, n)
leak_p = int(bin(p)[2:].zfill(512)[40:465], 2) << 47
p0_bitwise = p &((2**472)- (2**47))
print(f'{n= }')
print(f'{e= }')
print(f'{c= }')
print(f'{p= }')
print(f'{leak_p= }')

# n= 95833140363150173085400781562336570561015616460313210023975270126616157131624528587272063057307225026161835408699888323499488279019129501329065630402087285258471135141986496693723213866761952112220188009361594959340470056360323997143701160632189890086147838319540477404939016199414749172031337591306156717957
# e= 65537
# c= 85585941751998800537891696785955548411294697759152457743742952506986880949373120940602110913029788782243069830692032701804087815911677859038561767938618923528464864146810669499058733566518068351509560838577248261272216817539613495749072417594986788748418531887477297026449652895516064864083462020309481181862
# p= 11456457963127424583798262588226103909638173395331112776288736968451860812267255499792030631234202192856091661147772692821692557541694568816668751032441059
# leak_p= 446726636560982512156094109972620717668814180129313191107990193476358979707694308539854517523276106719891732860421584561376386167782984646656