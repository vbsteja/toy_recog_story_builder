from game.objects import Actor

class Game:
    """ Base class for game logic. """
    def __init__(self):
        self.actors = {}  # Dictionary to hold game actors
        self.state = 'idle'
        self.current_actor = None
        self.current_dialogue = None
        self.time = 0  # Game time in seconds

    def add_actor(self, name):
        """Add a new actor to the game."""
        self.actors[name] =Actor(name)

    def remove_actor(self, name):
        """Remove an actor from the game."""
        if name in self.actors:
            del self.actors[name]

    def get_actor(self, name):
        """Get an actor by its name."""
        return self.actors.get(name, None)

    def update_time(self, dt):
        """Update the game time."""
        self.time += dt
        if self.time >= 60:
            self.time = 0
    def reset_game(self):
        """Reset the game state."""
        self.actors.clear()
        self.state = 'idle'
        self.current_actor = None
        self.current_dialogue = None
        self.time = 0

    def start_game(self):
        """Start the game."""
        self.state = 'running'
        self.time = 0
        # Initialize actors or game state as needed

    def pause_game(self):
        """Pause the game."""
        self.state = 'paused'
        # Save current state or perform any necessary actions
    def resume_game(self):
        """Resume the game."""
        if self.state == 'paused':
            self.state = 'running'
            # Restore game state or perform any necessary actions
    def end_game(self):
        """End the game."""
        self.state = 'ended'
        # Perform any cleanup or final actions
        # e.g., save score, show end screen, etc.
    def get_game_state(self):
        """Get the current game state."""
        return {
            'state': self.state,
            'time': self.time,
            'actors': {name: actor.get_state() for name, actor in self.actors.items()}
        }
    def set_game_state(self, state):
        """Set the game state from a saved state."""
        self.state = state.get('state', 'idle')
        self.time = state.get('time', 0)
        self.actors = {name: Actor(**actor) for name, actor in state.get('actors', {}).items()}
        # Restore current actor and dialogue if needed
        self.current_actor = None
        self.current_dialogue = None

    def get_current_actor(self):
        """Get the current actor."""
        return self.current_actor
    def set_current_actor(self, actor_name):
        """Set the current actor."""
        if actor_name in self.actors:
            self.current_actor = self.actors[actor_name]
        else:
            self.current_actor = None
    def get_current_dialogue(self):
        """Get the current dialogue."""
        return self.current_dialogue
    def set_current_dialogue(self, dialogue):
        """Set the current dialogue."""
        self.current_dialogue = dialogue
        if self.current_actor:
            self.current_actor.set_dialogue(dialogue)
        else:
            raise ValueError("No current actor set for dialogue.")
    def get_game_time(self):
        """Get the current game time."""
        return self.time
    def set_game_time(self, time):
        """Set the game time."""
        if time < 0:
            raise ValueError("Time cannot be negative.")
        self.time = time
    def reset_game_time(self):
        """Reset the game time to zero."""
        self.time = 0

    def update_game(self, dt):
        """Update the game state."""
        if self.state == 'running':
            self.update_time(dt)
            # Update actors or game logic as needed
            for actor in self.actors.values():
                actor.update(dt)
        elif self.state == 'paused':
            # Handle paused state if needed
            pass
        elif self.state == 'ended':
            # Handle end of game state if needed
            pass

    def get_game_info(self):
        """Get basic game information."""
        return {
            'state': self.state,
            'time': self.time,
            'actor_count': len(self.actors),
            'current_actor': self.current_actor.name if self.current_actor else None,
            'current_dialogue': self.current_dialogue
        }
    def save_game(self, filename):
        """Save the game state to a file."""
        import json
        with open(filename, 'w') as f:
            json.dump(self.get_game_state(), f, indent=4)
    def load_game(self, filename):
        """Load the game state from a file."""
        import json
        with open(filename,
                    'r') as f:
                state = json.load(f)
        self.set_game_state(state)
    def __str__(self):
        """String representation of the game."""
        return f"Game(state={self.state}, time={self.time}, actors={list(self.actors.keys())})"