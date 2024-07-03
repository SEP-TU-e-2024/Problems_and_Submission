class Validator():
    OUTPUT_FILE = "/results/results.csv"

    def __init__(self):
        self.reward = 0

        with open('instances/instance', 'r') as f:
            lines = f.readlines()
            self.right_answer = int(lines[0])
            self.numbers = [int(n) for n in lines[1:]]

    def obtain_data(self) -> int:
        if len(self.numbers) == 0:
            return None
        return self.numbers.pop()

    def push_data(self, num: int):
        if num == self.right_answer:
            self.reward = 1
        
        with open(self.OUTPUT_FILE, "w", newline="") as f:
            f.write("reward\n")
            f.write(str(self.reward))