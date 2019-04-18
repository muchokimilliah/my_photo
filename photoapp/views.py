from django .shortcuts import render, get_object_or_404, redirect
from . models import Photo
from . forms import PhotoForm, CommentForm, UserForm
from django . contrib. auth.decorate import login_required

# Create your views here.
def index(request):
    photos=Photo.objects.all()
    return render(request, 'photoapp:index.html',{'photos':photos})

def detail (request, photo_id):
    photo=get_object_or_404(Photo, pk=photo_id)
    return  render(request, 'photoapp/detail.html', {'photo':photo})

def create_photo(request):
    form=PhotoForm(request.POST or None, request .FILES or None)
    if form . is_valid():
        photo=form.save(commit=False)
        photo.user=request.user
        photo.save()
        context={'photo':photo, 'message':'photo_created'}
        return  render(request, 'photoapp/detail.html', context)

    form =PhotoForm()
    return render(request, 'photoapp/create_photo.html', {'form':form})

def comment_photo(request, photo_id):
    form=CommentForm(request.POST or None, request.FILES or None)
    photo=get_object_or_404(Photo, pk=photo_id)
    comment=form.save(commit=False)



