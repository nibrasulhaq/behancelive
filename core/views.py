from profile import Profile
from django.shortcuts import render,redirect
from . models import Work
from .forms import Workform, Commentform


def home(request):
    works = Work.objects.all()
    context = {'works':works}
    return render(request, 'index.html', context)


def singlework(request, pk):
    work = Work.objects.get(id=pk)
    profile = request.user.profile
    form =Commentform()

    if request.method == 'POST':
        form = Commentform(request.POST)
        comment = form.save(commit=False)
        comment.work = work
        comment.profile = request.user.profile
        comment.save()
        return redirect('singlework', pk=work.id)
    context = {'work':work, 'form':form}
    return render(request, 'singlework.html', context)


def creatework(request):
    profile = request.user.profile
    form = Workform()
    if request.method == "POST":
        form = Workform(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.profile = profile
            work.save()
            return redirect('home')

            
    context = {'form': form}
    return render(request, 'creatework.html', context)

