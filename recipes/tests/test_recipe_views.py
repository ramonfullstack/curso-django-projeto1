from django.urls import reverse, resolve 
from recipes import views
from .recipe_test_base import RecipeTestBase
from unittest import skip
    
#@skip('A mensagem do porque eu estou pulando este teste')
class RecipeViewsTest(RecipeTestBase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
        
    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        print(content)
        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            content
        )
        #self.fail('Para que eu termine de digitá-lo')
        
    def test_recipe_home_template_loads_recipe(self):
        #need a recipe for this test
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        #need a recipe for this test
        self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        
        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            content
        )
    
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)
        
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
        
    def test_recipe_category_template_loads_recipe(self):
        needed_title = 'This is a category test'
        #need a recipe for this test
        self.make_recipe(title=needed_title)
        
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')
        
        self.assertIn(needed_title, content)
        
    def test_recipe_category_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        #need a recipe for this test
        recipe = self.make_recipe(is_published=False)
        
        url = reverse('recipes:recipe', kwargs={'id': recipe.category.id})
        response = self.client.get(
            url
        )
        
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        view = resolve(
            url
        )
        self.assertEqual(url, '/recipes/1/')
        #self.assertIs(view.func, views.recipe)
        
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        url = reverse('recipes:recipe', kwargs={'id': 1000})
        response = self.client.get(
            url
        )
        self.assertEqual(response.status_code, 404)
        
    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a category test - it load one recipe'
        
        #need a recipe for this test
        recipe = self.make_recipe(title=needed_title)
        
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': recipe.category.id
                }
            )
        )
        content = response.content.decode('utf-8')
        
        self.assertIn(needed_title, content)
        
    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        """Test recipe is_published False dont show"""
        #need a recipe for this test
        recipe = self.make_recipe(is_published=False)
        
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': recipe.id
                }
            )
        )
        
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
 