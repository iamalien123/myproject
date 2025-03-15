import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from shop.models import Category, Product, Cart, CartItem, Order
from django.utils import timezone
from decimal import Decimal
import random

# Create test users
def create_users():
    users = []
    for i in range(5):
        username = f'user{i+1}'
        user, created = User.objects.get_or_create(
            username=username,
            defaults={'email': f'{username}@example.com'}
        )
        if created:
            user.set_password('password123')
            user.save()
        users.append(user)
    return users

# Insert sample data
def populate_db():
    # Create users
    users = create_users()
    
    # Create categories
    categories = [
        Category.objects.create(name=name, slug=slug) for name, slug in [
            ('Electronics', 'electronics'),
            ('Clothing', 'clothing'),
            ('Books', 'books'),
            ('Home & Kitchen', 'home-kitchen'),
            ('Sports', 'sports'),
            ('Beauty', 'beauty'),
            ('Toys', 'toys'),
            ('Jewelry', 'jewelry'),
            ('Garden', 'garden'),
            ('Automotive', 'automotive')
        ]
    ]

    # Create products
    products = [
        Product.objects.create(
            category=categories[0],
            name='Smart Phone',
            slug='smart-phone',
            description='Latest smartphone with amazing features',
            price=Decimal('699.99'),
            image='products/phone.jpg',
            stock=50
        ),
        
        # ... Add more products similarly
    ]

    # Create carts and cart items
    for user in users:
        cart = Cart.objects.create(user=user)
        for _ in range(random.randint(1, 3)):
            CartItem.objects.create(
                cart=cart,
                product=random.choice(products),
                quantity=random.randint(1, 5)
            )

    # Create orders
    statuses = ['Pending', 'Processing', 'Shipped', 'Delivered']
    for user in users:
        for _ in range(2):
            Order.objects.create(
                user=user,
                address=f'{random.randint(1, 999)} Sample St, City, Country',
                phone=f'{random.randint(1000000000, 9999999999)}',
                total_amount=Decimal(random.randint(50, 1000)),
                status=random.choice(statuses)
            )

if __name__ == '__main__':
    populate_db()
    print("Sample data inserted successfully!")

    # Additional code to query all products
    from shop.models import Product
    print(Product.objects.all())