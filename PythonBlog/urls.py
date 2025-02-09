from django.contrib import admin
from django.urls import path
from python_blog.views import catalog_posts, post_detail, catalog_categories, category_detail, catalog_tags, tag_detail

app_name = "blog"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", catalog_posts, name="posts"),
    # категории
    path("categories/", catalog_categories, name="categories"),
    path("categories/<slug:category_slag>/", category_detail, name="category_detail"),
    # теги
    path("tags/", catalog_tags, name="tags"),
    path("tags/<slug:tag_slag>/", tag_detail, name="tag_detail"),
    # посты
    path("<slug:post_slug>/", post_detail, name="post_detail"),
]
