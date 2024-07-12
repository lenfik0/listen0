from django.shortcuts import render, redirect
from reviews.forms import Review_form
from reviews.models import Review

def reviews(request):
    if request.method == 'POST':
        form = Review_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            review = data.get('review')
            Review.objects.create(name = name, review = review)
            return redirect('review')
    else:
        form = Review_form()
        all_reviews = Review.objects.all()
        title = 'Отзывы'
        return render(request,'review.html', {'title':title, 'form':form, 'all_reviews':all_reviews})
