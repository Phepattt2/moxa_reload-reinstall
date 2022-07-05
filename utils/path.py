import os


def get_home_path():
	home_path = "/home"
	home_path = os.path.join(home_path, os.listdir(home_path)[0])
	return home_path
