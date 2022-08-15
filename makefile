install:
	echo "\nmake install\n" &&\
	pip install --upgrade pip &&\
		pip install -r requirements.txt

yamllint:
	yamllint -c yml_lint.yml .

all: install yamllint
