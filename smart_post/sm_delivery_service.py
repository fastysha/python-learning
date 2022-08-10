import time 
from sm_dbconnector import find_all_not_delivered_parcels, update_parcels
from sm_data_models import ParcelStatus

DELIVERY_TIME_SECONDS = 90

# Этот сервис имитирует работу грузовой машины которая идете и доставляет посылки
# Доставленной считается посылка которая едет уже энное время, см. DELIVERY_TIME_SECONDS
while True:
    print('Ваши посылки в пути...')
    delivered_parcels = find_all_not_delivered_parcels(DELIVERY_TIME_SECONDS)
    if delivered_parcels:
        parcel_ids = [str(p['ParcelID']) for p in delivered_parcels]
        print('Посылки приехали:', parcel_ids)
        update_parcels(ParcelStatus.DELIVERED.name, parcel_ids)
    time.sleep(10)