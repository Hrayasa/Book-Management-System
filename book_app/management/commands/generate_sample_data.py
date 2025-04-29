from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from book_app.models import Book
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Generates sample data for testing'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of books to create per user')
        parser.add_argument('--users', type=int, default=3, help='Number of users to create')

    def handle(self, *args, **options):
        # Create sample users
        users = []
        for i in range(options['users']):
            username = f'testuser{i+1}'
            email = f'{username}@example.com'
            user = User.objects.create_user(
                username=username,
                email=email,
                password='testpass123'
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {username}'))

        # Sample book data
        books_data = [
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
            {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
            {'title': '1984', 'author': 'George Orwell'},
            {'title': 'Pride and Prejudice', 'author': 'Jane Austen'},
            {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'},
            {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien'},
            {'title': 'Brave New World', 'author': 'Aldous Huxley'},
            {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien'},
            {'title': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky'},
            {'title': 'The Brothers Karamazov', 'author': 'Fyodor Dostoevsky'},
        ]

        # Create sample books for each user
        status_choices = ['TR', 'R', 'RD']
        for user in users:
            for i in range(options['count']):
                book_data = random.choice(books_data)
                publication_date = datetime.now() - timedelta(days=random.randint(0, 3650))
                Book.objects.create(
                    title=book_data['title'],
                    author=book_data['author'],
                    publication_date=publication_date,
                    isbn=f'978{random.randint(100000000, 999999999)}',
                    status=random.choice(status_choices),
                    notes=f'Sample note for {book_data["title"]}',
                    user=user
                )
            self.stdout.write(self.style.SUCCESS(f'Created {options["count"]} books for user: {user.username}'))

        self.stdout.write(self.style.SUCCESS('Sample data generation completed successfully!')) 