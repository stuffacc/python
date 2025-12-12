import pytest
import bheap     

def test_min():
    heap = bheap.BHeap([])
    
    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    
    assert heap.find_min() == 10    


if __name__ == "__main__":
    pytest.main()
