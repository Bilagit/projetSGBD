# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\directeur_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\directeur_autogen.dir\\ParseCache.txt"
  "directeur_autogen"
  )
endif()
