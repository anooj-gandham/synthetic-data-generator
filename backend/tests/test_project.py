
import unittest
from app import create_app

class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config["MONGO_URI"] = "mongodb://localhost:27017/test_db"

    def test_create_project(self):
        response = self.client.post('/api/projects', json={
            'name': 'Test Project',
            'description': 'A test project',
            'tags': ['test', 'project']
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
