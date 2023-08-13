.PHONY: install
install:
	python3.8 -m venv ./venv
	./venv/bin/pip install -U pip
	./venv/bin/pip install -r requirements.txt

.PHONY: download_weights
download_weights:
	mkdir -p weights
	wget -O weights/genre_classifier.pt https://www.dropbox.com/s/xlax7mfwmzh4rjl/genre_classifier.pt?dl=0
	wget -O weights/rotate_classifier.pt https://www.dropbox.com/s/976wwhi1531hmcg/rotate_classifier.pt?dl=0


