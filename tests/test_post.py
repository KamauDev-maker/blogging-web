import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_cate = User(first_name = "Sekani",
                                last_name = "Kamau",
                                username = "Skn",
                                password = "12345",
                                email = "sekani@gmail.com")
        self.new_post = Post(post_title = "Toys",
                            post_content = "Big Toys cars",
                            user_id = self.user_cate.id)
        self.new_comment = Comment(comment = "Want to buy",
                                    post_id = self.new_post.id,
                                    user_id = self.user_sekani.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_sekani, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))  