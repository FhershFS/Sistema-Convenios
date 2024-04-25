from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Convenio, UnidadAcademica, PersonaTramite, ESTADOS_CONVENIO
from .forms import ConvenioForm, UnidadAcademicaForm, PersonaTramiteForm, MostrarDetallesConvenioForm
from django.contrib import messages
from usuarios.decorators import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class Bienvenida(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


def is_valid_queryparam(param):
    return param != '' and param is not None


@allowed_users(allowed_roles=['admin', 'vinculacion'])
def mostrar_diversas_instituciones(request):
    id_clave = request.GET.get('clave_id')
    category = request.GET.get('category')
    category_persona = request.GET.get('category_persona')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    date_min_salida = request.GET.get('date_min_salida')
    date_max_salida = request.GET.get('date_max_salida')
    date_min_inicio = request.GET.get('date_min_inicio')
    date_max_inicio = request.GET.get('date_max_inicio')
    date_min_termino = request.GET.get('date_min_termino')
    date_max_termino = request.GET.get('date_max_termino')
    estatus = request.GET.get('status')

    # Primera lista
    conv_diversas_instituciones = Convenio.objects.filter(
        tipo="Diversas Instituciones").values()

    unidades_academicas = UnidadAcademica.objects.all()

    personas = PersonaTramite.objects.all()

    if is_valid_queryparam(id_clave):  # pragma: no cover
        conv_diversas_instituciones = conv_diversas_instituciones.filter(
            id=id_clave)

    if is_valid_queryparam(category) and category != 'Choose...':  # pragma: no cover
        conv_diversas_instituciones = conv_diversas_instituciones.filter(
            unidad_academica=category)

    if is_valid_queryparam(category_persona) and category_persona != 'Choose...':  # pragma: no cover
        conv_diversas_instituciones = conv_diversas_instituciones.filter(
            persona_tramito=category_persona)

    if is_valid_queryparam(estatus) and estatus in [estado[0] for estado in ESTADOS_CONVENIO]:  # pragma: no cover
        conv_diversas_instituciones = conv_diversas_instituciones.filter(
            estado=estatus)

    date_filters = {
        'fecha_ingreso__gte': date_min,
        'fecha_ingreso__lte': date_max,
        'fecha_salida__gte': date_min_salida,
        'fecha_salida__lte': date_max_salida,
        'fecha_inicio__gte': date_min_inicio,
        'fecha_inicio__lte': date_max_inicio,
        'fecha_termino__gte': date_min_termino,
        'fecha_termino__lte': date_max_termino,
    }

    for filter_key, filter_value in date_filters.items():
        if is_valid_queryparam(filter_value):
            conv_diversas_instituciones = conv_diversas_instituciones.filter(
                **{filter_key: filter_value})

    return render(request, "divinsts.html",
                  {
                      'ESTADOS_CONVENIO': ESTADOS_CONVENIO,
                      "convenios": conv_diversas_instituciones,
                      'personas': personas,
                      'unidades_academicas': unidades_academicas,
                  })


@allowed_users(allowed_roles=['admin', 'movilidad'])
def mostar_internacionales(request):
    id_clave = request.GET.get('clave_id')
    category = request.GET.get('category')
    category_persona = request.GET.get('category_persona')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    date_min_salida = request.GET.get('date_min_salida')
    date_max_salida = request.GET.get('date_max_salida')
    date_min_inicio = request.GET.get('date_min_inicio')
    date_max_inicio = request.GET.get('date_max_inicio')
    date_min_termino = request.GET.get('date_min_termino')
    date_max_termino = request.GET.get('date_max_termino')
    estatus = request.GET.get('status')

    # Segunda lista
    conv_internacionales = Convenio.objects.filter(
        tipo="Internacionales").values()

    unidades_academicas = UnidadAcademica.objects.all()

    personas = PersonaTramite.objects.all()
    """
    paginator = Paginator(conv_internacionales, 15)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    """

    if is_valid_queryparam(id_clave):  # pragma: no cover
        conv_internacionales = conv_internacionales.filter(id=id_clave)

    if is_valid_queryparam(category) and category != 'Choose...':  # pragma: no cover
        conv_internacionales = conv_internacionales.filter(
            unidad_academica=category)

    if is_valid_queryparam(category_persona) and category_persona != 'Choose...':  # pragma: no cover
        conv_internacionales = conv_internacionales.filter(
            persona_tramito=category_persona)

    if is_valid_queryparam(estatus) and estatus in [estado[0] for estado in ESTADOS_CONVENIO]:  # pragma: no cover
        conv_internacionales = conv_internacionales.filter(estado=estatus)

    date_filters = {
        'fecha_ingreso__gte': date_min,
        'fecha_ingreso__lte': date_max,
        'fecha_salida__gte': date_min_salida,
        'fecha_salida__lte': date_max_salida,
        'fecha_inicio__gte': date_min_inicio,
        'fecha_inicio__lte': date_max_inicio,
        'fecha_termino__gte': date_min_termino,
        'fecha_termino__lte': date_max_termino,
    }

    for filter_key, filter_value in date_filters.items():
        if is_valid_queryparam(filter_value):  # pragma: no cover
            conv_internacionales = conv_internacionales.filter(
                **{filter_key: filter_value})

    return render(request, "internacionales.html",
                  {'ESTADOS_CONVENIO': ESTADOS_CONVENIO, "convenios": conv_internacionales, 'personas': personas, 'unidades_academicas': unidades_academicas})


@allowed_users(allowed_roles=['admin', 'movilidad'])
def mostrar_nacionales(request):
    id_clave = request.GET.get('clave_id')
    category = request.GET.get('category')
    category_persona = request.GET.get('category_persona')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    date_min_salida = request.GET.get('date_min_salida')
    date_max_salida = request.GET.get('date_max_salida')
    date_min_inicio = request.GET.get('date_min_inicio')
    date_max_inicio = request.GET.get('date_max_inicio')
    date_min_termino = request.GET.get('date_min_termino')
    date_max_termino = request.GET.get('date_max_termino')
    estatus = request.GET.get('status')

    # Tercera lista
    conv_nacionales = Convenio.objects.filter(tipo="Nacionales").values()

    unidades_academicas = UnidadAcademica.objects.all()

    personas = PersonaTramite.objects.all()

    if is_valid_queryparam(id_clave):  # pragma: no cover
        conv_nacionales = conv_nacionales.filter(id=id_clave)

    if is_valid_queryparam(category) and category != 'Choose...':  # pragma: no cover
        conv_nacionales = conv_nacionales.filter(
            unidad_academica=category)

    if is_valid_queryparam(category_persona) and category_persona != 'Choose...':  # pragma: no cover
        conv_nacionales = conv_nacionales.filter(
            persona_tramito=category_persona)

    if is_valid_queryparam(estatus) and estatus in [estado[0] for estado in ESTADOS_CONVENIO]:  # pragma: no cover
        conv_nacionales = conv_nacionales.filter(estado=estatus)

    date_filters = {
        'fecha_ingreso__gte': date_min,
        'fecha_ingreso__lte': date_max,
        'fecha_salida__gte': date_min_salida,
        'fecha_salida__lte': date_max_salida,
        'fecha_inicio__gte': date_min_inicio,
        'fecha_inicio__lte': date_max_inicio,
        'fecha_termino__gte': date_min_termino,
        'fecha_termino__lte': date_max_termino,
    }

    for filter_key, filter_value in date_filters.items():
        if is_valid_queryparam(filter_value):
            conv_nacionales = conv_nacionales.filter(
                **{filter_key: filter_value})

    return render(request, "nacionales.html",
                  {'ESTADOS_CONVENIO': ESTADOS_CONVENIO, "convenios": conv_nacionales, 'personas': personas, 'unidades_academicas': unidades_academicas})


@allowed_users(allowed_roles=['admin'])
def mostar_varios(request):
    id_clave = request.GET.get('clave_id')
    category = request.GET.get('category')
    category_persona = request.GET.get('category_persona')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    date_min_salida = request.GET.get('date_min_salida')
    date_max_salida = request.GET.get('date_max_salida')
    date_min_inicio = request.GET.get('date_min_inicio')
    date_max_inicio = request.GET.get('date_max_inicio')
    date_min_termino = request.GET.get('date_min_termino')
    date_max_termino = request.GET.get('date_max_termino')
    estatus = request.GET.get('status')

    # Cuarta lista
    conv_varios = Convenio.objects.filter(tipo="Varios").values()

    unidades_academicas = UnidadAcademica.objects.all()

    personas = PersonaTramite.objects.all()

    if is_valid_queryparam(id_clave):  # pragma: no cover
        conv_varios = conv_varios.filter(id=id_clave)

    if is_valid_queryparam(category) and category != 'Choose...':  # pragma: no cover
        conv_varios = conv_varios.filter(
            unidad_academica=category)

    if is_valid_queryparam(category_persona) and category_persona != 'Choose...':  # pragma: no cover
        conv_varios = conv_varios.filter(
            persona_tramito=category_persona)

    if is_valid_queryparam(estatus) and estatus in [estado[0] for estado in ESTADOS_CONVENIO]:  # pragma: no cover
        conv_varios = conv_varios.filter(estado=estatus)

    date_filters = {
        'fecha_ingreso__gte': date_min,
        'fecha_ingreso__lte': date_max,
        'fecha_salida__gte': date_min_salida,
        'fecha_salida__lte': date_max_salida,
        'fecha_inicio__gte': date_min_inicio,
        'fecha_inicio__lte': date_max_inicio,
        'fecha_termino__gte': date_min_termino,
        'fecha_termino__lte': date_max_termino,
    }

    for filter_key, filter_value in date_filters.items():
        if is_valid_queryparam(filter_value):  # pragma: no cover
            conv_varios = conv_varios.filter(
                **{filter_key: filter_value})

    return render(request, "varios.html",
                  {'ESTADOS_CONVENIO': ESTADOS_CONVENIO, "convenios": conv_varios, 'personas': personas, 'unidades_academicas': unidades_academicas})


@login_required
@allowed_users(allowed_roles=['admin'])
def mostar_pendientes(request):
    id_clave = request.GET.get('clave_id')
    category = request.GET.get('category')
    category_persona = request.GET.get('category_persona')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    date_min_salida = request.GET.get('date_min_salida')
    date_max_salida = request.GET.get('date_max_salida')
    date_min_inicio = request.GET.get('date_min_inicio')
    date_max_inicio = request.GET.get('date_max_inicio')
    date_min_termino = request.GET.get('date_min_termino')
    date_max_termino = request.GET.get('date_max_termino')
    estatus = request.GET.get('status')

    # quinta lista
    conv_pendientes = Convenio.objects.filter(
        estado__in=["ESPERA", "NO EMPEZADO"])

    unidades_academicas = UnidadAcademica.objects.all()

    personas = PersonaTramite.objects.all()

    if is_valid_queryparam(id_clave):  # pragma: no cover
        conv_pendientes = conv_pendientes.filter(id=id_clave)

    if is_valid_queryparam(category) and category != 'Choose...':  # pragma: no cover
        conv_pendientes = conv_pendientes.filter(
            unidad_academica=category)

    if is_valid_queryparam(category_persona) and category_persona != 'Choose...':  # pragma: no cover
        conv_pendientes = conv_pendientes.filter(
            persona_tramito=category_persona)

    if is_valid_queryparam(estatus) and estatus in [estado[0] for estado in ESTADOS_CONVENIO]:  # pragma: no cover
        conv_pendientes = conv_pendientes.filter(estado=estatus)

    date_filters = {
        'fecha_ingreso__gte': date_min,
        'fecha_ingreso__lte': date_max,
        'fecha_salida__gte': date_min_salida,
        'fecha_salida__lte': date_max_salida,
        'fecha_inicio__gte': date_min_inicio,
        'fecha_inicio__lte': date_max_inicio,
        'fecha_termino__gte': date_min_termino,
        'fecha_termino__lte': date_max_termino,
    }

    for filter_key, filter_value in date_filters.items():
        if is_valid_queryparam(filter_value):  # pragma: no cover
            conv_pendientes = conv_pendientes.filter(
                **{filter_key: filter_value})

    return render(request, "pendientes.html",
                  {
                      'ESTADOS_CONVENIO': ESTADOS_CONVENIO,
                      "convenios": conv_pendientes,
                      'personas': personas,
                      'unidades_academicas': unidades_academicas,

                  })


@login_required
@allowed_users(allowed_roles=['admin'])
def agregar_convenio(request):
    form = ConvenioForm()

    if request.method == 'POST':
        form = ConvenioForm(request.POST)

        clave = request.POST["numero"]
        tipo = request.POST["tipo"]
        persona_tramito = request.POST["persona_tramito"]
        unidad_academica = request.POST["unidad_academica"]

        if Convenio.objects.filter(numero=clave).exists():
            messages.error(request, "La clave ya existe")
            return redirect('agregar_convenio')

        if not clave or not tipo or not persona_tramito or not unidad_academica:
            messages.error(request, "Llenar campos obligatorios")
            return redirect('agregar_convenio')
        if form.is_valid:
            form.save()
            messages.success(request, "Convenio agregado")
            return redirect('bienvenida')
        else:
            messages.error(request, "Campos invalidos")
            return redirect('agregar_convenio')
    return render(request, "agregar_convenio.html", {"form": form})


@login_required
@allowed_users(allowed_roles=['admin'])
def borrar_convenio(request, convenio_id):
    convenio = get_object_or_404(Convenio, id=convenio_id)

    if request.method == 'POST':
        convenio.delete()
        messages.success(request, "Convenio eliminado")
        return redirect('bienvenida')
    return render(request, 'borrar_convenio.html', {'convenio': convenio})


@login_required
@allowed_users(allowed_roles=['admin'])
def editar_convenio(request, convenio_id):
    convenio = get_object_or_404(Convenio, id=convenio_id)

    if request.method == 'POST':

        clave = request.POST["numero"]
        tipo = request.POST["tipo"]
        persona_tramito = request.POST["persona_tramito"]
        unidad_academica = request.POST["unidad_academica"]

        if (Convenio.objects.filter(numero=clave).exists()
                and Convenio.objects.get(numero=clave).id != convenio_id):
            messages.error(request, "La clave ya existe")
            return redirect('editar_convenio', convenio_id=convenio_id)

        if not clave or not tipo or not persona_tramito or not unidad_academica:
            messages.error(request, "Llenar campos obligatorios")
            return redirect('editar_convenio', convenio_id=convenio_id)

        form = ConvenioForm(request.POST, instance=convenio)

        if form.is_valid():
            form.save()
            messages.success(request, "Convenio editado")
            return redirect('bienvenida')
        else:
            messages.error(request, "Campos invalidos")
            return redirect('editar_convenio', convenio_id=convenio_id)
    else:
        form = ConvenioForm(instance=convenio)
    return render(request, 'editar_convenio.html', {'form': form, 'convenio': convenio})


@login_required
@allowed_users(allowed_roles=['admin'])
def agregar_unidad_academica(request):
    form = UnidadAcademicaForm()

    if request.method == 'POST':
        form = UnidadAcademicaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('bienvenida')
    return render(request, "agregar_unidad.html", {"form": form})


@login_required
@allowed_users(allowed_roles=['admin'])
def agregar_persona(request):
    form = PersonaTramiteForm()

    if request.method == 'POST':
        form = PersonaTramiteForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('bienvenida')
    return render(request, "agregar_persona.html", {"form": form})


@login_required
def mostar_detalles_convenio(request, convenio_id):
    convenio = get_object_or_404(Convenio, id=convenio_id)
    form = MostrarDetallesConvenioForm(instance=convenio)

    return render(request, 'mostrar_detalles_convenio.html',
                  {
                      "form": form
                  })
