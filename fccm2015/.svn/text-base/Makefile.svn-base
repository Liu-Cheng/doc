TITLE=scgra-customization
TEXORIG=scgra-customization.tex abstract.tex introduction.tex background.tex framework.tex conclusion.tex relatedwork.tex experiments.tex

BIBFILES=refs.bib 
IMGFILES=

DOCX2TXT := docx2txt.pl

%.tex : %.docx
	$(DOCX2TXT) $< $@

$(TITLE).pdf : $(TEXORIG) $(BIBFILES) $(IMGFILES)
	pdflatex $(TITLE)
	bibtex $(TITLE)
	pdflatex $(TITLE)
	pdflatex $(TITLE)

.PHONY : clean
clean :
	\rm -f *~ *.log $(TITLE).pdf *.aux *.bbl *.blg *.lot *.lof
