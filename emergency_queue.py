class Patient:
    def __init__(self, name, urgency):
        self.name = str(name)
        self.urgency = int(urgency)
        if not (1 <= self.urgency <= 10):
            raise ValueError("urgency must be between 1 and 10")

    def __repr__(self):
        return f"Patient(name={self.name!r}, urgency={self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    def _parent(self, i): return (i - 1) // 2 if i > 0 else None
    def _left(self, i):   return 2 * i + 1
    def _right(self, i):  return 2 * i + 2

    def heapify_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self.data[i].urgency < self.data[p].urgency:
                self.data[i], self.data[p] = self.data[p], self.data[i]
                i = p
            else:
                break

    def heapify_down(self, i):
        n = len(self.data)
        while True:
            left = self._left(i)
            right = self._right(i)
            smallest = i

            if left < n and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < n and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == i:
                break

            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest

    def insert(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("insert expects a Patient object")
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        n = len(self.data)
        if n == 0:
            return None
        if n == 1:
            return self.data.pop()
        root = self.data[0]
        self.data[0] = self.data.pop()  
        self.heapify_down(0)
        return root

    def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")


if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    
    next_up = heap.peek()
    if next_up:
        print(next_up.name, next_up.urgency)

    served = heap.remove_min()
    if served:
        print("Served:", served.name)
    heap.print_heap()
    
    empty = MinHeap()
    print("Peek empty:", empty.peek())
    print("Remove empty:", empty.remove_min())
    try:
        heap.insert(("not", "a", "patient"))
    except TypeError as e:
        print("Edge (type):", e)
