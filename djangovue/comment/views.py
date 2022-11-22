from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Comment,Contact
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
            return redirect('comment:index')
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
            return redirect('comment:update',pk=comment.id)
    else:
        form = CommentForm(instance=comment)

    return render(request,'comment/update.html', {
        'form':form,
        'comment':comment
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            print('Nombre: '+form.cleaned_data['name'])
            contact = Contact()
            contact.name = form.cleaned_data['name']
            contact.surname = form.cleaned_data['surname']
            contact.phone = form.cleaned_data['phone']
            contact.email = form.cleaned_data['email']
            contact.date_birth = form.cleaned_data['date_birth']
            contact.sex = form.cleaned_data['sex']
            contact.type_contact = form.cleaned_data['type_contact']
            if 'document' in request.FILES:
                contact.document = request.FILES['document']
            contact.save()

            messages.add_message(request, messages.INFO, 'Contacto recibido')
            return redirect('comment:index')
            #form.save()
            #return redirect('indexcomment')
    else:
        form = ContactForm()
    return render(request,'comment/contact.html', {
        'form':form
    })
    