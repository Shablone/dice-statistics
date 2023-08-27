#%%
import matplotlib.pyplot as plt
from src.dice import Die, FairDie, UnFairDie

class Board_Statistics:
    def __init__(self):
        self.chances = {}
        self.chances[0]=1.0

    def new(self):
        self.chances = {}
        self.chances[0]=1.0
        return self
    def add_flat_value(self, val):
        glob_chances_new = {}
        for glob_outcome, glob_chance in self.chances.items():
            glob_chances_new[glob_outcome+1] = glob_chance
        self.chances = glob_chances_new

    def add_die(self, die : Die):
        self._add_chances_to_self(die.chances)
        return self
    
    def add_highest(self, dice: [Die]):
        self._add_chances_to_self(self._pick_highest(dice))
        return self
    
    def _add_chances_to_self(self, chances: dict):
        glob_chances_new = {}
        for outcome, outcome_chance in chances.items():
            for glob_outcome, glob_chance in self.chances.items():
                curr_outcome = outcome + glob_outcome
                if curr_outcome in glob_chances_new:
                    glob_chances_new[curr_outcome] += outcome_chance * glob_chance
                else:
                    glob_chances_new[curr_outcome] = outcome_chance * glob_chance
        self.chances = glob_chances_new
        return self        
    
    def _pick_highest(self, dice: [Die]):
        aggr_chances = {}    
        aggr_chances[0] = 1.0
        for die in dice:
            aggr_chances_new = {}
            for die_outcome, die_chance in die.chances.items():
                for aggr_outcome, aggr_chance in aggr_chances.items():
                    outcome = max(die_outcome,aggr_outcome)
                    if outcome in aggr_chances_new:
                        aggr_chances_new[outcome] += die_chance * aggr_chance
                    else:
                        aggr_chances_new[outcome] = die_chance * aggr_chance
            aggr_chances =  aggr_chances_new
        return aggr_chances
    
    def plot(self):    



        x_values = list(self.chances.keys())
        y_values = list(self.chances.values())

        all_keys = range(min(x_values), max(x_values) + 1)
        for key in all_keys:
            if key not in self.chances:
                x_values.append(key)
                y_values.append(0)         

        sorted_data = sorted(zip(x_values, y_values))
        sorted_x_vals = [x for x, _ in sorted_data]
        sorted_y_vals = [y for _, y in sorted_data]

        weighted_mean_value = sum(x * y for x, y in zip(sorted_x_vals, sorted_y_vals))
        cumulative_probabilities = [sum(sorted_y_vals[:i+1]) for i in range(len(sorted_y_vals))]

        median_index = next(i for i, cp in enumerate(cumulative_probabilities) if cp >= 0.5)
        median_value = sorted_x_vals[median_index]

        squared_deviations_sum_weighted_mean = sum((x - weighted_mean_value)**2 * y for x, y in zip(sorted_x_vals, sorted_y_vals))
        weighted_std_deviation = (squared_deviations_sum_weighted_mean / sum(sorted_y_vals)) ** 0.5

        plt.bar(sorted_x_vals, sorted_y_vals)
        plt.xlabel('X-axis')
        plt.ylabel('Probability')
        plt.title('Plotting Data')
        plt.axvline(weighted_mean_value, color='red', linestyle='--', label=f'Weighted Mean: {weighted_mean_value:.2f}')
        plt.axvline(median_value, color='green', linestyle='--', label=f'Weighted Median: {median_value:.2f}')
        plt.legend()
        plt.xticks(ticks=sorted_x_vals, labels=[f'{int(val):d}' for val in sorted_x_vals])
        plt.show()



