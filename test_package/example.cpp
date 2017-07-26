#include <iostream>
#include <array>
#include "include/numerical.hpp"

int main() {
    std::array<int, 3> nums{1, 2, 3};
    std::cout << "average of [1, 2, 3] is " 
              << shino::average(nums.begin(), nums.end(), 0)
              << '\n';
}
