def main(file):
	lines = file.read().splitlines()

	workflows = {}
	for line in lines:
		if line == "":
			break
		workflow_name, workflow_rules = line.split("{")
		workflow_rules = workflow_rules[:-1].split(",")
		last_rule = workflow_rules[-1]
		workflow_rules = [rule.split(':') for rule in workflow_rules[:-1]]
		workflow_rules = [[condition, result] for condition, result in workflow_rules]
		workflow_rules.append([last_rule])
		workflows[workflow_name] = workflow_rules
	
	sum_ratings = 0
	for line in lines[len(workflows) + 1:]:
		ratings = line[1:-1].split(',')
		ratings = {rating.split('=')[0]: int(rating.split('=')[1]) for rating in ratings}
		print(ratings)
		
		current_workflow = 'in'
		reached_end = False
		accepted = False
		# loop through the rules for that workflow
		while not reached_end:
			current_rules = workflows[current_workflow]
			print(current_rules)
			for rule in current_rules:
				if len(rule) == 1:
					if rule[0] == 'A':
						accepted = True
						reached_end = True
					elif rule[0] == 'R':
						accepted = False
						reached_end = True
					else:
						current_workflow = rule[0]
					break

				condition, resulting_workflow = rule
				rating_letter = condition[0]
				rating_value = int(condition[2:])
				if condition[1] == '>' and ratings[rating_letter] > rating_value:
					if resulting_workflow == 'A':
						accepted = True
						reached_end = True
					elif resulting_workflow == 'R':
						accepted = False
						reached_end = True
					else:
						current_workflow = resulting_workflow
					break
				elif condition[1] == '<' and ratings[rating_letter] < rating_value:
					if resulting_workflow == 'A':
						accepted = True
						reached_end = True
					elif resulting_workflow == 'R':
						accepted = False
						reached_end = True
					else:
						current_workflow = resulting_workflow
					break
				elif condition[1] == '=' and ratings[rating_letter] == rating_value:
					if resulting_workflow == 'A':
						accepted = True
						reached_end = True
					elif resulting_workflow == 'R':
						accepted = False
						reached_end = True
					else:
						current_workflow = resulting_workflow
					break

		if accepted:
			sum_ratings += sum(ratings.values())

	print(sum_ratings)