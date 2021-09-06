from benchopt import BaseDataset, safe_import_context
from benchopt.datasets.simulated import make_correlated_data

with safe_import_context() as import_ctx:
    import numpy as np


class Dataset(BaseDataset):

    name = "Simulated"

    # List of parameters to generate the datasets. The benchmark will consider
    # the cross product for each key in the dictionary.
    parameters = {
        'n_samples, n_features': [
            (100, 5000),
            (100, 10000)],  # slow to simulate big correlated design
        'rho': [0, 0.6]
    }

    def __init__(self, n_samples=50, n_features=10, rho=0, random_state=27):
        # Store the parameters of the dataset
        self.n_samples = n_samples
        self.n_features = n_features
        self.random_state = random_state
        self.rho = rho

    def get_data(self):
        rng = np.random.RandomState(self.random_state)

        X, y, _ = make_correlated_data(self.n_samples, self.n_features,
                                       rho=self.rho, random_state=rng)

        data = dict(X=X, y=y)

        return self.n_features + 2, data
