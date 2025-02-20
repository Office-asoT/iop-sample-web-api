from django.urls import path

from api import views

urlpatterns = [
    path('municipalities', views.MunicipalityList.as_view()),
    path('weather_forecast_settings/<str:user_id>', views.WeatherForecastSettingDetail.as_view()),
    path('display_settings/<str:user_id>', views.DisplaySettingList.as_view()),
    path('display_settings/<str:user_id>/<str:farm_field_id>', views.DisplaySettingDetail.as_view()),
    path('sensors_data/<str:user_id>', views.SensorsDataList.as_view()),
    path('sensors_data/<str:user_id>/latest', views.LatestSensorsDataList.as_view()),
    path('delivery_email_address/<str:user_id>', views.DeliveryEmailAddressDetail.as_view()),
    path('send_test_mail/<str:user_id>', views.SendTestMail.as_view()),
    path('farm_fields/<str:user_id>', views.FarmFieldList.as_view()),
    path('ja_branch_offices', views.JaBranchOfficeList.as_view()),
    path('fuel_order_target_jas/<str:user_id>', views.FuelOrderTargetJaDetail.as_view()),
    path('fuel_orders/<str:user_id>', views.FuelOrderList.as_view()),
    path('fuel_order/<str:user_id>', views.FuelOrderDetail.as_view()),
    path('send_fuel_order_mail/<str:user_id>', views.SendFuelOrderMail.as_view()),
    path('send_cancel_fuel_order_mail/<str:user_id>', views.SendCancelFuelOrderMail.as_view()),
    path('warning_mail_settings/<str:user_id>', views.WarningMailSettingList.as_view()),
    path('warning_mail_settings/<str:user_id>/<str:pk>', views.WarningMailSettingDetail.as_view()),
    path('warning_histories/<str:user_id>', views.WarningHistoryList.as_view()),
]
