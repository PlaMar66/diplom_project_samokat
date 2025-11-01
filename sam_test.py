import request
import data
# Бороздин Евгений, 37-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_order_info_by_track():
    track = request.create_order(data.order_body).json()['track']
    response = request.get_order_info_by_track(track)
    assert response.status_code == 200