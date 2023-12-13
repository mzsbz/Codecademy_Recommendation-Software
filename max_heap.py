class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2
    
    def left_child_idx(self, idx):
        return idx * 2
    
    def right_child_idx(self, idx):
        return idx * 2 + 1
    
    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            # print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child_score = self.heap_list[self.left_child_idx(idx)][-1]
            right_child_score = self.heap_list[self.right_child_idx(idx)][-1]

            if left_child_score > right_child_score:
                # print("Left child larger")
                return self.left_child_idx(idx)
            else:
                # print("Right child larger")
                return self.right_child_idx(idx)
            
    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def add(self, element):
        # print(f'Adding {element} to {self.heap_list}')
        
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        # print('Restoring the heap property...')

        idx = self.count

        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            child_score = self.heap_list[idx][-1]
            parent_score = self.heap_list[self.parent_idx(idx)][-1]
            child_title = self.heap_list[idx][0]
            parent_title = self.heap_list[self.parent_idx(idx)][0]

            if parent_score < child_score:
                # print(f"swapping {parent_title}|{parent_score} with {child_title}|{child_score}")
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            idx = self.parent_idx(idx)

            # print(f"HEAP RESTORED! {self.heap_list}")
    
    def retrieve_max(self):
        if self.count == 0:
            # print("No items in heap")
            return None
        
        max_val = self.heap_list[1]
        # print(f"Removing:{max_val} from {self.heap_list}")

        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1

        self.heap_list.pop()

        # print(f"Last element moved to first: {self.heap_list}")

        self.heapify_down()
        return max_val
    
    def heapify_down(self):
        # print("Heapifying down!")
        idx = 1

        while self.child_present(idx):
            # print("Heapifying down!")
            larger_child_idx = self.get_larger_child_idx(idx)
            child = self.heap_list[larger_child_idx]
            parent = self.heap_list[idx]
            child_score = self.heap_list[larger_child_idx][-1]
            parent_score = self.heap_list[idx][-1]

            if parent_score < child_score:
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
            
            idx = larger_child_idx

        # print(f"HEAP RESTORED! {self.heap_list}")