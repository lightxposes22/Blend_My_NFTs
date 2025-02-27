import bpy

from . import DNA_Generator

class bcolors:
   """
   The colour of console messages.
   """
   OK = '\033[92m'  # GREEN
   WARNING = '\033[93m'  # YELLOW
   ERROR = '\033[91m'  # RED
   RESET = '\033[0m'  # RESET COLOR


def get_combinations():
   """
   Returns "combinations", the number of all possible NFT DNA for a given Blender scene formatted to BMNFTs conventions
   combinations.
   """

   hierarchy = DNA_Generator.get_hierarchy()
   hierarchyByNum = []

   for i in hierarchy:
      # Ignore Collections with nothing in them
      if len(hierarchy[i]) != 0:
         hierarchyByNum.append(len(hierarchy[i]))
      else:
         print(f"The following collection has been identified as empty: {i}")

   combinations = 1
   for i in hierarchyByNum:
      combinations = combinations*i

   return combinations
