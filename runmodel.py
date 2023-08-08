import base64
import requests
import os
import json

##To apply this code,  open the command prompt, go to the folder where you want your result stored or directly modify output directory in line 25,
#and then type "python3 runmodel.py" to start running the code 

api_key = "rQbCvsR.AwG9R7YRyKrCcp8AArfXyd39lpUwPBGz" ##Change to your darwin API key
images_path = "/Users/josephinebocquet/Documents/Data_Josephine/GOPRO_22-09-12/Groupe2" ## Change to your GoPro directory
url = "https://darwin.v7labs.com/ai/models/a8beb161-c8a4-4e97-bc18-14418f3faaf5/infer"

def image_detection(image_name,url):

    image = os.path.join(images_path,image_name)

    with open(image, "rb") as f:
        image_data = base64.b64encode(f.read())

    json_tile = {"image": {"base64": image_data.decode("utf-8")}}
    headers = {"Authorization": f"ApiKey {api_key}"}

    result = requests.post(url, json=json_tile, headers=headers)

    # Save the response to a file
    output_dir = "result"
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
    output_file = os.path.join(output_dir, f"{image_name}.json")
    with open(output_file, "w") as f:
        # Reading from json file
        json.dump(result.json(), f)

# Iterate over each file in the directory
for filename in os.listdir(images_path):

    filepath = os.path.join(images_path, filename)
    
    # Check if the current item is a file
    if os.path.isfile(filepath) and filepath.endswith(".JPG"):
        # Do something with the file
        image_detection(filename, url)
        print(filename+ " finished !")
        
        
        


