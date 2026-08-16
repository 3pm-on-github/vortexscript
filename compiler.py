import random, json, sys

jsondata = {
  "project_id": random.randbytes(16).hex(),
  "parts": [],
  "lights": [
    {
      "name": "Light",
      "position": {
        "x": 50.0,
        "y": 80.0,
        "z": 30.0
      },
      "rotation": {
        "x": -0.39447272,
        "y": 0.43916786,
        "z": 0.22334667,
        "w": 0.775654
      },
      "color": {
        "r": 0.99999994,
        "g": 0.99999994,
        "b": 0.99999994,
        "a": 1.0
      },
      "illuminance": 10000.0,
      "shadows_enabled": True
    }
  ],
  "groups": []
}
def getpartjson():
    return {
        "name": "Part",
        "position": {
            "x": 0.0,
            "y": -0.5,
            "z": 0.0
        },
        "rotation": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0,
            "w": 1.0
        },
        "scale": {
            "x": 1.0,
            "y": 1.0,
            "z": 1.0
        },
        "color": {
            "r": 1.0,
            "g": 1.0,
            "b": 1.0,
            "a": 1.0
        },
        "material": "Plastic",
        "group": None,
        "cast_shadow": True,
        "anchored": False,
        "can_collide": True,
        "spawn_location": False,
        "baseplate": False,
        "custom_appearance": False,
        "truss": False,
        "textures": [],
        "point_light": None,
        "spot_light": None
    }

def compiler(input, output):
    script = open(input, "r").read()
    variables = {}
    i = 0
    groupi = -1
    tocontinue = False
    for line in script.split("\n"):
        i+=1
        line = line.strip()
        for variable in variables:
            if line.startswith(variable+"."):
                if not "=" in line:
                    name = line[len(variable)+1:-1].split("(")[0].strip()
                    value = line[len(variable)+1:-1].split("(")[1].strip()
                    if name == "addTexture":
                        variables[variable]["textures"].append(variables[value])
                else:
                    name = line[len(variable+"."):].split("=")[0].strip()
                    value = line[len(variable)+1:].split("=")[1].strip()
                    if name == "group":
                        for variable2 in variables:
                            if variable2 == value:
                                variables[variable]["group"] = variables[variable2]["id"]
                    elif value == "true":
                        variables[variable][name] = True
                    elif value == "false":
                        variables[variable][name] = False
                    elif value.startswith("\"") or value.startswith("'"):
                        variables[variable][name] = value[1:-1]
                    elif value.startswith("Vector3"):
                        x = float(value[8:-1].split(",")[0].strip())
                        y = float(value[8:-1].split(",")[1].strip())
                        z = float(value[8:-1].split(",")[2].strip())
                        variables[variable][name]["x"] = x
                        variables[variable][name]["y"] = y
                        variables[variable][name]["z"] = z
                    elif value.startswith("Vector4"):
                        x = float(value[8:-1].split(",")[0].strip())
                        y = float(value[8:-1].split(",")[1].strip())
                        z = float(value[8:-1].split(",")[2].strip())
                        w = float(value[8:-1].split(",")[3].strip())
                        variables[variable][name]["x"] = x
                        variables[variable][name]["y"] = y
                        variables[variable][name]["z"] = z
                        variables[variable][name]["w"] = w
                    elif value.startswith("ColorRGBA"):
                        r = float(int(value[10:-1].split(",")[0].strip()) / 255)
                        g = float(int(value[10:-1].split(",")[1].strip()) / 255)
                        b = float(int(value[10:-1].split(",")[2].strip()) / 255)
                        a = float(int(value[10:-1].split(",")[3].strip()) / 255)
                        variables[variable][name]["r"] = r
                        variables[variable][name]["g"] = g
                        variables[variable][name]["b"] = b
                        variables[variable][name]["a"] = a
                    else:
                        print(f"Error: unknown value at line {str(i)} \"{value}\"")
                        exit()
                tocontinue = True
        if tocontinue:
            tocontinue = False
            continue
        if line.startswith("part"):
            name = line[4:].strip().split("=")[0].strip()
            value = line[4:].strip().split("=")[1].strip()
            if value == "Part()":
                variables[name] = getpartjson()
                variables[name]["type"] = "Part"
                variables[name]["name"] = name
        elif line.startswith("group"):
            name = line[5:].strip().split("=")[0].strip()
            value = line[5:].strip().split("=")[1].strip()
            groupi+=1
            if value == "Group()":
                variables[name] = {"type": "Group", "name": name, "id": groupi, "parent_group": None}
        elif line.startswith("texture"):
            name = line[7:].strip().split("=")[0].strip()
            value = line[7:].strip().split("=")[1].strip()
            if value == "Texture()":
                variables[name] = {"face": "Top", "kind": "Studs"}
        elif line.startswith("//") or line == "":
            pass
        else:
            print(f"Error: unknown line at line {str(i)} \"{line}\"")
            exit()
    for variable in variables:
        if "type" in variables[variable]:
            if variables[variable]["type"] == "Part":
                variables[variable].pop("type")
                jsondata["parts"].append(variables[variable])
            elif variables[variable]["type"] == "Group":
                variables[variable].pop("type")
                variables[variable].pop("id")
                jsondata["groups"].append(variables[variable])
        open(f"{output}", "w").write(json.dumps(jsondata))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: not enough arguments!\nUsage: py compiler.py [input filename] [output filename]")
        exit()
    compiler(sys.argv[1], sys.argv[2])