cmake_minimum_required(VERSION 3.22.6)
project(draft VERSION 0.1)

find_package(asio REQUIRED)

add_executable(draft src/draft.cpp)
target_link_libraries(draft asio::asio)

