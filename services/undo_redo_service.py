from undo_redo.data_structures.stack import Stack

class UndoRedoService:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.current_state = ""

    def perform_action(self, action):
        self.undo_stack.push(self.current_state)
        self.current_state += action
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack.is_empty():
            return "Nothing to undo"
        self.redo_stack.push(self.current_state)
        self.current_state = self.undo_stack.pop()
        return self.current_state

    def redo(self):
        if self.redo_stack.is_empty():
            return "Nothing to redo"
        self.undo_stack.push(self.current_state)
        self.current_state = self.redo_stack.pop()
        return self.current_state

    def get_state(self):
        return self.current_state
