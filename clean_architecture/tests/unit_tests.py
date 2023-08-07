import unittest


class Testing(unittest.TestCase):
    def test_ORM(self):
        from clean_architecture.adapters.ORM.post import PostModel
        model = PostModel()
        model.title = 'title test'
        model.id = 0
        model.content = 'post content'
        self.assertEqual(model.title, 'title test')


if __name__ == '__main__':
    unittest.main()