from __future__ import division
import mpmath as math
from units import *
from copy import copy

def sqrt(x):
  if hasattr(x,'unit'):
    return math.sqrt(x.number) | x.unit**0.5 
  return math.sqrt(x)  

#trigonometric convenience functions which are "unit aware"
sin=lambda x: math.sin(1.*x)
cos=lambda x: math.cos(1.*x)
tan=lambda x: math.tan(1.*x)
cot=lambda x: math.cot(1.*x)

asin=lambda x: math.asin(x) | rad
acos=lambda x: math.acos(x) | rad
atan=lambda x: math.atan(x) | rad
atan2=lambda x,y: math.atan2(x,y) | rad

#~ cos=math.cos
#~ sin=math.sin
#~ tan=math.tan
#~ cosh=math.cosh
#~ sinh=math.sinh
#~ tanh=math.tanh
#~ acos=math.acos
#~ asin=math.asin
#~ atan=math.atan
acosh=math.acosh
asinh=math.asinh
atanh=math.atanh
#~ atan2=math.atan2
#~ cot=math.cot
coth=math.coth
j=math.j

log=math.log
log10=math.log10
fac=math.fac

e=math.e
pi=math.pi

rnd=math.rand

#unit functions:
def in_base(x):
  if hasattr(x,'unit'):
    return x.in_base()
  return x

def strip(x):
  if hasattr(x,'unit'):
    return x.number
  return x
  
def clean(x):
  if hasattr(x,'unit'):
    return x.simplify()
  return x

def simplify(x):
  if hasattr(x,'unit'):
    return x.to_simple_form()
  return x

def constants():
  return filter(lambda x: isinstance(globals()[x], PhysicalConstant),globals().keys())

def siunits():
  return filter(lambda x: isinstance(globals()[x], core.base_unit),globals().keys())

def named_units():
  return filter(lambda x: isinstance(globals()[x], core.named_unit),globals().keys())

def si_prefixes():
  return ['deca(','hecto(','kilo(','mega(','giga(','terra(','peta(', \
      'exa(','zetta(','yotta(','deci(','centi(','milli(','micro(','nano(','pico(',\
      'femto(','atto(','zepto(','yocto(']

class Expression(list):
  def fix_parentheses(self):
    unclosedleft=0
    unclosedright=0
    express=self.python_string()
    for x in express:
      if(x==')'):
        if(unclosedleft==0):
          unclosedright+=1
        else:
          unclosedleft+=-1  
      if(x=='('):
        unclosedleft+=1  
    self.extend(unclosedleft*[")"])
    for i in range(unclosedright):
      self.insert(0,"(")  
  def python_string(self):
    return "".join(self)
  def pretty_string(self):
    return "".join(self)
    
    
class calcengine(object):

  def __init__(self):
    self.ans=0
    self.history=[Expression()]
    self._i=0

  def pushback_result(self,result):
    self.ans=result

  def pushback_express(self,express):
    self.history.append(express)
    if len(self.history)>100: 
      self.history.pop(0)    
    self._i=len(self.history)

  def forward_express(self):
    if self._i<len(self.history): self._i+=1
    if self._i==len(self.history):
      return Expression()
    return copy(self.history[self._i])

  def backward_express(self):
    if(self._i>0): self._i-=1
    return copy(self.history[self._i])

  def calculate(self,express):
    try:
      result=eval(express.python_string().replace("ans","self.ans"))
    except:
      raise
    else:
      self.pushback_result(result)
      self.pushback_express(express)
      return result  
