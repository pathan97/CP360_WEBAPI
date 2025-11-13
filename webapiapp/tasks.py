from celery import shared_task
from .models import Category, Product

@shared_task
def generate_dummy_category_product_task(cat_count=5,prod_count=5):
    fake = Faker()
    categories = []

    for _ in range(num_categories):
        name = fake.unique.word()
        category, created = Category.objects.get_or_create(name=name)
        categories.append(category)
    
    for _ in range(num_categories * num_products_per_category):
        category = random.choice(categories)
        Product.objects.create(
            category=category,
            name=fake.sentence(nb_words=3),
            description=fake.paragraph(),
            price=random.uniform(10.00, 1000.00),
            status=pending,
        )
    
    return f"Generated {num_categories} categories and {num_categories * num_products_per_category} products."