from peewee import *

db = SqliteDatabase('db.db')


class BaseModel(Model):
    class Meta:
        database = db


class Housing(BaseModel):
    id = AutoField()
    region = CharField()
    price = FloatField()
    address = CharField()
    full_address = CharField()

    units = FloatField()
    square = FloatField()
    builts = FloatField()
    stories = FloatField()

    beds = FloatField()
    rooms = FloatField()
    baths = FloatField()

    nofee = BooleanField()
    gym = BooleanField(default=False) #'Gym': 'gym',
    loft = BooleanField(default=False) # 'Loft': 'loft',
    deck = BooleanField(default=False) # 'Deck': 'deck',
    patio = BooleanField(default=False) # 'Patio': 'patio',
    garden = BooleanField(default=False) # 'Garden':'garden',
    sublet = BooleanField(default=False) # 'Sublet':'sublet',
    terrace = BooleanField(default=False) # 'Terrace': 'terrace',
    doorman = BooleanField(default=False) # 'Doorman': 'doorman',
    hot_tub = BooleanField(default=False) # 'Hot Tub':'hot_tub',
    balcony = BooleanField(default=False) # 'Balcony':  'balcony',
    elevator = BooleanField(default=False) # 'Elevator':'elevator',
    bike_room = BooleanField(default=False) # 'Bike Room':'bike_room',
    roof_deck = BooleanField(default=False) # 'Roof Deck':'roof_deck',
    city_view = BooleanField(default=False) # 'City View': 'city_view',
    concierge = BooleanField(default=False) # 'Concierge': 'concierge',
    courtyard = BooleanField(default=False) # 'Courtyard': 'courtyard',
    fireplace = BooleanField(default=False) # 'Fireplace': 'fireplace',
    furnished = BooleanField(default=False) # 'Furnished': 'furnished',
    park_view = BooleanField(default=False) # 'Park View': 'park_view',
    media_room = BooleanField(default=False) # 'Media Room':'media_room',
    dishwasher = BooleanField(default=False) # 'Dishwasher': 'dishwasher',
    water_view = BooleanField(default=False) # 'Water View': 'water_view',
    smoke_free = BooleanField(default=False) # 'Smoke-free': 'smoke_free',
    waterfront = BooleanField(default=False) # 'Waterfront': 'waterfront',
    roof_rights = BooleanField(default=False) # 'Roof Rights':'roof_rights',
    central_air = BooleanField(default=False) # 'Central Air': 'central_air',
    garden_view = BooleanField(default=False) # 'Garden View':'garden_view',
    locker_cage = BooleanField(default=False) # 'Locker/Cage': 'locker_cage',
    package_room = BooleanField(default=False) # 'Package Room':'package_room',
    cold_storage = BooleanField(default=False) # 'Cold Storage': 'cold_storage',
    pets_allowed = BooleanField(default=False) # 'Pets Allowed': 'pets_allowed',
    skyline_view = BooleanField(default=False) # 'Skyline View':'skyline_view',
    swimming_pool = BooleanField(default=False) # 'Swimming Pool':'swimming_pool',
    valet_parking = BooleanField(default=False) # 'Valet Parking':'valet_parking',
    gifts_allowed = BooleanField(default=False) # 'Gifts Allowed':'gifts_allowed',
    live_in_super = BooleanField(default=False) # 'Live-in Super':'live_in_super',
    green_building = BooleanField(default=False) # 'Green Building': 'green_building',
    garage_parking = BooleanField(default=False) # 'Garage Parking': 'garage_parking',
    hardwood_floors = BooleanField(default=False) # 'Hardwood Floors': 'hardwood_floors',
    sublets_allowed = BooleanField(default=False) # 'Sublets Allowed': 'sublets_allowed',
    virtual_doorman = BooleanField(default=False) # 'Virtual Doorman': 'virtual_doorman',
    wheelchair_acces = BooleanField(default=False) # 'Wheelchair Access': 'wheelchair_acces',
    storage_available = BooleanField(default=False) # 'Storage Available': 'storage_available',
    parking_available = BooleanField(default=False) # 'Parking Available': 'parking_available',
    part_time_doorman = BooleanField(default=False) # 'Part-time Doorman': 'part_time_doorman',
    private_roof_deck = BooleanField(default=False) # 'Private Roof Deck': 'private_roof_deck',
    full_time_doorman = BooleanField(default=False) # 'Full-time Doorman': 'full_time_doorman',
    cats_only_no_dogs = BooleanField(default=False) # 'Cats Only - No Dogs':'cats_only_no_dogs',
    childrens_playroom = BooleanField(default=False) # 'Children's Playroom': 'childrens_playroom',
    guarantors_allowed = BooleanField(default=False) # 'Guarantors Allowed': 'guarantors_allowed',
    guarantors_accepted = BooleanField(default=False) # 'Guarantors Accepted': 'guarantors_accepted',
    laundry_in_building = BooleanField(default=False) # 'Laundry in Building': 'laundry_in_building',
    co_purchase_allowed = BooleanField(default=False) # 'Co-purchase Allowed': 'co_purchase_allowed',
    fireplace_decorative = BooleanField(default=False) # 'Fireplace: Decorative': 'fireplace_decorative',
    washer_dryer_in_unit = BooleanField(default=False) # 'Washer / Dryer in Unit': 'washer_dryer_in_unit',
    pied_a_terre_allowed = BooleanField(default=False) # 'Pied-a-Terre Allowed': 'pied_a_terre_allowed',
    cats_and_dogs_allowed = BooleanField(default=False) # 'Cats and Dogs Allowed': 'cats_and_dogs_allowed',
    parents_buying_allowed = BooleanField(default=False) # 'Parents Buying Allowed': 'parents_buying_allowed',
    board_approval_required = BooleanField(default=False) # 'Board Approval Required': 'board_approval_required',
    community_recreation_facilities = BooleanField(default=False) # 'Community Recreation Facilities''community_recreation_facilities',


if __name__ == '__main__':
    Housing.drop_table()
    Housing.create_table()