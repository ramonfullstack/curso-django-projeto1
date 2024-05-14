from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.core.paginator import Paginator
from utils.pagination import make_pagination, make_pagination_range
from django.contrib import messages
import os

PER_PAGE = int(os.environ.get('PER_PAGE', 6))
print(PER_PAGE, type(PER_PAGE))

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('id')
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    
    messages.error(request, 'Que legal foi um erro')
    messages.success(request, 'Epa, você foi pesquisar algo que eu vi.')
    messages.info(request, 'Epa, você foi pesquisar algo que eu vi.')
    
    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range
    })
    
    
def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'title': f'{recipes[0].category.name} - Category | ',
        'pagination_range': pagination_range,
    }, status=200)
    
    
def recipe(request, id):
    
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)
    
    return render(request, 'recipes/pages/category.html', context={
            'recipe': recipe,
            'is_detail_page': True,
        },
    status=200)

def search(request):
    messages.success(request, 'EPA VOCÊ VEIO PESQUISAR ALGO...')
    
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': recipes,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })