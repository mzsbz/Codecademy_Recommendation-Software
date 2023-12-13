from max_heap import MaxHeap

class Recommender:
    # Use ?? data structure and ?? to find similar movies
    def __init__(self):
        self.data = []
        self.max_heap = MaxHeap()
    
    def import_data(self, data):
        self.data = data

    def deviation_rating(self, item, comparator):
        ratings = {'G':1, 'PG':2, 'PG-13':3, 'NC-17':4, 'R':5, 'Not Rated':5}
        try:
            id_item = ratings[item]
            id_comparator = ratings[comparator]
            # R - PG-13 = 5 - 3 = 2 | G - R = 1 - 5 = -4
            deviation = abs(id_comparator - id_item) * 20
        except:
            deviation = 100

        return deviation
    
    def deviation(self, item, comparator):
        try:
            return int(abs(item - comparator))/comparator * 100
        except:
            return 0
    
    def calculate_similarity(self):
        comparator = self.data[0]
        for item in self.data:
            rating_similarity = 100 - self.deviation_rating(item[2], comparator[2])
            runtime_similarity = 100 - self.deviation(item[3], comparator[3])
            score_similarity = 100 - self.deviation(item[4], comparator[4])
            similarity = round((rating_similarity + score_similarity + (runtime_similarity*0.1))/210 * 100, 2)
            item.append(similarity)
        # print(self.data)

    def heapsort(self):
        sort = []

        for item in self.data:
            self.max_heap.add(item)

        while self.max_heap.count > 0:
            max_value = self.max_heap.retrieve_max()
            sort.insert(0, max_value)

        return sort

        