from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
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


def species_delete(request: HttpRequest, pk: int):
    species = get_object_or_404(Woodland, id=pk)

    if request.method == 'POST':
        species.delete()
        return redirect('wood_land:woods')

    return render(request, 'frontend/pages/delete_species.html', {'species': species})

def update_species(request, pk:int):
    species = Woodland.objects.get(id=pk)
    if request.method == 'POST':
        form = WoodForm(request.POST,instance=species)
        if form.is_valid():
            form.save()
            return redirect('wood_land:woods')
    else:
        form = WoodForm(instance=species)
    context={
      'form':form,
    }
    return render(request, 'frontend/pages/update_species.html',context)