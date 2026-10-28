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
Inmuebles.objects.get(ubicacion__icontains="a")
Traceback (most recent call last):
  File "/usr/lib/python3.12/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<console>", line 1, in <module>
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/query.py", line 725, in get
    raise self.model.MultipleObjectsReturned(
tasks.models.Inmuebles.MultipleObjectsReturned: get() returned more than one Inmuebles -- it returned 3!

Inmuebles.objects.filter(nombre="Torre")
<QuerySet []>
>>> 

>>> Inmuebles.objects.exclude(nombre="App móvil")
<QuerySet [<Inmuebles: Torre de King Kong>, <Inmuebles: Real departament>, <Inmuebles: Portal de clientes>, <Inmuebles: Nombre del inmueble>, <Inmuebles: Empire state>, <Inmuebles: Burf Khalifa>]>
>>> 

>>>Inmuebles.objects.filter(nombre="Inexistente")
<QuerySet []>
>>>

>>> Inmuebles.objects.filter(nombre__contains="ong")
<QuerySet [<Inmuebles: Torre de King Kong>]>
>>> 

>>> Inmuebles.objects.filter(nombre__icontains="kong")
<QuerySet [<Inmuebles: Torre de King Kong>]>
>>> 

>>> Inmuebles.objects.filter(nombre__startswith="a")
<QuerySet []>
>>> 

>>> Inmuebles.objects.filter(created_at__gte=date(2026, 1, 1))
/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1653: RuntimeWarning: DateTimeField Inmuebles.created_at received a naive datetime (2026-01-01 00:00:00) while time zone support is active.
  warnings.warn(
<QuerySet [<Inmuebles: Torre de King Kong>, <Inmuebles: Real departament>, <Inmuebles: Portal de clientes>, <Inmuebles: Nombre del inmueble>, <Inmuebles: Empire state>, <Inmuebles: Burf Khalifa>]>
>>> 

>>> Inmuebles.objects.filter(created_at__lte=date(2026, 10, 27))
/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1653: RuntimeWarning: DateTimeField Inmuebles.created_at received a naive datetime (2026-10-27 00:00:00) while time zone support is active.
  warnings.warn(
<QuerySet []>
>>> 

>>> Inmuebles.objects.filter(created_at__gt=date(2026, 1, 1))
/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1653: RuntimeWarning: DateTimeField Inmuebles.created_at received a naive datetime (2026-01-01 00:00:00) while time zone support is active.
  warnings.warn(
<QuerySet [<Inmuebles: Torre de King Kong>, <Inmuebles: Real departament>, <Inmuebles: Portal de clientes>, <Inmuebles: Nombre del inmueble>, <Inmuebles: Empire state>, <Inmuebles: Burf Khalifa>]>
>>> 

>>> Inmuebles.objects.filter(created_at__lt=date(2026, 1, 1))
/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1653: RuntimeWarning: DateTimeField Inmuebles.created_at received a naive datetime (2026-01-01 00:00:00) while time zone support is active.
  warnings.warn(
<QuerySet []>
>>> 

>>> Inmuebles.objects.filter(ubicacion__isnull=True)
<QuerySet []>
>>> 

>>> Inmuebles.objects.filter(nombre__in=["Torre de King Kong", "Real departament"])
<QuerySet [<Inmuebles: Torre de King Kong>, <Inmuebles: Real departament>]>
>>> 

>>> Inmuebles.objects.filter(nombre__icontains="a", created_at__gte=date(2026, 1, 1))
/home/dany/Documents/programacion_ii_melo_daniela/Django/taskflow-api/venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1653: RuntimeWarning: DateTimeField Inmuebles.created_at received a naive datetime (2026-01-01 00:00:00) while time zone support is active.
  warnings.warn(
<QuerySet [<Inmuebles: Real departament>, <Inmuebles: Portal de clientes>, <Inmuebles: Empire state>, <Inmuebles: Burf Khalifa>]>
>>> 

>>> Inmuebles.objects.order_by("ubicacion")
<QuerySet [<Inmuebles: Portal de clientes>, <Inmuebles: Nombre del inmueble>, <Inmuebles: Burf Khalifa>, <Inmuebles: Empire state>, <Inmuebles: Torre de King Kong>, <Inmuebles: Real departament>]>
>>> 

>>> Inmuebles.objects.order_by("-created_at")
<QuerySet [<Inmuebles: Burf Khalifa>, <Inmuebles: Empire state>, <Inmuebles: Nombre del inmueble>, <Inmuebles: Portal de clientes>, <Inmuebles: Real departament>, <Inmuebles: Torre de King Kong>]>
>>> 

>>> Inmuebles.objects.order_by("nombre", "-created_at")
<QuerySet [<Inmuebles: Burf Khalifa>, <Inmuebles: Empire state>, <Inmuebles: Nombre del inmueble>, <Inmuebles: Portal de clientes>, <Inmuebles: Real departament>, <Inmuebles: Torre de King Kong>]>
>>> 

>>> Inmuebles.objects.count()
6
>>> 

>>> Inmuebles.objects.filter(nombre__icontains="e").count()
5
>>> 

>>> Inmuebles.objects.filter(nombre="No existe").exists()
False
>>> 

>>> Inmuebles.objects.exists()
True
>>> 

>>> queryset = Inmuebles.objects.filter(nombre__icontains="a")
>>> queryset = queryset.exclude(nombre="Torre de King Kong")
>>> queryset = queryset.order_by("-created_at")
>>> print(queryset.query)
SELECT "tasks_inmuebles"."id", "tasks_inmuebles"."nombre", "tasks_inmuebles"."tipo_inmueble", "tasks_inmuebles"."ubicacion", "tasks_inmuebles"."created_at" FROM "tasks_inmuebles" WHERE (UPPER("tasks_inmuebles"."nombre"::text) LIKE UPPER(%a%) AND NOT ("tasks_inmuebles"."nombre" = Torre de King Kong)) ORDER BY "tasks_inmuebles"."created_at" DESC
>>> 
https://francisco-higuera.site/tutorials/django-framework-desde-cero