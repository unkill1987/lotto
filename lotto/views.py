from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

from lotto.form import PostForm
from lotto.models import GuessNumbers, Location


def post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'lotto/form.html', {'form': form})
    else:
        form = PostForm(request.POST)
    if form.is_valid():
        lotto = form.save(commit=False)
        lotto.generate()
        return redirect('/lotto')


def index(request):

    lottos = GuessNumbers.objects.all()
    location = Location.objects.get(id=1)
    return render(request,
                  'lotto/index.html',
                  {'lottos': lottos,'location':location}
                  )


def detail(request, lotto_key):
    lotto = GuessNumbers.objects.get(pk=lotto_key)
    return render(request,
                  'lotto/detail.html',
                  {'lotto': lotto}
                  )
