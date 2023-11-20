from backend import meal
from backend import mongoconnec


def mongo_uploadrecipe(recipe : meal.Meal()):
    coll = mongoconnec.get_mongocollrecipes()
    coll.insertOne(recipe)

def mongo_downloadrecipe(recipe : meal.Meal()):
    return None


