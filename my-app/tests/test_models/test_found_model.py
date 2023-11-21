import unittest
from found_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Arrange
        # Act
        instance = BaseModel()

        # Assert
        self.assertEqual(instance.id, None)
        self.assertIsNotNone(instance.created_at)
        self.assertIsNotNone(instance.updated_at)

    def test_save(self):
        # Arrange
        instance = BaseModel()
        instance.username = "test"
        instance.email = "test@example.com"
        instance.password = "password"

        # Act
        instance.save()

        # Assert
        self.assertIsNotNone(instance.id)
        self.assertEqual(instance.username, "test")
        self.assertEqual(instance.email, "test@example.com")
        self.assertEqual(instance.password, "password")

    def test_delete(self):
        # Arrange
        instance = BaseModel()
        instance.username = "test"
        instance.email = "test@example.com"
        instance.password = "password"
        instance.save()

        # Act
        instance.delete()

        # Assert
        instance = BaseModel.retrieve(instance.id)
        self.assertEqual(instance, None)

    def test_create(self):
        # Arrange
        # Act
        instance = BaseModel.create(
            username="test",
            email="test@example.com",
            password="password",
        )

        # Assert
        self.assertIsNotNone(instance.id)
        self.assertEqual(instance.username, "test")
        self.assertEqual(instance.email, "test@example.com")
        self.assertEqual(instance.password, "password")

    def test_retrieve(self):
        # Arrange
        instance = BaseModel.create(
            username="test",
            email="test@example.com",
            password="password",
        )

        # Act
        retrieved_instance = BaseModel.retrieve(instance.id)

        # Assert
        self.assertEqual(retrieved_instance, instance)

    def test_count(self):
        # Arrange
        instance1 = BaseModel.create(
            username="test",
            email="test@example.com",
            password="password",
        )
        instance2 = BaseModel.create(
            username="test",
            email="test@example.com",
            password="password",
        )

        # Act
        count = BaseModel.count()

        # Assert
        self.assertEqual(count, 2)

    def test_update_attributes(self):
        # Arrange
        instance = BaseModel.create(
            username="test",
            email="test@example.com",
            password="password",
        )

        # Act
        instance.username = "test"
        instance.email = "test@example.com"
        instance.update_attributes()

        # Assert
        self.assertEqual(instance.username, "test")
        self.assertEqual(instance.email, "test@example.com")

if __name__ == "__main__":
    unittest.main()
