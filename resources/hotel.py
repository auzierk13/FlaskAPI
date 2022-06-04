from flask_restful import Resource, reqparse

from models.hotel import HotelModel

hotels = [
    {
        "hotel_id": "alpha",
        "name": "Alpha hotel",
        "stars": 4.3,
        "daily": 420.34,
        "city": "Manaus"
    },
    {
        "hotel_id": "bravo",
        "name": "Bravo hotel",
        "stars": 4.4,
        "daily": 440.34,
        "city": "São Paulo"
    },
    {
        "hotel_id": "charle",
        "name": "Charle hotel",
        "stars": 3.9,
        "daily": 390.34,
        "city": "Rio de janeiro"
    },
]


class Hotels(Resource):
    def get(self):
        return hotels


class Hotel(Resource):
    request_argument = reqparse.RequestParser()
    request_argument.add_argument("name")
    request_argument.add_argument("stars")
    request_argument.add_argument("daily")
    request_argument.add_argument("city")

    @staticmethod
    def find_hotel(hotel_id):
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = self.find_hotel(hotel_id)
        if hotel:
            return hotel, 200
        return {"message": "Hotel not found"}, 404

    def post(self, hotel_id):
        dados = self.argument_parse(hotel_id)
        print(dados)
        hotels.append(dados)
        return dados, 200

    @staticmethod
    def argument_parse(hotel_id):
        dados = Hotel.request_argument.parse_args()
        hotel_model = HotelModel(hotel_id, **dados)
        print(f"hotel_model {hotel_model}")
        return hotel_model.json()

    def put(self, hotel_id):
        dados = self.argument_parse(hotel_id)
        print(dados)
        hotel = self.find_hotel(hotel_id)
        if hotel:
            hotel.update(dados)
            return dados, 200
        hotels.append(dados)
        return dados, 201  # Created
    
    def delete(self, hotel_id):
        for index, hotel in enumerate(hotels):
            if hotel["hotel_id"] == hotel_id:
                hotels.remove(hotel)
                return hotels
        return 404
