cmake_minimum_required(VERSION 3.0.2)
project(my_service)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
)

## Generate services in the 'srv' folder
add_service_files(
   FILES
   my_service.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
include
  ${catkin_INCLUDE_DIRS}
)

add_executable(my_service_server src/my_service_server.cpp)
add_executable(my_service_client src/my_service_client.cpp)

add_dependencies(my_service_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(my_service_client ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(my_service_server
   ${catkin_LIBRARIES}
)
target_link_libraries(my_service_client
   ${catkin_LIBRARIES}
)
