from django.urls import path
from .views import IndexView,HomeView,BookDetailView
from django.views.generic.base import TemplateView #シンプルな画面のみ実装する場合使える

app_name = 'store'

urlpatterns = [
     path('index/', IndexView.as_view(), name='index',),
#      path('home/',TemplateView.as_view(template_name='home.html'), name='home'),
     path('home/<name>/', HomeView.as_view(), name='home',),
      path('detail_book/<int:book_id>/', BookDetailView.as_view(), name='detail_book',),
      path('detail_book/<str:slug>/', BookDetailView.as_view(), name='detail_book',),
 ]
