from utils import normalize_data, normalize_weights


class Solver:
    def __init__(self, criterion_cnt: int, size: int, raw_data: list[list[int |float]], raw_weights: list[float], directions):
        self.criterion_cnt = criterion_cnt
        self.size = size
        self.data = raw_data  #normalize_data(raw_data)
        self.weights = normalize_weights(raw_weights)
        self.directions = [1 if x == 'max' else -1 for x in directions]


    def convolution(self, data):
        total_res = []
        for row in range(len(data)):
            total_res.append(0)
            for col in range(len(data[0]) - 1):
                if self.directions[col] == 1:
                    total_res[-1] += self.weights[col] * data[row][col + 1]
                else:
                    total_res[-1] += self.weights[col] * data[row][col + 1] * -1
            total_res[-1] = round(total_res[-1], 3)


        self.result = total_res
        return total_res


    def create_pareto(self):
        def check_pareto(elem, others):
            for other in others:
                if other == elem:
                    continue
                new_elem = elem[:]
                new_other = other[:]
                for i in range(1, len(new_elem)):
                    new_elem[i] *= self.directions[i - 1]
                    new_other[i] *= self.directions[i - 1]

                if all(a <= b for a, b in zip(new_elem[1:], new_other[1:])) and any(a < b for a, b in zip(new_elem[1:], new_other[1:])):
                    return False
            return True
        res = []
        for i in range(len(self.data)):
            elem = self.data[i]
            if check_pareto(elem, self.data):
                res.append(elem)
        return res


if __name__ == '__main__':
    pass