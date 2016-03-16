from pyramid.view import view_config
from datetime import datetime as dt
import forecastio
import json
import os

# Seattle
lat = 47.6235410
lon = -122.3362230

# So. Cali
# lat = 32.8795872
# lon = -116.6748047

# Mt. Rainier
# lat = 47.1489940
# lon = -121.6316550

# Alaska
# lat = 64.2008410
# lon = -149.4936730

API_KEY = os.environ.get('API_KEY', None)


@view_config(route_name='home', renderer='templates/index.jinja2')
def api_test(request):
    current_time = dt.now()
    forecast = forecastio.load_forecast(
        API_KEY,
        lat,
        lon,
        time=current_time
    )
    hourly = forecast.hourly().data
    import pdb; pdb.set_trace()

    return {'hourly': hourly, 'time': current_time}


@view_config(route_name='forecast', renderer='json')
def api_v1(request):
    current_time = dt.now()
    api = json.loads(request.body)
    lat = api['lat']
    lon = api['lon']

    forecast = forecastio.load_forecast(
        API_KEY,
        lat,
        lon,
        time=current_time
    )
    hourly = forecast.hourly().data

    return {'hours': hourly}
