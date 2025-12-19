# Обзор начальной математики и математического анализа

from sympy import *
from sympy.plotting import plot
from sympy.plotting import plot3d

# Объявление линейной функции в Python
def f(x):
    return 2 * x + 1
x_values = [0, 1, 2, 3]
for x in x_values:
    y = f(x)
    print(y)

# Построение графика линейной функции с помощью SymPy
x = symbols('x')
f = 2*x + 1
#plot(f)

x = symbols('x')
f = x**2 + 1
#plot(f)

# Объявление функции с двумя независимыми переменными в Python
x, y = symbols('x y')
f = 2*x + 3*y
#plot3d(f)

# Выполнение суммирования на Python
summation = sum(2*i for i in range(1,6))
print(summation)

# СУММЫ В SYMPY
i,n = symbols('i n')
# перебирает элементы i от 1 до n,
# затем умножает и суммирует
summation = Sum(2*i,(i,1,n))
# задает n равным 5,
# перебирает числа от 1 до 5
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit()) # 30

# УПРОЩЕНИЕ ВЫРАЖЕНИЙ С ПОМОЩЬЮ SYMPY
from sympy import *
x = symbols('x')
expr = x**2 / x**5
print(expr) # x**(-3)

# Вычисление логарифма на Python
from math import log
# 2 в какой степени даст 8?
x = log(8, 2)
print(x) # выводит 3.0

# Вычисление сложных процентов на Python
from math import exp
p = 100
r = .20
t = 2.0
n = 12
a = p * (1 + (r/n))**(n * t)
print(a) # выводит 148.69146179463576

# Вычисление непрерывных процентов на Python
from math import exp
p = 100 # начальный капитал
r = 0.20 # годовая процентная ставка
t = 2.0 # количество лет
a = p * exp(r*t)
print(a) # выводит 149.18246976412703

# Натуральные логарифмы
# в какую степень нужно возвести e, чтобы получить 10?
x = log(10)
print(x) # выводит 2.302585092994046

# число E, вычисление используя предел 

x = symbols('x')
expr = (1 + 1/x)**x
print(expr)
result = limit(expr, x, oo)
print(result) # E
print(result.evalf()) #2.71828182845905

# Производные

#Вычисление производной на Python
def derivative_x(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m
def my_function(x):
    return x**2
slope_at_2 = derivative_x(my_function, 2, .00001)
print(slope_at_2) # выводит 4.000010000000827

#Вычисление производной с помощью SymPy
from sympy import *
# Объявляем символ 'x' для SymPy
x = symbols('x')
# Теперь объявляем функцию через обычный синтаксис Python
f = x**2
# Вычисляем производную функции
dx_f = diff(f)
print(dx_f) # выводит 2*x

#Вычисление производной на Python
def f(x):
    return x**2
def dx_f(x):
    return 2*x
slope_at_2 = dx_f(2.0) # уклон в точке x = 2
print(slope_at_2) # выводит 4.0

# Вычисляем уклон при x = 2
x = symbols('x')
dxf = 2*x
print(dxf.subs(x,2)) # выводит 4

# Частные производные

# Вычисление частных производных с помощью SymPy
from sympy import *
from sympy.plotting import plot3d
# Объявляем символы x и y в SymPy
x,y = symbols('x y')
# Теперь объявляем функцию через обычный синтаксис Python
f = 2*x**3 + 3*y**3
# Вычисляем частные производные по x и y
dx_f = diff(f, x)
dy_f = diff(f, y)
print(dx_f) # выводит 6*x**2
print(dy_f) # выводит 9*y**2
# Выводим график функции
#plot3d(f)


# Вычисление производной и без него приводит к одному и тому же результату
# с использованием цепного правила
from sympy import *

x, y = symbols('x y')
# Производная первой функции
# Задаем имя с нижним подчеркиванием, чтобы не было конфликта переменных
_y = x**2 + 1
dy_dx = diff(_y)
# Производная второй функции
z = y**3 - 2
dz_dy = diff(z)
# Вычисляем производную с помощью цепного правила
# и без него, подставляем функцию y
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain = diff(z.subs(y, _y))

# Цепное правило работает:
# оба варианта дают одинаковый результат
print(dz_dx_chain) # 6*x*(x**2 + 1)**2
print(dz_dx_no_chain) # 6*x*(x**2 + 1)**2

# Интегралы

# Приближенное вычисление интеграла на Python
def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n # ширина каждого прямоугольника
    total_sum = 0
    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        # midpoint — координата по x середины верхней стороны прямоугольника
        total_sum += f(midpoint)
    return total_sum * delta_x
def my_function(x):
    return x**2 + 1
area = approximate_integral(a=0, b=1, n=5, f=my_function)
print(area) # выводит 1.33
# Еще одно приближенное вычисление интеграла на Python
area = approximate_integral(a=0, b=1, n=1000, f=my_function)
print(area) # выводит 1.333333250000001
# И еще одно приближенное вычисление интеграла на Python
area = approximate_integral(a=0, b=1, n=1_000_000, f=my_function)
print(area) # выводит 1.3333333333332733

# Интегрирование с помощью SymPy
from sympy import *
# Объявляем символ x для SymPy
x = symbols('x')
# Объявляем функцию через обычный синтаксис Python
f = x**2 + 1
# Вычисляем интеграл от функции по x в интервале от x = 0 до x = 1
area = integrate(f, (x, 0, 1))
print(area) # выводит 4/3

# Использование пределов для вычисления интегралов
from sympy import *
# Объявляем переменные для SymPy
x, i, n = symbols('x i n')
# Объявляем функцию и интервал
f = x**2 + 1
lower, upper = 0, 1
# Вычисляем ширину и высоту каждого прямоугольника с индексом i
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)
# Перебираем все n прямоугольников и суммируем их площади
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()
# Вычисляем площадь,
# устремив число прямоугольников n к бесконечности
area = limit(n_rectangles, n, oo)
print(area) # выводит 4/3