from django.forms import ValidationError
from .recipe_test_base import RecipeTestBase
from parameterized import parameterized

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 70
        
        with self.assertRaises(ValidationError):
            self.recipe.full_clean() #aqui a validação ocorre
            
    def test_recipe_fields_max_length(self):
        fields = [
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 165),
            ('servings_unit', 165),
        ]
        
        for field, max_length in fields:
            with self.subTest(field=field, max_length=max_length):
                setattr(self.recipe, field, 'A' * (max_length + 1))
                with self.assertRaises(ValidationError):
                    self.recipe.full_clean() #aqui a validação ocorre
                    
                    
    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
        