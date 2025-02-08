from rest_framework.views import APIView
from rest_framework.response import Response
from os import path
from datetime import datetime
import pandas as pd

from api.serializers import SensorsDataListGetSerializer
from api.utils import replace_nan_with_none

class SensorsDataList(APIView):

    def __get_data_from_csv(self, farm_field_id, start, end):
        csv_file = path.join(path.dirname(path.abspath(__file__)), f'{farm_field_id}.csv')
        csv_data = pd.read_csv(csv_file, index_col='timestamp')
        csv_data.index = pd.to_datetime(csv_data.index)
        target_data = csv_data[(start <= csv_data.index) & (csv_data.index <= end)].to_dict(orient='split')
        result = {}
        for i, data_name in enumerate(target_data['columns']):
            result[data_name] = []
            for j, timestamp in enumerate(target_data['index']):
                result[data_name].append({
                    'timestamp': timestamp.to_pydatetime().isoformat(sep='T', timespec='milliseconds'),
                    'value': target_data['data'][j][i]
                })
        return replace_nan_with_none(result)

    def get(self, request, user_id):

        serializer = SensorsDataListGetSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        start = datetime.fromisoformat(request.query_params.get('start'))
        end = datetime.fromisoformat(request.query_params.get('end'))

        farm_field_ids = ['farm-field-a', 'farm-field-b', 'farm-field-c']
        result = {}
        for farm_field_id in farm_field_ids:
            result[farm_field_id] = self.__get_data_from_csv(farm_field_id, start, end)

        return Response(result)
