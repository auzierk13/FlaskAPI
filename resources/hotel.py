from flask_restful import Resource

hotels = [
    {
        "hotel_id": "alpha",
        "name": "Alpha hotel",
        "stars": 4.3,
        "daily": 420.34,
        "city": "Manaus"
    },
    {
        "hotel_id": "alpha",
        "name": "Bravo hotel",
        "stars": 4.4,
        "diaria": 440.34,
        "city": "São Paulo"
    },
    {
        "hotel_id": "alpha",
        "name": "Charle hotel",
        "stars": 3.9,
        "diaria": 390.34,
        "city": "Rio de janeiro"
    },
]


class Hotels(Resource):
    def get(self):
        return hotels

