from django.shortcuts import render,redirect
from .models import Woodland
from .forms import WoodForm
# Create your views here.


def woods_view(request):
    if request.method == 'POST':
        form = WoodForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WoodForm()
    woodland = Woodland.objects.all()
    context = {
        'form': form,
        'woodland':woodland}
    return render(request, './frontend/pages/woodland.html', context)
