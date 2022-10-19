help:
	@just --list

# Run problems for given day. day_no in [01, 02, ... 25]
run day_no:
	@printf "Part A -\n\t" 
	-@python "day_{{day_no}}/a.py"
	@printf "Part B -\n\t"
	-@python "day_{{day_no}}/b.py"
