from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicule, Marque, Contact
from django.contrib import messages


def liste_vehicules(request):
    voitures = Vehicule.objects.filter(est_disponible=True)
    marques = Marque.objects.all()

    # Filtres
    marque_id = request.GET.get('marque')
    prix_min = request.GET.get('prix_min')
    prix_max = request.GET.get('prix_max')

    if marque_id:
        voitures = voitures.filter(marque_id=marque_id)
    if prix_min:
        voitures = voitures.filter(prix__gte=prix_min)
    if prix_max:
        voitures = voitures.filter(prix__lte=prix_max)

    return render(request, 'car_shop/catalogue.html', {
        'voitures': voitures,
        'marques': marques
    })


def detail_vehicule(request, id):
    voiture = get_object_or_404(Vehicule, id=id)

    if request.method == "POST":
        Contact.objects.create(
            vehicule=voiture,
            nom=request.POST.get('nom'),
            email=request.POST.get('email'),
            telephone=request.POST.get('telephone'),
            message=request.POST.get('message')
        )
        messages.success(request, "Merci ! Votre message a été envoyé.")
        return redirect('detail_vehicule', id=id)

    return render(request, 'car_shop/detail.html', {'voiture': voiture})