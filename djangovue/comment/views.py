from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm, ContactForm

# Create your views here.
def index(request):
    comments = Comment.objects.all()
    return render(request,'comment/index.html', {
        'comments':comments
    })


def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexcomment')
    else:
        form = CommentForm()

    return render(request,'comment/add.html', {
        'form':form
    })

def update(request, pk):

    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        print(form.errors.as_json())
        if form.is_valid():
            form.save(commit=False)
            return redirect('updatecomment',pk=comment.id)
    else:
        form = CommentForm(instance=comment)

    return render(request,'comment/update.html', {
        'form':form,
        'comment':comment
    })


def contact(request):
    form = ContactForm()
    return render(request,'comment/contact.html', {
        'form':form
    })