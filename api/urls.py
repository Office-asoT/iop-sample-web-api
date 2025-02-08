from django.urls import path

from api import views

urlpatterns = [
    path('municipalities', views.MunicipalityList.as_view()),
    path('weather_forecast_settings/<str:user_id>', views.WeatherForecastSettingDetail.as_view()),
    path('display_settings/<str:user_id>', views.DisplaySettingList.as_view()),
    path('display_settings/<str:user_id>/<str:farm_field_id>', views.DisplaySettingDetail.as_view()),
