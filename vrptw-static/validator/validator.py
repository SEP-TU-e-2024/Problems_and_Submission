import pyvrp

#----------------------------------------------------------------
# TYPES
#----------------------------------------------------------------
COORDS = list[tuple[int, int]]
DEMAND = list[int]
TIME_WINDOW = list[tuple[int, int]]

RAWDATA = dict[str, int | COORDS | DEMAND | TIME_WINDOW]
RAWSOLUTION = list[list[int]]

#----------------------------------------------------------------
# VALIDATOR
#----------------------------------------------------------------

class Validator:

    OUTPUT_FILE = "/results/results.csv"

    def obtain_data(self, raw: bool=False) -> pyvrp.ProblemData | RAWDATA:
        problemdata = pyvrp.read("instances/instance")
        
        if not raw:
            return problemdata

        return {
            "num_clients": problemdata.num_clients,
            "num_vehicles": problemdata.num_vehicles,
            "num_depots": problemdata.num_depots,
            "capacity": problemdata.vehicle_types()[0].capacity,
            "client_coords": [(c.x, c.y) for c in problemdata.clients()],
            "depot_coords": [(d.x, d.y) for d in problemdata.depots()],
            "demand": [c.delivery for c in problemdata.clients()],
            "time_window": [(c.tw_early, c.tw_late) for c in problemdata.clients()]
        }

    def push_data(self, solution: pyvrp.Solution | RAWSOLUTION):
        if type(solution) != pyvrp.Solution:
            solution = pyvrp.Solution(data=pyvrp.read("instances/instance"), routes=RAWSOLUTION)

        if not solution.is_feasable():
            raise ValueError("Solution provided is not valid")

        with open(self.OUTPUT_FILE, "w", newline="") as f:
            f.write("Score\n")
            f.write(solution.distance_cost())
