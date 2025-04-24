import unittest
from modules.cluster import connect_to_cluster

class TestClusterConnection(unittest.TestCase):
    def test_connect_to_cluster(self):
        result = connect_to_cluster()
        self.assertIn("Kubernetes control plane", result)

if __name__ == "__main__":
    unittest.main()
