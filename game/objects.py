

class Actor:
    def __init__(self, name):
        self.name = name
        self.dialogue = None

    def get_state(self):
        """Get the current state of the actor."""
        return {
            'name': self.name
            #'position': self.position,
            #'dialogue': self.dialogue
        }

    def set_dialogue(self, dialogue):
        """Set the dialogue for the actor."""
        self.dialogue = dialogue

    def update(self, dt):
        """Update the actor's state based on the elapsed time."""
        # Implement actor-specific update logic here
        pass