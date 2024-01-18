# secret_santa
В школе перед Новым годом устраивают игру в Тайного Санту. Каждому ученику i выдается ученик a(i), которому он должен подарить подарок.
Костя, как администратор игры, определил каждому школьнику свое число a(i). Но потом его коллега Маша спросила: А правда ли, что если начать цепочку подарков от школьника 1 к школьнику a(1), потом a(a(1)) и так далее, то цепочка замкнется на школьнике 1, после того, как задействует всех остальных учеников ровно по одному разу?
Костя не знает, правда это или нет, но он собирается изменить ровно одно число a(i), чтобы получить конфигурацию, которая устроит Машу. Помогите ему с этим.

Формат входных данных
В первой строке находится натуральное число n - количество школьников (2<=n<=10^5).
В следующей строке находится n натуральных чисел a(i) - ученик, который достался Тайному Санте с номером i(1<=a(i)<=n).

Формат выходных данных
В первой строке выведите два числа (1<=x,y<=n,x!=y) - номер ученика x, которому нужно изменить число a(x), и новое значение a(x).
Должно выполняться условие a(x) != y. Если ответов несколько - выведите любой.
Если сделать это невозможно - выведите  <<-1 -1>>

Примеры:

3

1 2 3
Вывод: -1 -1

3

1 3 1
Вывод: 1 2

Во втором примере после изменения происходят передачи подарков 1→2→3→1﻿.
