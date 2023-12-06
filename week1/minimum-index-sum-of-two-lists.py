class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = defaultdict(list)
        min_index_sum = float('inf')
        
        for i, restaurant in enumerate(list1):
            common[restaurant].append(i)
        
        common_restaurants = []
        
        for j, restaurant in enumerate(list2):
            if restaurant in common:
                indices = common[restaurant]
                for index in indices:
                    index_sum = index + j
                    if index_sum < min_index_sum:
                        min_index_sum = index_sum
                        common_restaurants = [restaurant]
                    elif index_sum == min_index_sum:
                        common_restaurants.append(restaurant)
        
        return common_restaurants