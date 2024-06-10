# models/magazine.py
class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.id} {self.name} {self.category}>'

    def get_magazine_id(self):
        return self.id

    def save(self):
        # Add saving functionality here
        pass

# tests/test_models.py
import unittest
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_get_magazine_id(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.get_magazine_id(), 1)

    def test_saves_magazine(self):
        magazine = Magazine(None, "Tech Weekly", "Technology")
        with self.assertRaises(AttributeError):
            magazine.save()

if __name__ == "__main__":
    unittest.main()
