from django.shortcuts import render, get_object_or_404
from blog.models import Person, Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

# Create your views here.

# def list(request):
#     Data = {'Persons': Person.objects.all().order_by("-date")}
#     return render(request, 'sos/sos.html', Data)

class PostListView(ListView):
    queryset = Person.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Persons'
    paginate_by = 2

# class PostDetailView(DetailView):
#     model = Person
#     template_name = 'sos/person.html'


def person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST,author=request.user,person=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, "blog/person.html", {"person":person, "form":form})