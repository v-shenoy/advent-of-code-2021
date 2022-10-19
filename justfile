help:
	@just --list

# Run problems for given day. Values = [01, 02, ... 25]
run day_no:
	python "day_{{day_no}}/a.py"
	python "day_{{day_no}}/b.py"
