from random import choices

def random_result(view):
	prob_top ={"a":.95, "b":.01, "c":.04}
	prob_bottom ={"a":.95, "b":.05, "c":.0}
	prob_left ={"a":.99, "b":.005, "c":.005}
	prob_right ={"a":.99, "b":.005, "c":.005}

	if view == "top_view":
		prob = prob_top
	elif view == "bottom_view":
		prob = prob_bottom
	elif view == "left_view":
		prob = prob_left
	elif view == "right_view":
		prob = prob_right
	return choices([0, 1, 2], [prob['a'], prob['b'], prob['c']])[0]