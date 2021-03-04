from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Developer, Skill
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'ninja/index.html'
    context_object_name = 'all_devs'

    def get_queryset(self):
        return Developer.objects.all()

#Making Details Generic caused the app to throw a NoReverseMatch Error so i didnt implement a Details view
def details(request, dev_id):
    dev = get_object_or_404(Developer, pk=dev_id)
    return render(request, 'ninja/details.html', {'dev':dev})

def level(request, dev_id):
    dev = get_object_or_404(Developer, pk=dev_id)
    try:
        select = dev.skill_set.get(pk=request.POST['skill'])
    except(KeyError, Skill.DoesNotExist):
        return render(request, 'ninja/details.html',{
            'dev':dev,
            'error_message':"No Skill"
        })
    else:
        select.level += 1
        select.save()
        return HttpResponseRedirect(reverse('ninja:details', args=(dev.id,)))