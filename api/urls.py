from django.urls import path

from api import views

urlpatterns = [
    path('municipalities', views.MunicipalityList.as_view()),
    path('weather_forecast_settings/<str:user_id>', views.WeatherForecastSettingDetail.as_view()),
    path('delivery_email_address/<str:user_id>', views.DeliveryEmailAddressDetail.as_view()),
    path('send_test_mail/<str:user_id>', views.SendTestMail.as_view()),
    path('farm_fields/<str:user_id>', views.FarmFieldList.as_view()),
]
