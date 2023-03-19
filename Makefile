.PHONY: all clean

# Find all CSV files and derive corresponding PDF targets
CSV_FILES := $(wildcard *.csv)
PDF_FILES := $(patsubst %.csv,%.pdf,$(CSV_FILES))

all: $(PDF_FILES)

# Generate a PDF file from a CSV file
%.pdf: %.csv
	python generate_keyset.py $< --output-dir $(basename $<)
	python svg_to_pdf.py $(basename $<) --output-file $@

clean:
	rm -rf $(basename $(CSV_FILES))
