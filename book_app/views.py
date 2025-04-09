from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib import messages
from .models import Book
from .forms import BookForm, CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to your personal library.')
            return redirect('book_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'book_app/book_list.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            messages.success(request, f'Book "{book.title}" added successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_app/book_form.html', {'form': form, 'title': 'Add Book'})

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'Book "{book.title}" updated successfully!')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_app/book_form.html', {'form': form, 'title': 'Edit Book'})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        book.delete()
        messages.success(request, f'Book "{book.title}" deleted successfully!')
        return redirect('book_list')
    return render(request, 'book_app/book_confirm_delete.html', {'book': book})

@login_required
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(user=request.user)
    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)
    books_data = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'status': book.get_status_display(),
    } for book in books]
    return JsonResponse({'books': books_data})
