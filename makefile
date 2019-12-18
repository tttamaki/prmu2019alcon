all:
	zip prmu-alcon-2019-reference.zip prmu-alcon-2019-reference/*
	zip prmu-alcon-2019-scoring_program-test-dev.zip prmu-alcon-2019-scoring_program-test-dev/*
	zip prmu-alcon-2019-scoring_program-test-challenge.zip prmu-alcon-2019-scoring_program-test-challenge/*
	zip bundle.zip \
		competition.yaml \
		evaluation.html \
		overview.html \
		data.html \
		terms_and_conditions.html \
		logo.png \
		prmu-alcon-2019-reference.zip \
		prmu-alcon-2019-scoring_program-test-dev.zip \
		prmu-alcon-2019-scoring_program-test-challenge.zip

clean:
	rm *.zip
	find . -name ".DS_Store" -print -exec rm {} \;

