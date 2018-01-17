from __future__ import division
import mpmath as math
from si import *
from values import ScalarQuantity

class PhysicalConstant(ScalarQuantity):
  def __init__(self,quantity):
    ScalarQuantity.__init__(self, quantity.number,quantity.unit)

# misc every day
minute = named('minute','min.', 60 * s)
hour = named('hour','hr', 60 * minute)
day = named('day','day', 24 * hour)
year =   named('year', 'yr', 365.242199 * day)
julianyr = named('julian yr','julianyr',365.25* day)

N = named('newton', 'N', kg * m /s**2)
J = named('joule','J', kg * m **2  * s ** -2)
W = named('watt', 'W', J / s)
F = named('farad','F', s**4*A**2*m**(-2)*kg**(-1))
C = named('coulomb','C', A*s)
V = named('volt','V', J/C)
T = named('tesla','T', kg/A/s/s)
H = named('henry','H', kg * m**2/A**2/s**2)
S = named('siemens', 'S', A/V)
Wb = named('weber','Wb', kg * m**2/A**2/s**2)
Mx = named('maxwell','Mx', 1.e-8*Wb)

amu=named('atomic mass unit', 'amu',1.660538782*10**-27 * kg)
qe=named('electron charge','qe',1.602176487e-19 * C)
eV=named('electron volt','eV', qe*V)

# cgs
g = named('gram','g', 1e-3 * kg)
cm=named('centimeter','cm',0.01*m)
erg = named('energy','erg', 1e-7 * J)

# physical constants
G = PhysicalConstant( 6.673e-11 | m**3/kg/s**2)
kB = PhysicalConstant( 1.3806503 * 10**-23 | m**2 * kg / s**2 / K)
c=PhysicalConstant( 299792458. | m / s)
h=PhysicalConstant( 6.6260689633e-34 | J * s)
hbar=PhysicalConstant( h/2/math.pi )
mu0=PhysicalConstant( 4*math.pi*1.e-7 | N/A**2 )
eps0=PhysicalConstant( mu0**-1*c**-2)
e_mass = PhysicalConstant(9.10938215e-31 | kg )
Avogadro = PhysicalConstant(6.02214179e+23 | mol**-1)
alpha = PhysicalConstant((1/137.035999679) | none )

# astronomical units
AU =  named('astronomical unit', 'AU', 149597870691.0  * m)
parsec=named('parsec','parsec', 3.08568025e16 * m)
kpc=named('kilo parsec','kpc',10**3 * parsec)
Mpc=named('mega parsec','Mpc',10**6 * parsec)
lightyear = named('light year', 'ly', (c*julianyr).to_unit())
LSun = named('solar luminosity', 'LSun', 3.839e26 * W) 
MSun = named('solar mass', 'MSun', 1.98892e30 * kg)
RSun = named('solar radius', 'RSun', 6.955e8 * m)
Myr = named('million year', 'Myr', 1000000 * year)

Pa = named('pascal', 'Pa', N / (m ** 2))

Hz = named('hertz', 'Hz', s**-1)
MHz = named('megahertz', 'MHz', 1e6*Hz)

rad = named('radian','rad',m/m)
rev=named('revolutions','rev',(2*math.pi) * rad)
deg=named('degree','deg',(math.pi/180) *  rad)
arcmin=named('arcminutes', 'arcmin', (1./60) * deg)
arcsec=named('arcseconds', 'arcsec', (1./3600) * deg)

sr = named('steradian','sr',m**2/m**2)

dm=named('decimeter','dm',0.1*m)
liter=named('liter','L', dm**3)

mile=named('mile','mi',1609.344*m)
gallon=named('gallon','gal',3.785412*liter)
km=kilo(m)
