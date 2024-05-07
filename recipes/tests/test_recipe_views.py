from django.urls import reverse, resolve 
from recipes import views
from .recipe_test_base import RecipeTestBase, Recipe
    
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
        
    def test_recipe_home_template_loads_recipe(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    
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
    
        
 