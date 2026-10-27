>>> import django
>>> from tasks.models import Inmuebles
>>> Inmuebles.objects.all()
<QuerySet [<Inmuebles: Torre de King Kong>, <Inmuebles: Real departament>, <Inmuebles: Portal de clientes>, <Inmuebles: Nombre del inmueble>]>
>>> 
>>> Inmuebles.objects.create(nombre="Empire state",
... tipo_inmueble="Edificio",
... ubicacion="Gran manzana"
... )
<Inmuebles: Empire state>
>>> edificacion = Inmuebles(nombre="Burf Khalifa", tipo_inmueble="Rascacielos", ubicacion="Arabia Saudita")
>>> edificacion.save()
Inmuebles.objects.all()
<QuerySet [<Inmuebles: Torre de King Kong>, <Inmuebles: Real departament>, <Inmuebles: Portal de clientes>, <Inmuebles: Nombre del inmueble>, <Inmuebles: Empire state>, <Inmuebles: Burf Khalifa>]>
>>> 
>>> Inmuebles.objects.get(nombre="Burf Khalifa")
<Inmuebles: Burf Khalifa>
>>> 
>>> Inmuebles.objects.get(pk=1)
<Inmuebles: Torre de King Kong>
>>> 
>>> Inmuebles.objects.get(pk=3)
<Inmuebles: Portal de clientes>
>>> 
>>> Inmueble.objects.get(name="No existe")
Traceback (most recent call last):
  File "/usr/lib/python3.12/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<console>", line 1, in <module>
NameError: name 'Inmueble' is not defined. Did you mean: 'Inmuebles'?
>>> Inmuebles.objects.get(name="No existe")
Traceback (most recent call last):
  File "/usr/lib/python3.12/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<console>", line 1, in <module>
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/query.py", line 708, in get
    clone = self._chain() if self.query.combinator else self.filter(*args, **kwargs)
                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/query.py", line 1701, in filter
    return self._filter_or_exclude(False, args, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/query.py", line 1719, in _filter_or_exclude
    clone._filter_or_exclude_inplace(negate, args, kwargs)
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/query.py", line 1729, in _filter_or_exclude_inplace
    self._query.add_q(Q(*args, **kwargs))
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/sql/query.py", line 1680, in add_q
    clause, _ = self._add_q(q_object, can_reuse)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/sql/query.py", line 1712, in _add_q
    child_clause, needed_inner = self.build_filter(
                                 ^^^^^^^^^^^^^^^^^^
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/sql/query.py", line 1550, in build_filter
    lookups, parts, reffed_expression = self.solve_lookup_type(arg, summarize)
                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/sql/query.py", line 1357, in solve_lookup_type
    _, field, _, lookup_parts = self.names_to_path(lookup_splitted, self.get_meta())
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/sql/query.py", line 1846, in names_to_path
    raise FieldError(
django.core.exceptions.FieldError: Cannot resolve keyword 'name' into field. Choices are: created_at, id, nombre, tipo_inmueble, ubicacion
>>> 
https://francisco-higuera.site/tutorials/django-framework-desde-cero