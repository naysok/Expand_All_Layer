import rhinoscriptsyntax as rs


#https://developer.rhino3d.com/api/RhinoScriptSyntax/#layer-LayerIds
#https://developer.rhino3d.com/api/RhinoScriptSyntax/#layer-ExpandLayer


### Get All Layers
layer_ids = rs.LayerIds()


for layer_id in layer_ids:
    
    ### Get Layer Name
    name = rs.LayerName(layer_id)
    print(name)
    
    ### Get Layer Expand-Status
    is_expanded = rs.IsLayerExpanded(layer_id)
    print(is_expanded)
    
    ### Update
    if is_expanded == False:
        rs.ExpandLayer(layer_id, True)
    
    print("- - -")
    