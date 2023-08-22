import os

def extract_texture_names(filepath):
	texture_names = []
	with open(filepath, 'r') as file:
		lines = file.readlines()
		for line in lines:
			if line.strip().startswith('"'):
				texture_name = line.strip().split('"')[1]
				texture_names.append(texture_name)
	return texture_names

def find_missing_textures(texture_set_folder, terrainmaps_folder):
	texture_set_files = [f for f in os.listdir(texture_set_folder) if f.endswith('.txt')]
	
	missing_textures_dict = {}
	
	for texture_set_file in texture_set_files:
		texture_set_filepath = os.path.join(texture_set_folder, texture_set_file)
		texture_names_in_set = extract_texture_names(texture_set_filepath)
		
		missing_textures = []
		for texture_name in texture_names_in_set:
			texture_filepath = os.path.join(terrainmaps_folder, texture_name)
			if not os.path.exists(texture_filepath):
				missing_textures.append(texture_name)
		
		if missing_textures:
			missing_textures_dict[texture_set_file] = missing_textures
	
	with open("missing-files.txt", "w") as output_file:
		for texture_set_file, missing_textures in missing_textures_dict.items():
			output_file.write(f"Missing textures in '{texture_set_file}':\n")
			for missing_texture in missing_textures:
				output_file.write(f"  - {missing_texture}\n")
			output_file.write("\n")

if __name__ == "__main__":
	texture_set_folder = r'D:/ymir work/textureset'
	terrainmaps_folder = r'D:/ymir work/terrainmaps'
	find_missing_textures(texture_set_folder, terrainmaps_folder)
