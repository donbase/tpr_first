from statistics import mean, stdev
import numpy as np


def normalize_weights(raw_weights: list[float]) -> list[float]:
    """
    Нормирование значений весов критериев
    """
    total_sum = sum(raw_weights)
    return [elem / total_sum for elem in raw_weights]


def normalize_data(raw_data: list[list[float]]) -> list:
    """
    Z-нормализация входных данных
    :param raw_data:
    :return:
    """

    data = np.array(raw_data)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    normalized_data = (data - mean) / std
    #print(normalized_data)
    return normalized_data.tolist()
