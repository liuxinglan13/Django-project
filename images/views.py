from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageCreateForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Image
from django.contrib import messages


@login_required
def image_create(request):
    if request.method == 'POST':
        # request_dic = getattr(request, 'POST')
        form = ImageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
        # assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, '图片上传成功')
        # redirect to new created item detail view

    else:  # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm()

    return render(request, 'images/create.html', {'form': form})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 10)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'images/list_ajax.html',
                      {'section': 'images', 'images': images})
    return render(request,
                  'images/list.html',
                  {'section': 'images', 'images': images})
