from django.shortcuts import render, redirect
from clients.forms import clientForm, addIndustry, addPosition
from clients.models import client, industryChoices, positionChoices
# Create your views here.
def create_client_view(request):
  form = clientForm()
  if request.method == 'POST':
    form = clientForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('results', 'Any', 'Any', 'Any', 0, 'None')
  context = {
    'form': form,
  }
  return render(request, 'clientForm.html', context)

def home_view(request):
  context = {}
  return render(request, 'base.html', context)

def search_view(request):
  cl = client.objects.all()
  if request.method == 'POST':
    ind = request.POST.get('searchIND')
    pos = request.POST.get('searchPOS')
    res = request.POST.get('searchRES')
    exp = request.POST.get('searchEXP')
    return redirect('results', ind, pos, res, exp, 'None')
  context= {
    'clients': cl,
    'industries': industryChoices.objects.all(),
    'positions': positionChoices.objects.all(),
  }
  return render(request, 'searchClients.html', context)

def search_results_view(request, ind, pos, res, exp, sort):
  query = client.objects.all()
  if ind != 'Any':
    query = query.filter(industry__ind=ind)
  if pos != 'Any':
    query = query.filter(position__pos=pos)
  if res != 'Any':
    query = query.filter(residency=res)
  if exp != 0:
    query = query.filter(experience__gte=exp)
  if sort != 'None':
    query = query.order_by(sort, '-experience')
  else:
    query = query.order_by('-experience')
  if request.method == 'POST':
    sort = request.POST.get('sort')
    return redirect('results', ind, pos, res, exp, sort)
  context = {
    'query': query,
    'sorted': sort
  }
  return render(request, 'searchResults.html', context)


def add_options_view(request):
  Iform = addIndustry()
  Pform = addPosition()
  if request.method=='POST':
    newInd = request.POST.get('ind')
    newPos = request.POST.get('pos')
    if newInd is not None:
      industryChoices.objects.create(ind = newInd)
    if newPos is not None:
      positionChoices.objects.create(pos=newPos)
  context = {
    'Iform': Iform,
    'Pform': Pform,
  }
  return render(request, 'addOptions.html', context)

def delete_view(request, id):
  cl = client.objects.get(id=id)
  cl.delete()
  context = {
    'cl': cl
  }
  return render(request, 'deleteClient.html', context)
