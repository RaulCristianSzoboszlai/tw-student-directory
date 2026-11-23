from django.http import Http404, JsonResponse
from django.views.decorators.http import require_GET

STUDENTS = [
    {"id": 1, "name": "Ana Popescu", "year": 3},
    {"id": 2, "name": "Radu Ionescu", "year": 3},
]


# TODO 1 (E2.c): lista accepta doar GET, altfel Django returneaza 405
@require_GET
def student_list(request):
    return JsonResponse({"items": STUDENTS})


# TODO 2 (E2.a): cautam studentul dupa id in lista STUDENTS
def student_detail(request, student_id):
    student = next(
        (s for s in STUDENTS if s["id"] == student_id),
        None,
    )
    if student is None:
        raise Http404("Student not found")
    return JsonResponse(student)


# TODO 3 (E2.b): verificarea starii serviciului
def health(request):
    return JsonResponse({"status": "ok"})
