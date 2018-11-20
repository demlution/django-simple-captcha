
from django.conf.urls import url
import captcha.views
    
urlpatterns = [
    url(r'image/(?P<key>\w+)/$', captcha.views.captcha_image, name='captcha-image', kwargs={'scale': 1}),
    url(r'image/(?P<key>\w+)@2/$', captcha.views.captcha_image, name='captcha-image-2x', kwargs={'scale': 2}),
    url(r'audio/(?P<key>\w+)/$', captcha.views.captcha_audio, name='captcha-audio'),
    url(r'refresh/$', captcha.views.captcha_refresh, name='captcha-refresh'),
]
