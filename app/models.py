from datetime import datetime as dt

class Post:
    def __init__(self, _id, image, email, title, body):
        self._id = _id
        self.image = image
        self.email = email
        self.title = title
        self.body = body
        self.created_on = dt.utcnow()

    # def from_dict(self):
    #     pass

    def to_dict(self):
        return {
            'id': self._id,
            'image': self.image,
            'email': self.email,
            'title': self.title,
            'body': self.body,
            'created_on': self.created_on
        }

    def __repr__(self):
        return f'<Post: [{self.email}]: {self.body[:20]}...'