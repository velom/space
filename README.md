Интерфейс работы с экземплярами кораблей и планет.

Пример:
```python
>>> from space import *
>>> v = Vessel('velom', [0,0], 1000)
>>> e = Planet('Earth', [100,100], 5000)
>>> m = Planet('Mars', [1000,1000], 000)
>>> m.report()
Mars. Местоположение: [1000, 1000]. Товаров нет.
>>> e.report()
Earth. Местоположение: [100, 100]. Груз: 5000т.
>>> v.flyTo([100,100])
>>> v.report()
velom. Местоположение: [100, 100]. Товаров нет.
>>> e.loadCargoTo(v, 1200)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "space.py", line 49, in loadCargoTo
    raise Exception("Not such free space at %s" % vessel.name)
Exception: Not such free space at velom
>>> e.loadCargoTo(v, 1000)
>>> v.report()
velom. Местоположение: [100, 100]. Груз: 1000т.
>>> e.report()
Earth. Местоположение: [100, 100]. Груз: 4000т.
>>> v.flyTo(m)
>>> m.unloadCargoFrom(v, 1200)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "space.py", line 58, in unloadCargoFrom
    raise Exception("Not such available cargo at %s" % vessel.name)
Exception: Not such available cargo at velom
>>> m.unloadCargoFrom(v, 1000)
>>> m.report()
Mars. Местоположение: [1000, 1000]. Груз: 1000т.
>>> e.report()
Earth. Местоположение: [100, 100]. Груз: 4000т.
>>> v.report()
velom. Местоположение: Mars. Товаров нет.
>>> new = Vessel('new', [100,100], 500)
>>> v.report()
new. Местоположение: Earth. Товаров нет.
```
