from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import  DetailView


class WalletDetailView(DetailView):
    model = Articles
    template_name = 'wallets/details_view.html'
    context_object_name = 'article'

def wallets_home (request):
    wallets = Articles.objects.all()
    return render(request, 'wallets/wallets_home.html', {'wallets': wallets})

def add_new_wallet(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wallets_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'wallets/add_new_wallet.html', data)