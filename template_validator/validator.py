#----------------------------------------------------------------
# TEMPLATE VALIDATOR
#----------------------------------------------------------------

class Validator:
    """
    This is a base class that should be used as a template for the Validator.
    It defines some basic functionality that should be implemented by the Validator: obtain_data and push_data.
    """

    # Docker container expects this file to be created after evalution
    OUTPUT_FILE = "/results/results.csv"

    def obtain_data(self):
        """
        obtain_data is called by the submission code to obtain a new (or the initial) state of the current problem.
        The Validator must implement this function and define the appropriate return datatype.
        """
        pass

    def push_data(self):
        """
        push_data is called by the submission code to push a new solution it has computed to the validator.
        The Validator must implement this function and define the appropriate datatype for such a solution.
        Every time this method is called the Validator should write the current score to a results file (overwrite content of file).
        Metrics written to results.csv should be in csv format: first line contains the fields seperated by a comma,
        the second line contains the values seperated by a comma. 
        """
        # Run this code at end of method
        # Replace "cost" by "reward" if the problem is a maximization problem
        with open(self.OUTPUT_FILE, "w", newline="") as f:
            f.write("cost\n")
            f.write(str(1)) #example value

