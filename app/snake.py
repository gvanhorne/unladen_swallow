import json
import bottle

class Snake(object):
    """Create an object representing the snake."""
    def __init__(self, snake):
        self.id = snake['id']
        self.coords = self.body(snake)

    def body(self, snake):
        coords = []
        for i in snake['body']:
          coords.append([i['x'], i['y']])
        return coords


