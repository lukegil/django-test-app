from django.conf.urls import patterns, url
from testproject2 import views


urlpatterns = patterns('',
    url(r'submit-answer/$',views.submit_results, name='submit_results'),
    url(r'results-page/$',views.results_page, name='results_page'),
    url(r'^$', views.splash_page, name='splash-page'),
    url(r'submit-question/$', views.post_new_question, name='submit_question'),
)
