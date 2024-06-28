from pyvrp import Model

from validator.Validator import Validator


def main():
    val = Validator()
    problem = val.obtain_data(raw=False)

    model = Model.from_data(problem)
    result = model.solve()

    val.push_data(result.best)

if __name__ == "__main__":
    main()