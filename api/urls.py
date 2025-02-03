from django.urls import path

from api import views

urlpatterns = [
    path('municipalities', views.MunicipalityList.as_view()),
    path('weather_forecast_settings/<str:user_id>', views.WeatherForecastSettingDetail.as_view()),
    path('farm-field/<str:user_id>', views.FarmFieldList.as_view()),
]