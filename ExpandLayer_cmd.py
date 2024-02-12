import rhinoscriptsyntax as rs

__commandname__ = "ExpandLayer"


# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
  
  VERSION = "1.0.0.0"
  print("***RUN ExpandLayer (ver {})".format(VERSION))
  
  ### Get All Layers
  layer_ids = rs.LayerIds()
  
  for layer_id in layer_ids:
    
    ### Get Layer Expand-Status
    is_expanded = rs.IsLayerExpanded(layer_id)
    # print(is_expanded)
    
    ### Update
    if is_expanded == False:
      
      ### Get Layer Name
      name = rs.LayerName(layer_id)
      
      ### Update
      rs.ExpandLayer(layer_id, True)
      
      print("###Expand : {}".format(name))
    
    
  
  # you can optionally return a value from this function
  # to signify command result. Return values that make
  # sense are
  #   0 == success
  #   1 == cancel
  # If this function does not return a value, success is assumed
  return 0
