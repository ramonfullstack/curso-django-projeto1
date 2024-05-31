from django.urls import reverse, resolve 
from recipes import views
from .recipe_test_base import RecipeTestBase
from unittest import skip
    
class RecipeDetailViewTest(RecipeTestBase):
    def test_recipe_detail_view_function_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'pk': 1})
        view = resolve(
            url
        )
        self.assertEqual(url, '/recipes/1/')
        
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        url = reverse('recipes:recipe', kwargs={'pk': 2500})
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
                    'pk': recipe.category.id
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
                    'pk': recipe.id
                }
            )
        )
        
        self.assertEqual(response.status_code, 404)
    
        
 