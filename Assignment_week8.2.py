# ^^^^^^^^^^^^^^Solving Assignment from(60:64)^^^^^^^^^^^^^^^

print('--------------Assignment 1 --------------------')


def get_score(**score):
	for mat, prog in score.items():
		print(f'Your progress in {mat} is >> {prog}')


# get_score( mathematics='70%', physics='99%', communication='97%')


def get_people_scores(*name, **scores):
	if scores:
		if name:
			print(f'Hello {str(name[0])} This Is Your Score Table:')
		for score_key, score_val in scores.items():
			print(f'- {score_key}=> {score_val}')
	elif name:
		print(f'Hello {str(name[0])} You Have No Scores To Show')
	else:  # this from me
		print("You Have No Name or Scores To Show")


# get_people_scores("Osama", Math=90, Science=80, Language=70)

data = {'math': 90,
        'Language': 70,
        'Science': 80}


def get_the_scores(*name, **scores_from_dict):
	if scores_from_dict:

		if name:
			print(f'Hello {str(name[0])} This Is Your Score Table:')
		for score_key, score_val in scores_from_dict.items():
			print(f'- {score_key}=> {score_val}%')
	elif name:
		print(f'Hello {str(name[0])} You Have No Scores To Show')
	else:  # this from me
		print("You Have No Name or Scores To Show")


get_the_scores("Osama", **data)
