# VortexScript v0.2
VortexScript is a programming language that compiles to vortex maps.  
The file extension for VortexScript is .vs

## TODO-LIST

### Formats
- [x] JSON format  
- [ ] VRTX format  

### Objects
- [x] Parts  
- [x] Textures  
- [x] PointLight  
- [x] SpotLight  
- [x] Groups  
- [x] Lighting  

### Parts
- [x] Part variable type  
- [x] Position (Vector3)  
- [x] Rotation (Vector4)  
- [x] Scale (Vector3)  
- [x] Color (ColorRGBA)  
- [x] Material (String)  
- [x] Group (Group Variable Type)  
- [x] Cast Shadow (Boolean)  
- [x] Anchored (Boolean)  
- [x] Can Collide (Boolean)  
- [x] Spawn Location (Boolean)  
- [x] Baseplate (Boolean)  
- [x] Custom Appearance (Boolean)  
- [x] Truss (Boolean)  
- [x] Textures (Texture variable type)  
- [x] PointLight (PointLight variable type)  
- [x] SpotLight (SpotLight variable type)  

### Textures
- [x] Texture variable type  
- [x] Face (String)  
- [x] Texture (String)  

### PointLight
- [x] Color (ColorRGBA)  
- [x] Intensity (Float)  
- [x] Range (Float)  
- [x] Shadow Maps Enabled (Boolean)  

### SpotLight
- [x] SpotLight variable type  
- [x] Color (ColorRGBA)  
- [x] Intensity (Float)  
- [x] Range (Float)  
- [x] Angle (Float)  
- [x] Shadow Maps Enabled (Boolean)  
- [x] Face (String)  

### Groups
- [x] Group variable type  
- [x] Parent Group (Integer)  

### Lighting
- [x] Lighting variable type  
- [x] Ambient Color (ColorRGBA)  
- [x] Brightness (Float)  
- [x] Sun Color (ColorRGBA)  
- [x] Sun Illuminance (Float)  
- [x] Sun Shadow Maps Enabled (Boolean)  

## VRTX format

### Structure
- [ ] "VRTX" magic number
- [ ] Version (0x01)
- [ ] zstd-compressed payload

### Payload
- [ ] u8 - leading byte
- [ ] string - project id (u64 length prefix + utf8 sha128 hash)
- [ ] u64 - part count

### Parts
- [ ] string - name
- [ ] f32*3 - position
- [ ] f32*4 - rotation
- [ ] f32*3 - scale
- [ ] f32*4 - color
- [ ] u8 - material
- [ ] u32 - unknown
- [ ] u64 - group id

***The rest is unknown for now, which is why we didn't implement the VRTX format yet.***