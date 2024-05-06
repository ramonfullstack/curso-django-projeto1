from django.test import TestCase
from recipes.models import Category, Recipe, User

class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        category = self.make_recipe()
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            #title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porcões',
            preparation_steps='Recipe Preparation Steps',
            #preparation_steps_is_html=False,
            is_published=True,
        )
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def make_recipe(self):
        return Category.objects.create(name='Category')
