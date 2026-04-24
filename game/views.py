from django.shortcuts import render, get_object_or_404, redirect
from .models import Panel


def start_view(request):
    """Перенаправляет на стартовую панель или показывает список."""
    start = Panel.objects.filter(is_start=True).first()
    if start:
        return redirect("game:panel_detail", panel_number=start.number)
    panels = Panel.objects.all()
    return render(request, "game/start.html", {"panels": panels})


def panel_detail(request, panel_number):
    """Отображает текущую панель с кнопками выбора."""
    panel = get_object_or_404(Panel, number=panel_number)

    # Игровое состояние в сессии (ОЗ, инвентарь) — заложено для будущего
    if "hp" not in request.session:
        request.session["hp"] = 70
        request.session["inventory"] = []

    choices = panel.choices.select_related("to_panel").all()

    return render(
        request,
        "game/panel.html",
        {
            "panel": panel,
            "choices": choices,
            "hp": request.session["hp"],
            "inventory": request.session.get("inventory", []),
        },
    )