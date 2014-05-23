import random
import operator
import sys

class GameServer:
    all_shoes = {}
    not_picked = {}
    current_centroids = []
    selected_shoes = []

    def get_distance(self, shoe1, shoe2):
        pass


    def load_shoes(self):
        pass

    def __init__(self):
        self.load_shoes(self)

    def get_next_samples(self, number):
        centroids = self.kmean(number)
        current_centroids = centroids
        return centroids

    def get_current_rank(self):
        shoes = []
        for i in range(10):
            shoe = Shoe()
            shoes.append(shoe)
        return shoes

    def feed_option(self, shoe):
        pass

    def kmeans(self, number):
        self.selected_shoes = random.shuffle(self.selected_shoes)
        centroids = self.selected_shoes[:number]
        for iter in range(10):
            assigning = [[] for i in range(number)]
            for shoe in self.selected_shoes:
                distances = [self.get_distance(shoe, centroid) for centroid in centroids]
                min_index, min_value = min(enumerate(distances), key=operator.itemgetter(1))
                assigning[min_index].append(shoe)
            centroids = self.new_centroids(assigning)
        return centroids

    def new_centroids(self, assigning):
        centroids = []
        for shoes in assigning:
            min_dis = sys.float_info.max
            centroid = None
            for shoeA in shoes:
                dis_sum = sum([self.get_distance(shoeA, shoeB) for shoeB in shoes])
                if dis_sum < min_dis:
                    min_dis = dis_sum
                    centroid = shoeA
            centroids.append(centroid)
        return centroids









class Shoe:
    def __init__(self):
        pass