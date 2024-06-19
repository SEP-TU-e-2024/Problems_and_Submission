from validator.IOModule import IOModule

class Validator(IOModule):
    def __init__(self):
        self.reward = 0

        with open('instances/instance', 'r') as f:
            lines = f.readlines()
            self.right_answer = int(lines[0])
            self.numbers = [int(n) for n in lines[1:]]

    def _score(self) -> dict:
        return {"score": self.reward}

    def obtain_data(self) -> int:
        if len(self.numbers) == 0:
            return None
        return self.numbers.pop()

    def push_data(self, num: int):
        if num == self.right_answer:
            self.reward = self.right_answer