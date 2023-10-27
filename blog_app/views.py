from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog


def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = BlogForm()
    return render(request, 'create.html', {'form':form})
def retrieve_blog(request):
    blogs = Blog.objects.all()
    return render(request,'index.html',{'blogs':blogs} )
def update_blog(request,pk):
    blogs = Blog.objects.get(id=pk)
    form = BlogForm(instance=blogs)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'blogs': blogs,
        'form': form,
    }
    return render(request,'edit.html',context)
def delete_blog(request, pk):
    blogs = Blog.objects.get(id=pk)

    if request.method == 'POST':
        blogs.delete()
        return redirect('/')

    context = {
        'blogs': blogs,
    }
    return render(request, 'delete.html', context)