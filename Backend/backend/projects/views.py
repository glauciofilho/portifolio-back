from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Project, ProjectAccess
from .utils import get_client_ip, get_user_agent


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # 🔴 REGISTRA O ACESSO AQUI
    ProjectAccess.objects.create(
        project=project,
        ip_address=get_client_ip(request),
        user_agent=get_user_agent(request),
        country=""  # depois você pode preencher via API externa
    )

    # Idioma
    lang = request.GET.get('lang', 'pt')

    data = {
        "id": project.id,
        "name": project.name_pt if lang == 'pt' else project.name_en,
        "summary": project.summary_pt if lang == 'pt' else project.summary_en,
        "stack": project.stack,
        "created_at": project.created_at,
    }

    return JsonResponse(data)