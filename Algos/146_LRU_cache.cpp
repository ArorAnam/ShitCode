#include <iostream>
#include <unordered_map>
#include <list>

class LRUCache {
public:
    LRUCache(int capacity) : capacity_(capacity) {}

    int get(int key) {
        auto it = cacheItemsMap.find(key);
        if (it == cacheItemsMap.end()) {
            return -1;
        } else {
            cacheItemsList.splice(cacheItemsList.begin(), cacheItemsList, it->second);
            return it->second->second;
        }
    }

    void put(int key, int value) {
        auto it = cacheItemsMap.find(key);
        if (it != cacheItemsMap.end()) {
            cacheItemsList.splice(cacheItemsList.begin(), cacheItemsList, it->second);
            it->second->second = value;
            return;
        }

        if (cacheItemsList.size() == capacity_) {
            auto del = cacheItemsList.back();
            cacheItemsMap.erase(del.first);
            cacheItemsList.pop_back();
        }

        cacheItemsList.emplace_front(key, value);
        cacheItemsMap[key] = cacheItemsList.begin();
    }

private:
    int capacity_;
    std::list<std::pair<int, int>> cacheItemsList;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cacheItemsMap;
};

int main() {
    LRUCache lruCache(2);
    lruCache.put(1, 1);
    lruCache.put(2, 2);
    std::cout << lruCache.get(1) << std::endl; // returns 1
    lruCache.put(3, 3); // evicts key 2
    std::cout << lruCache.get(2) << std::endl; // returns -1 (not found)
    lruCache.put(4, 4); // evicts key 1
    std::cout << lruCache.get(1) << std::endl; // returns -1 (not found)
    std::cout << lruCache.get(3) << std::endl; // returns 3
    std::cout << lruCache.get(4) << std::endl; // returns 4
    return 0;
}