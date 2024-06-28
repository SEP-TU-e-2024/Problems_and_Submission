from pyvrp import Model
from pyvrp.stop import MaxRuntime

from validator.validator import Validator


def main():
    val = Validator()
    problem = val.obtain_data(raw=False)

    model = Model.from_data(problem)
    result = model.solve(stop=MaxRuntime(30), display=False)

    val.push_data(result.best)

if __name__ == "__main__":
    main()