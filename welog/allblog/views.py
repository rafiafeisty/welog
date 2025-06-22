import urllib

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blogs,Comments
from signup.models import Signup

# Create your views here.

def index(request):
    carry=request.session.get('message')
    if carry==True:
        all_blogs=Blogs.objects.all()
        paramas={'all_blogs':all_blogs}
        return render(request, 'allblog/index.html', paramas)
    else:
        return render(request, 'index.html')
def myblog(request):
    carry = request.session.get('message')
    if carry==True:
        username=request.session.get('username')
        user=Signup.objects.get(username=username)
        user_blog=Blogs.objects.filter(user=user)
        paramas={'all_blog':user_blog}
        return render(request, 'allblog/myblog.html',paramas)
    else:
        return render(request, 'index.html')
def madeblog(request):
    carry = request.session.get('message')
    if carry==True:
        return render(request, 'allblog/madeblog.html')
    else:
        return render(request, 'index.html')
def details(request, blog_id):
    carry = request.session.get('message')
    if carry==True:
        blog = Blogs.objects.get(blog_id=blog_id)
        comments = Comments.objects.filter(blog=blog)
        title = request.GET.get('title')
        content = request.GET.get('content')
        image = request.GET.get('image')

        dectitle = urllib.parse.unquote(title)
        deccontent = urllib.parse.unquote(content)
        decimage = urllib.parse.unquote(image)

        params = {"title": dectitle, "content": deccontent, "image": decimage, "comments": comments,"blog_id": blog_id,"blog_user":blog}
        return render(request, 'allblog/details.html', params)
    else:
        return render(request, 'index.html')




def forminput(request):
    carry = request.session.get('message')
    if carry==True:
        content=request.POST.get('content')
        title=request.POST.get('title')
        pic=request.FILES.get('picture')
        username=request.session.get('username')
        user=Signup.objects.get(username=username)
        myblog=Blogs(user=user,content=content,Titleblog=title,image=pic)
        myblog.save()
        return redirect('/allblog/')
    else:
        return render(request, 'index.html')


def commentsaving(request):
    carry = request.session.get('message')
    if carry == True:
        comment = request.POST.get('comment')
        username = request.session.get('username')
        blog_id = request.POST.get('blog_id')

        try:
            blog = Blogs.objects.get(blog_id=blog_id)
            user = Signup.objects.get(username=username)

            # Save the new comment
            new_comment = Comments(content=comment, user=user, blog=blog)
            new_comment.save()

            # Update comment count
            blog.comment += 1
            blog.save()

            # Get the correct image URL
            image_url = blog.image.url if blog.image else ''

            return redirect(
                f'/allblog/details/{blog_id}/?title={urllib.parse.quote(blog.Titleblog)}'
                f'&content={urllib.parse.quote(blog.content)}'
                f'&image={urllib.parse.quote(image_url)}'
            )

        except (Blogs.DoesNotExist, Signup.DoesNotExist):
            return redirect('/allblog/')
    else:
        return render(request, 'index.html')
def edit(request,blog_id_to_edit):
    content = request.GET.get('content')
    title = request.GET.get('title')
    pic = request.GET.get('image')
    decimage = urllib.parse.unquote(pic)
    params={"content":content,"title":title,"pic":decimage,"id":blog_id_to_edit}
    print(params)
    return render(request, 'allblog/edit.html',params)


def formedit(request,blog_id_to_edit):
    carry = request.session.get('message')
    if carry == True:
        try:
            # 1. Get the existing blog
            blog = Blogs.objects.get(blog_id=blog_id_to_edit)

            # 2. Update fields
            blog.content = request.POST.get('content')
            blog.Titleblog = request.POST.get('title')

            # Only update image if a new one was provided
            if 'picture' in request.FILES:
                blog.image = request.FILES.get('picture')

            # 3. Save changes
            blog.save()

            return redirect('/allblog/')

        except Blogs.DoesNotExist:
            # Handle case where blog doesn't exist
            return redirect('/allblog/')

    else:
        return render(request, 'index.html')

def delete(request,blog_id_to_edit):
    carry = request.session.get('message')
    if carry==True:
        try:
            blog = Blogs.objects.get(blog_id=blog_id_to_edit)
            blog.delete()
            return redirect('/allblog/')
        except Blogs.DoesNotExist:
            return redirect('/allblog/')
    else:
        return render(request, 'index.html')